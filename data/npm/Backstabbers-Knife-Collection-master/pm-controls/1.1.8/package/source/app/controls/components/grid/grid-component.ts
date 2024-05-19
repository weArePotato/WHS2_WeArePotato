import { 
  Component, 
  ChangeDetectionStrategy,
  ChangeDetectorRef,  
  EventEmitter,
  HostBinding,
  Input,  
  OnChanges,
  OnInit,
  Output,
  SimpleChanges,
  ViewContainerRef,
  ViewChild  
} from '@angular/core';

import * as _ from 'lodash';
import { DialogService } from '../../..//controls/services/dialog/dialog-service';
import { ColumnGroup } from '../../../objects/request/column-group';
import { Dictionary } from '../../../objects/dictionary';
import { GridSelectionMode } from '../../../objects/enums/grid-selection-mode';
import { ColumnFilter } from '../../../controls/components/grid/filters/column-filter';
import { ColumnSort } from '../../../controls/components/grid/sorting/column-sort';
import { ColumnGrouping } from '../../../objects/request/column-grouping';
import { Column } from '../../../objects/request/column';
import { JitComponent } from '../../../controls/components/base/components/jit-component';
import { ColumnType } from '../../../objects/request/column-type';
import { ElementExtensions } from '../../../objects/extensions/element-extensions';
import { GridColumnRange } from '../../../controls/components/grid/grid-columns/grid-column-range';
import { GridSettingsDialog } from '../../../controls/components/grid/grid-settings/grid-settings-dialog';
import { GridExport } from '../../../controls/components/grid/grid-export/grid-export';
import { GridCell } from '../../../controls/components/grid/grid-cell/grid-cell';
import { SortDirection } from '../../../objects/enums/sort-direction';
import { ControlsModule } from '../../../controls/controls-module';

const MILLISECONDS_TO_WAIT_ON_SCROLLING_BEFORE_RENDERING = 5;

@Component({
  selector: 'pm-grid',
  //templateUrl: './app/controls/components/grid/grid.html',
  templateUrl: './grid.html',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class GridComponent implements OnChanges, OnInit {

  constructor(
    private changeDetectorRef: ChangeDetectorRef,
    private viewContainerRef: ViewContainerRef,
    private dialog: DialogService) {

    this.el = viewContainerRef.element.nativeElement;
  }

  @Input() GridClass: string;
  @Input() SelectedCell;
  @Input() SelectedRow;
  @Output() SelectedRowChange: EventEmitter<any> = new EventEmitter<any>();
  @Input() SelectedCells;
  @Input() SelectedRows;
  @Input() RowFocus;
  @Input() ColumnFocus;
  @Input() HeightPx: any = 0;
  @Input() WidthPx: any = 0;
  @Input() PanelWidthPx: any = 0;
  @Input() FrozenColumnCount: number;
  @Input() HierarchyColumnIndex: number;
  @Input() HierarchyColumnProperty: any;
  @Input() ShowRowNumbers: boolean = true;
  @Input() ShowFooter: boolean = false;
  @Input() ShowColumnGroups: boolean = false;
  @Input() ColumnGroups: Dictionary<ColumnGroup>;
  @Input() ContextMenu: any;
  @Input() LastColumnFill: boolean;
  @Input() HideRowResize: boolean;
  @Input() CalculateRowSize: Function;  
  @Input() CellMouseOver: string;
  @Input() RowMouseOver: string;
  @Input() GridSelectionMode: GridSelectionMode = GridSelectionMode.Cell;
  @Input() IsBusy: boolean;
  @Input() BusyMessage: string;
  @ViewChild('gridRowVerticalContainer') gridRowVerticalContainer: any;
  @ViewChild('gridRowHorizontalContainer') gridRowHorizontalContainer: any;
  @ViewChild('gridColumnHorizontalContainer') gridColumnHorizontalContainer: any;
  @ViewChild('gridColumnGroupContainer') gridColumnGroupContainer: any;  
  @ViewChild('gridFooterContainer') gridFooterContainer: any;
  @ViewChild('gridTableScrollbarHorizontalContainer') gridTableScrollbarHorizontalContainer: any;
  @ViewChild('gridTableScrollbarVerticalContainer') gridTableScrollbarVerticalContainer: any;
  @ViewChild('gridTableScrollbarHorizontalScrollPanel') gridTableScrollbarHorizontalScrollPanel: any;
  TopHeightPx: string;
  TransformY: string;
  // to react to the width / height changes
  // @HostBinding('style.flex-grow')
  // @Input() FlexGrow: string;

  get Grid(): GridComponent {
    return this;
  }

  Rows: Array<any> = new Array<any>();
  VisibleRows: Array<any> = new Array<any>();
  RowNumbers: Array<any>;  
  private el: any;
  ScrollTop: any;
  ScrollLeft: any;  
  ContainerHeight: any;
  ContainerWidth: any;
  VisibleColumns: Array<any> = new Array<any>();
  Filters: Dictionary<ColumnFilter> = new Dictionary<ColumnFilter>();
  Sorts: Dictionary<ColumnSort> = new Dictionary<ColumnSort>();
  ColumnGroupings: Array<ColumnGrouping> = new Array<ColumnGrouping>();

  private itemsSource: Array<any> = [];
  @Input('ItemsSource')
  get ItemsSource(): Array<any> {
    return this.itemsSource;
  }

  set ItemsSource(value: Array<any>) {
    if (value === this.itemsSource) return;
    this.itemsSource = value;
    this.createCollectionView();
    this.handleVerticalScroll(this.ScrollTop);
  }
  
  private columns: Dictionary<Column> = new Dictionary<Column>();
  @Input('Columns')
  get Columns(): Dictionary<Column> {
    return this.columns;
  }

  set Columns(value: Dictionary<Column>) {

    if (value) {
      for (var i=0; i < value.Values.length; i++) {
        var item = value.Values[i];
        if (item.CellTemplate) {
          item.CellTemplateComponent = JitComponent.createComponent(item.CellTemplate, item.CellModules);
        } else if (item.Type.IsBoolean) {
          item.CellTemplate = "<pm-check-box class=\"control-center\" IsReadOnly=\"true\" [IsChecked]=\"Row['" + item.Property + "']\"></pm-check-box>";
          item.CellTemplateComponent = JitComponent.createComponent(item.CellTemplate, item.CellModules);
        }
        if (item.HeaderTemplate) {
          item.HeaderTemplateComponent = JitComponent.createComponent(item.HeaderTemplate, item.HeaderComponents);
        }
      }

      if (value.Values.some((item) => ColumnType.Fill == item.Type) == false)
        value.add("_fill", Column.FillerColumn);
    }
    this.columns = value;
    this.calculateWidth();
    this.changeDetectorRef.detectChanges();
    //this.createCollectionView();
    //this.handleVerticalScroll(this.ScrollTop);
  }

  private rowHeight: number = 30;
  @Input('RowHeight')
  get RowHeight(): number {
    return this.rowHeight;
  }

  set RowHeight(value: number) {
    this.rowHeight = value;
    if (this.Rows)
    {
      this.calculateRowHeights(this.Rows);
    }
  }

  private columnHeaderHeight: number = 24;
  @Input('ColumnHeaderHeight')
  get ColumnHeaderHeight(): number {
    return this.columnHeaderHeight;
  }

  set ColumnHeaderHeight(value: number) {
    this.columnHeaderHeight = value;
  }

  ngOnInit() {
    this.calculateWidth();

    this.ContainerWidth = ElementExtensions.width(this.gridColumnHorizontalContainer);
    this.ContainerHeight = ElementExtensions.height(this.gridTableScrollbarVerticalContainer);
    this.handleHorizontalScroll(0);
    this.handleVerticalScroll(0);
  }

  ngDoCheck() {
    if (this.ContainerHeight != ElementExtensions.height(this.gridTableScrollbarVerticalContainer))
    {
      this.ContainerHeight = ElementExtensions.height(this.gridTableScrollbarVerticalContainer);
      this.handleVerticalScroll(this.ScrollTop);      
    }

    if (this.ContainerWidth != ElementExtensions.width(this.gridColumnHorizontalContainer))
    {
      this.SizeHorizontalScrollbar();
      this.ContainerWidth = ElementExtensions.width(this.gridColumnHorizontalContainer);
      this.handleHorizontalScroll(this.ScrollLeft);
    }
  }

  ngOnChanges(changes: SimpleChanges) {

    if (changes['Columns']) {
      this.handleHorizontalScroll(this.ScrollLeft);
    }

    // if (changes['ItemsSource']) {

    // }

    // if (changes['FrozenColumnCount']) {
    // }

    // if (changes['HierarchyColumnIndex']) {
    // }

    // if (changes['HierarchyColumnProperty']) {
    // }

    // if (changes['ShowRowNumbers']) {
    // }

    // if (changes['ShowFooter']) {
    // }

    // if (changes['ShowColumnGroups']) {
    // }
  }

  get RegularColumns() : Array<Column> {
    if (this.Columns)
    {
      var columns = [];
      for (var i = 0; i < this.Columns.Values.length; i++) {
        var column = this.Columns.Values[i];
        if (!column.IsHidden)
          columns.push(column);
      }
      return columns.slice(this.FrozenColumnCount);
    }
    return [];
  }

  get FrozenColumns(): Array<Column> {    
    if (this.Columns && this.FrozenColumnCount > 0) {
      var columns = [];
      for (var i = 0; i < this.Columns.Values.length; i++) {
        var column = this.Columns.Values[i];
        if (!column.IsHidden)
          columns.push(column);
      }
      return columns.slice(0, this.FrozenColumnCount);
    }
    return [];
  }

  get RegularColumnGroupings(): Array<ColumnGrouping> {
    if (this.ColumnGroupings) {
      return this.ColumnGroupings;
    }
    return [];
  }

  get FrozenColumnGroupings(): Array<ColumnGrouping> {
    if (this.ColumnGroupings) {
      return this.ColumnGroupings;
    }
    return [];
  }

  get FrozenColumnWidthPx(): number {
    var frozenColumns = this.FrozenColumns;
    if (frozenColumns.length > 0) {
      var width = 0;
      for (var i = 0; i < frozenColumns.length; i++) {
        var column = frozenColumns[i];
        width += column.Width.Value;
      }
      return width;
    }
    return 0;
  }

  get VerticalScrollbarTopPx(): number {
    if (this.ShowColumnGroups) {
      return 23 + 24;
    }
    return 23;
  }

  get VerticalScrollbarBottomPx(): number {
    if (this.ShowFooter) {
      return 18 + 24;
    }
    return 18;
  }

  createCollectionView() {
    if (!this.ItemsSource) return;
    var items = this.ItemsSource.slice();    
    //this._isExpanded

    if (this.Filters.any()) {
      for (var i = 0; i < this.Filters.length; i++)
      {
        var filter = this.Filters.Values[i];

        items = items.filter(function(item) 
        {
          return filter.Filter(item);
        });
      }
    }

    if (this.Sorts.any()) {
      for (var i = 0; i < this.Sorts.length; i++) {
        var sort = this.Sorts.Values[i];

        items = items.sort(function(a, b) 
        {
          return sort.Sort(a, b);
        });
      }
    }

    if (items)
    {
      items = this.getAllItems(items);
      this.calculateRowHeights(items);
    }
    
    this.Rows = items;
    this.RowNumbers = Array.from(Array(this.Rows.length).keys());
    //this.calculateRowHeights(this.Rows);
  }

  onVerticalScroll(event) {
    const currentScrollTop = this.gridRowVerticalContainer.nativeElement.scrollTop = event.target.scrollTop;
    //this.handleVerticalScroll(currentScrollTop);
    setTimeout(() => {
      const latestScrollTop = this.gridRowVerticalContainer.nativeElement.scrollTop;

      if (currentScrollTop !== latestScrollTop) {
        return;
      }

      this.handleVerticalScroll(latestScrollTop);

    }, MILLISECONDS_TO_WAIT_ON_SCROLLING_BEFORE_RENDERING);
  }

  private async handleVerticalScroll(scrollTop: number): Promise<any> {
    this.ScrollTop = scrollTop;
    const viewPortStartIndex = this.getViewPortStartIndex();
    const viewPortEndIndex = this.getViewPortEndIndex(viewPortStartIndex); 
    this.VisibleRows = this.Rows.slice(viewPortStartIndex, viewPortEndIndex);
    this.changeDetectorRef.detectChanges();
  }

  private getViewPortStartIndex() {
    if ( this.CalculateRowSize) {
      // do a binary search on the elements to find the first item.
      return Math.max(_(this.Rows).map(i => i._top).sortedIndex(this.ScrollTop)-1,0);
    }
    return Math.floor(this.ScrollTop / this.RowHeight);
  }

  private getViewPortEndIndex(startIndex : number) {
    if (this.CalculateRowSize) { 
      let i = startIndex;
      while(i < this.Rows.length && this.Rows[i]._top < this.ContainerHeight+this.ScrollTop) 
        i++;

      return i;
    }

    return startIndex+Math.ceil(this.ContainerHeight / this.RowHeight) + 1;
  }

  onHorizontalScroll(event) {
    const currentScrollLeft 
      = this.gridRowHorizontalContainer.nativeElement.scrollLeft 
      = this.gridColumnHorizontalContainer.nativeElement.scrollLeft
      = event.target.scrollLeft;
    if (this.ShowFooter)
      this.gridFooterContainer.nativeElement.scrollLeft = event.target.scrollLeft;
    if (this.ShowColumnGroups)
      this.gridColumnGroupContainer.nativeElement.scrollLeft = event.target.scrollLeft;
    //this.handleHorizontalScroll(currentScrollLeft);
    setTimeout(() => {
       const latestScrollLeft = this.gridRowHorizontalContainer.nativeElement.scrollLeft;
        if (currentScrollLeft !== latestScrollLeft) {
          return;
      }
      this.handleHorizontalScroll(latestScrollLeft);
    }, MILLISECONDS_TO_WAIT_ON_SCROLLING_BEFORE_RENDERING);
  }

  private async handleHorizontalScroll(scrollLeft: number): Promise<any> {
    this.ScrollLeft = scrollLeft;
    if (!this.Columns) return;
    var width = ElementExtensions.width(this.gridColumnHorizontalContainer) + scrollLeft + this.FrozenColumnWidthPx;

    this.FrozenColumns.forEach(c => c.IsVisible = true);
    var columns = this.RegularColumns;
    var visibleColumns = GridColumnRange.GetVisibleColumns(columns, scrollLeft, width);

    if (this.VisibleColumns.length == 0) {
      visibleColumns.forEach(c => c.IsVisible = true);
    } else {
      var visible = _.difference(visibleColumns, this.VisibleColumns);
      var hidden = _.difference(this.VisibleColumns, visibleColumns);

      visible.forEach(c => c.IsVisible = true);
      hidden.forEach(c => c.IsVisible = false);
    }

    this.VisibleColumns = visibleColumns;
    this.changeDetectorRef.detectChanges();    
  }

  calculateWidth() {
    var width = 0;
    var currentGroupName, columnGroupings = [], currentColumnGrouping;
    if (this.Columns)
    {
      for (var i=0; i<this.Columns.Values.length; i++)
      {
        var column = this.Columns.Values[i];
        column['_columnNumber'] = i;
        if (!column.IsHidden) {
          column['_left'] = width;
          width += column.Width.Value;
          column['_right'] = width;
        }

        if (column.Type.IsFill) {
          var element1 = ElementExtensions.width(this.gridRowHorizontalContainer);
          if (width < element1) {
            var amount = element1 - width;
            column['_left'] = width;
            //width += 100;
            column.Width.Value = amount;
            width += column.Width.Value;
            column['_right'] = width;
          } else if (column.Width.Value < 1) {
            column.IsHidden = true;
          }
        }

        if (this.ShowColumnGroups && this.ColumnGroups) {
          if (column.ColumnGroupName == currentGroupName) {
            currentColumnGrouping.Width.Value += column.Width.Value;
          } else {
            currentGroupName = column.ColumnGroupName;
            var group = <ColumnGroup> this.ColumnGroups[currentGroupName];
            if (group) {
              currentColumnGrouping = new ColumnGrouping(group.Name, group.HeaderTextAlign);
              currentColumnGrouping.Width.Value = column.Width.Value;
              columnGroupings.push(currentColumnGrouping);
            }
          }
        }
      }
      
      if (this.ShowColumnGroups && columnGroupings) {
        this.ColumnGroupings = columnGroupings;
      }
    }

    this.WidthPx = width;
    this.SizeHorizontalScrollbar();    
  }

  SizeHorizontalScrollbar() {
    var panel = ElementExtensions.width(this.gridTableScrollbarHorizontalScrollPanel);
    var container = ElementExtensions.width(this.gridTableScrollbarHorizontalContainer);
    var diff = container - panel;
    this.PanelWidthPx = this.WidthPx - diff;
  }

  getAllItems(items: Array<any>): Array<any>{
    if (this.HierarchyColumnProperty && items) {
      var all = [];
      for (var i=0; i<items.length; i++) {
        var item = items[i];

        all.push(item);
        if (item['_isExpanded']) {
          var children = this.getAllItems(item[this.HierarchyColumnProperty]);
          all.push(...children);
        }
      }
      return all;
    }

    return items;
  }

  calculateRowHeights(items: Array<any>) {
    var totalHeight = 0;
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      item['_top'] = totalHeight;
      item['_rowNumber'] = i + 1;

      if (item['_rowResizeHeight'])
        item['_rowHeight'] = item['_rowResizeHeight'];
      else if (this.CalculateRowSize)
        item['_rowHeight'] = this.CalculateRowSize(item);
      else
        item['_rowHeight'] = this.RowHeight;
      
      totalHeight += item['_rowHeight'];
    }

    this.HeightPx = totalHeight;
  }

  showSettings() {
    GridSettingsDialog.Show(this);
  }

  mouseWheelUp(event: any) {
    this.gridTableScrollbarVerticalContainer.nativeElement.scrollTop -= event.wheelDelta;
  }

  mouseWheelDown(event: any) {
    this.gridTableScrollbarVerticalContainer.nativeElement.scrollTop -= event.wheelDelta;
  }

  ExportToExcel() {
    var gridExport = new GridExport();
    gridExport.ExportToXlsx(this, "export");
  }

  SetRowFocus(row: any) {
    var rowFocus = {};
    rowFocus[row['_rowNumber']] = true;
    this.RowFocus = rowFocus;

    var columnFocus = {};
    for (var i=0; i<this.Columns.length; i++) {
      var column = this.Columns.Values[i];
      columnFocus[column.Key] = true;
    }

    this.ColumnFocus = columnFocus;
  }
  
  SetColumnFocus(row: any, column: any) {
    var rowFocus = {};
    rowFocus[row['_rowNumber']] = true;
    this.RowFocus = rowFocus;

    var columnFocus = {};
    columnFocus[column.Key] = true;
    this.ColumnFocus = columnFocus;
  }

  SelectRow(row: any) {
    var rows = {};
    rows[row['_rowNumber']] = true;
    
    this.SetRowFocus(row);
    this.SelectedCells = {};
    this.SelectedRows = rows;
    this.SelectedRow = row;
    this.SelectedRowChange.emit(this.SelectedRow);
    this.changeDetectorRef.detectChanges();
  }

  SelectCell(cell: GridCell) {
    if (this.GridSelectionMode == GridSelectionMode.Row) 
    {
      this.SelectRow(cell.Row);
      return;
    }
    var cells = {};
    cells[cell.Row['_rowNumber'] + cell.Column.Key] = true;
    cells[cell.Row['_rowNumber']] = true;
    this.SetColumnFocus(cell.Row, cell.Column);

    this.SelectedCells = cells;    

    var rows = {};
    //rows[cell.Row['_rowNumber']] = true;
    this.SelectedCell = cell;
    this.SelectedRows = rows;
    this.SelectedRow = cell.Row;
    this.SelectedRowChange.emit(this.SelectedRow);
    this.changeDetectorRef.detectChanges();
  }

  ExpandCollapseHierarchyRow(row: any) {
    row['_isExpanded'] = !row['_isExpanded'];    
   
    if (this.Rows) {
      this.createCollectionView();
      this.RefreshGrid();
    }
  }

  ShowHideColumn(column: Column) {
    column.IsHidden = !column.IsHidden; 
    this.calculateWidth();
    this.handleHorizontalScroll(this.ScrollLeft);
  }

  ResizeColumn(column: Column) {
    this.calculateWidth();
    this.handleHorizontalScroll(this.ScrollLeft);
  }

  ResizeRow(row: any) {
    this.calculateRowHeights(this.Rows);
    this.handleVerticalScroll(this.ScrollTop);
  }

  SetFilter(column: Column, filterValue: string, searchType: number, selectedDistinctValues: Array<any>) {
    if (this.Filters.containsKey(column.Key)) {
      this.Filters.remove(column.Key);
    }

    column['_hasFilter'] = true;
    column['_selectedDistinctValues'] = selectedDistinctValues;
    this.Filters.add(column.Key, new ColumnFilter(column, filterValue, searchType, selectedDistinctValues));
    this.createCollectionView();
    this.handleVerticalScroll(this.ScrollTop);
  }

  ClearFilter(column: Column) {
    if (this.Filters.containsKey(column.Key)) {
      column['_hasFilter'] = false;
      this.Filters.remove(column.Key);
    }

    this.createCollectionView();
    this.handleVerticalScroll(this.ScrollTop);
  }

  SetSort(column: Column, direction: SortDirection) {
    if (this.Sorts.containsKey(column.Key)) {
      var sort = this.Sorts[column.Key];
      if (sort.Direction == direction) {
        column['_hasSort'] = undefined;
        this.Sorts.remove(column.Key);
      } else {
        sort.Direction = direction;
        column['_hasSort'] = { direction: direction };
      }
    } else {
      this.Sorts.add(column.Key, new ColumnSort(column, direction));
      column['_hasSort'] = { direction: direction };      
    }

    this.createCollectionView();
    this.handleVerticalScroll(this.ScrollTop);
  }

  ToggleSort(column: Column) {
    // When toggling the sort order, the column will go from No Sort -> Ascending -> Descending -> No Sort.

    if (this.Sorts.containsKey(column.Key)) {
      var sort = this.Sorts[column.Key];
      if (sort.Direction == SortDirection.Descending) {
        // Remove the sort because the order is on Descending.
        column['_hasSort'] = undefined;
        this.Sorts.remove(column.Key);
      } else {
        // Because there is an existing sort and it's not descending, then the current sort must be ascending.
        // So, flip it to descending.
        sort.Direction = SortDirection.Descending;
        column['_hasSort'] = { direction: SortDirection.Descending };
      }
    } else {
      // There was no existing sort order. So, start with ascending.
      this.Sorts.add(column.Key, new ColumnSort(column, SortDirection.Ascending));
      column['_hasSort'] = { direction: SortDirection.Ascending };      
    }

    this.createCollectionView();
    this.handleVerticalScroll(this.ScrollTop);
  }

  ExpandAll() {
    if (this.ItemsSource) {
      var items = this.ItemsSource.slice();

      for (var i=0; i<items.length; i++) {
        var item = items[i];
        item['_isExpanded'] = true;
      }

      this.createCollectionView();
      this.RefreshGrid();
    }
  }

  CollapseAll() {
    if (this.ItemsSource) {
      var items = this.ItemsSource.slice();

      for (var i = 0; i < items.length; i++) {
        var item = items[i];
        item['_isExpanded'] = false;
      }
      this.createCollectionView();
      this.RefreshGrid();
    }
  }

  ToggleHighlightRow(row: any) {
    row['_isHighlighted'] = true;
    this.RaiseChange();
  }

  RaiseChange() {
    this.changeDetectorRef.detectChanges();
  }
  
  RefreshGrid() {
    this.handleHorizontalScroll(this.ScrollLeft);
    this.handleVerticalScroll(this.ScrollTop);
  }

  get IsDevMode() {
    return ControlsModule.IsDevMode;
  }
}