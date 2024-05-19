import {
    Component,
    EventEmitter,
    forwardRef,
    HostListener,
    Input,
    Output,
    ViewChild,
    ViewContainerRef
} from '@angular/core';
import { ModalDialog } from '../../../../controls/components/modal/modal-dialog'; 
import { ContextMenuComponent } from '../../../../controls/components/context-menu/context-menu-component';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { ListBoxComponent } from '../../../../controls/components/boxes/list-box/list-box-component';
import { Column } from '../../../../objects/request/column';
import { SortDirection } from '../../../../objects/enums/sort-direction';
import { GridCell } from '../../../../controls/components/grid/grid-cell/grid-cell';
import { DateExtensions } from '../../../../objects/extensions/date-extensions';
import { ControlsModule } from '../../../../controls/controls-module';

@Component({
    //templateUrl: './app/controls/components/grid/filters/column-filter-popup.html',
    templateUrl: './column-filter-popup.html',
    styles: [`
    :host {   
      position: absolute;
      height: 100%;
      width: 100%;
      top: 0px;
      z-index: 1000;
      pointer-events: none;
    }
  `]
})
export class ColumnFilterPopup extends ModalDialog {
    constructor() {
        super();
    }

    @ViewChild('contextMenu') ContextMenu: ContextMenuComponent;
    Grid: GridComponent;
    @Input() ColumnFilter: any;
    ColumnFilterSearchOptions: Array<any> = [];
    @Input() SelectedColumnFilterSearchOption: any;
    @ViewChild(forwardRef(() => ListBoxComponent)) listBox: ListBoxComponent; 

    @Input() Column: Column; 

    private columnFilterDistinctItems: Array<any> = [];
    get ColumnFilterDistinctItems(): Array<any> {
        return this.columnFilterDistinctItems;
    }

    set ColumnFilterDistinctItems(value: Array<any>) {
        this.columnFilterDistinctItems = value;
    }

    private selectedColumnFilterDistinctItems: Array<any> = [];
    get SelectedColumnFilterDistinctItems(): Array<any> {
        return this.selectedColumnFilterDistinctItems;
    }

    set SelectedColumnFilterDistinctItems(value: Array<any>) {
        this.selectedColumnFilterDistinctItems = value;
        this.Grid.SetFilter(this.Column, this.ColumnFilter, this.SelectedColumnFilterSearchOption ? this.SelectedColumnFilterSearchOption.Value: null, this.SelectedColumnFilterDistinctItems);
    }
    
    @HostListener("click", ["$event"])
    public onClick(event: any): void {
        event.stopPropagation();
    }

    InitializeFilters() {
        // Set the filter options based on the data type of the column.
        this.SetFilterOptions();

        if (this.Grid.Filters.containsKey(this.Column.Key)) {
            this.ColumnFilter = this.Grid.Filters[this.Column.Key].FilterText;
            this.SelectedColumnFilterSearchOption = this.ColumnFilterSearchOptions.find(x => x.Value == this.Grid.Filters[this.Column.Key].SearchType);
        } else {
            this.ColumnFilter = undefined;
        }

        if (this.Column['_hasFilter'] === undefined || this.Column['_hasFilter'] === false)
        {
            // Since no filter haa been set we need to store these distinct values.
            this.Column['_distinctValues'] =  this.GetDistinctItems(this.Column);
        }

        this.SetDistinctItems(this.Column);
    }
    
    OnHideColumn() {
        this.Grid.ShowHideColumn(this.Column);
    }

    OnSortAscendingColumn() {
        this.Grid.SetSort(this.Column, SortDirection.Ascending);
    }

    OnSortDescendingColumn() {
        this.Grid.SetSort(this.Column, SortDirection.Descending);
    }

    OnClearFilter() {
        this.Column['_hasFilter'] = false;
        this.Column['_selectedDistinctValues'] = undefined;
        this.Column['_distinctValues'] = undefined;

        this.Grid.ClearFilter(this.Column);
        this.SelectedColumnFilterSearchOption = undefined;
        this.ColumnFilter = "";
        
        this.SelectedColumnFilterDistinctItems.length = 0;
        this.ColumnFilterDistinctItems.length = 0;
        this.Column['_distinctValues'] =  this.GetDistinctItems(this.Column);
        this.SetDistinctItems(this.Column);
    }

    OnSetFilter() {
        if (this.ColumnFilter && this.SelectedColumnFilterSearchOption) {
            this.Grid.SetFilter(this.Column, this.ColumnFilter, this.SelectedColumnFilterSearchOption.Value, this.SelectedColumnFilterDistinctItems);
        }
        else {
            // User either did not specify filter criteria or removed the filter text and/or search type.
            this.SelectedColumnFilterSearchOption = undefined;
            this.ColumnFilter = "";
            this.Grid.SetFilter(this.Column, undefined, undefined, this.SelectedColumnFilterDistinctItems);
        }
    }

    OnColumnSetSize(column: Column) {

    }

    OnDistinctColumnFilter(column: Column) {
        if (this.SelectedColumnFilterDistinctItems === undefined || this.SelectedColumnFilterDistinctItems.length === 0){
            // The user deselected all of the column filters. For now we will reset everything to get all distinct values back.
            this.OnClearFilter();
        }
        else {
            this.Grid.SetFilter(column, this.ColumnFilter, this.SelectedColumnFilterSearchOption ? this.SelectedColumnFilterSearchOption.Value: null, this.SelectedColumnFilterDistinctItems);
        }
    }

    SetFilterOptions() {
        if (this.Column.Type.IsNumber) {
            this.ColumnFilterSearchOptions = [
                { Name: 'Equals (=)', Value: 0 },
                { Name: 'Is Less Than (<)', Value: 1 },
                { Name: 'Is Less Than or Equal to (<=)', Value: 2 },
                { Name: 'Is Greater Than (>)', Value: 3 },
                { Name: 'Is Greater Than or Equal to (>=)', Value: 4 },
            ];
        } else if (this.Column.Type.IsDate || this.Column.Type.IsDateTime) {
            this.ColumnFilterSearchOptions = [
                { Name: 'Is After', Value: 0 },
                { Name: 'Is On or After', Value: 1 },
                { Name: 'Is Before', Value: 2 },
                { Name: 'Is On or Before', Value: 3 },
            ];
        } else {
            this.ColumnFilterSearchOptions = [
                { Name: 'Contains', Value: 0 },
                { Name: 'Does not contain', Value: 1 },
                { Name: 'Starts with', Value: 2 },
                { Name: 'Ends with', Value: 3 },
            ];
        }
    }
    
    IsChecked(item: any) {
        if (this.listBox.SelectedItems && this.listBox.SelectedItems.includes(item))
            return true;
            
        return false;
    } 

    GetDistinctItems(column: Column) {
        var distinctItems: Array<any> = [];
        var unique = {};

        // Identify all unique values.
        for (var i = 0; i < this.Grid.Rows.length; i++) {
            var cellValue = GridCell.GetProperty(column, this.Grid.Rows[i]);
            if ( typeof(unique[cellValue])=="undefined") {
                distinctItems.push(cellValue);
            }
            unique[cellValue] = 0;
        }

        // Return the unique values sorted by data type.
        return this.GetItemsSortedByDataType(distinctItems);
    }

    GetItemsSortedByDataType(items: Array<any>){
        if (this.Column.Type.IsNumber) {
            return items.sort(this.SortByNumber);
        } else if (this.Column.Type.IsDate || this.Column.Type.IsDateTime) {
            return items.sort(this.SortByDateAscending);
        } else {
            return items.sort();
        }
    }

    SetDistinctItems(column: Column) {
        var isChecked: Boolean = false;

        var selectedItems: Array<any> = column['_selectedDistinctValues'];
        var distinctItems: Array<any> = column['_distinctValues'];
        
        var itemsSource: Array<any> = [];
        var maxDistinctItems: number = 10000 < distinctItems.length ? 10000 : distinctItems.length;

        // Construct ItemsSource. Set to "Checked" all previously selected values.
        for (var i = 0; i < maxDistinctItems; i++) {
            var value = distinctItems[i];
            var item = {Name: value, IsChecked: false};
            
            if (selectedItems != undefined) {
                if(selectedItems.map(function(e) { return e.Name; }).indexOf(value)!==-1){
                    item.IsChecked = true;
                    this.selectedColumnFilterDistinctItems.push(item);
                }
            }
            itemsSource.push(item);
        }

        this.ColumnFilterDistinctItems = itemsSource;
    }

    SortByNumber(a,b) {
        return a - b;
    }

    SortByDateAscending(a,b) {
        return (DateExtensions.GetDate(b, 'DD-MMM-YYYY') - DateExtensions.GetDate(a, 'DD-MMM-YYYY')) * -1;
    }

    static Show(event: MouseEvent, grid: GridComponent, column: Column) {
        var popup = <ColumnFilterPopup>ControlsModule.dialog.Show(ColumnFilterPopup);

        popup.Column = column;
        popup.Grid = grid;
        popup.InitializeFilters();
        popup.ContextMenu.Open.subscribe((value: boolean) => {
            if (!value)
                popup.Close(value);
        });
        popup.ContextMenu.Show(event.clientX, event.clientY);
    }
}