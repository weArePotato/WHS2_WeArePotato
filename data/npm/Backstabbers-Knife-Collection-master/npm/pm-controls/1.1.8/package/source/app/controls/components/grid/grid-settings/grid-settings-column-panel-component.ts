import { 
    ChangeDetectorRef,
    ChangeDetectionStrategy,
    Component, 
    Input,
    SimpleChanges,
    ViewChild
} from '@angular/core';
import { ClipboardService } from '../../../../controls/services/clipboard/clipboard-service';
import { ColumnType } from '../../../../objects/request/column-type';
import { ColumnAggregate } from '../../../../objects/request/column-aggregate';
import { ModalDialog } from '../../../../controls/components/modal/modal-dialog';
import { Column } from '../../../../objects/request/column';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { Dictionary } from '../../../../objects/dictionary';
import { GridLength } from '../../../../objects/request/grid-length';

@Component({
    selector: 'pm-grid-settings-column-panel',
    //templateUrl: './app/controls/components/grid/grid-settings/grid-settings-column-panel.html',
    templateUrl: './grid-settings-column-panel.html',
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class GridSettingsColumnPanelComponent  {
    constructor(
        private clipboard: ClipboardService,
        private changeDetectorRef: ChangeDetectorRef) {
        changeDetectorRef.detach();
            
        this.TypesItemsSource = [
            ColumnType.Boolean,
            ColumnType.Currency,
            ColumnType.Date,
            ColumnType.DateTime,
            ColumnType.Number,
            ColumnType.String
        ];

        this.AlignItemsSource = [
            "left",
            "center",
            "right"
        ];

        this.TrueFalseItemsSource = [
            "true",
            "false"
        ];

        this.AggregateItemsSource = [
            ColumnAggregate.Sum
        ];
    }

    Code: any;
    TypesItemsSource;
    TrueFalseItemsSource;
    AlignItemsSource;    
    AggregateItemsSource;
    SelectedType;
    SelectedIsHidden;
    SelectedHeaderTextAlign;
    SelectedCellTextAlign;
    SelectedTabIndex: number = 0;
    HasSelection: boolean;
    @Input() Dialog: ModalDialog;
    @Input() CurrentColumn: any = {};
    @Input() GridColumns: Column[];

    private grid: GridComponent;
    @Input('Grid')
    get Grid(): GridComponent {
        return this.grid;
    }

    set Grid(value: GridComponent) {
        this.grid = value;
        this.GridColumns = this.grid.Columns ? this.grid.Columns.Values : [];
        this.changeDetectorRef.detectChanges();
    }

    private selectedItem: any = {};
    @Input('SelectedItem')
    get SelectedItem(): any {
      return this.selectedItem;
    }
  
    set SelectedItem(value: any) {
      this.selectedItem = value;
      this.CurrentColumn = Object.assign({}, value);

      if (value) {
          this.HasSelection = true;
      } else {
          this.HasSelection = false;
      }
      this.changeDetectorRef.detectChanges();
    }

    get Columns()
    {
        return new Dictionary<Column>([        
            { key: "Name", value: new Column("Name", "Name", "Name", ColumnType.String, new GridLength(140)) },
            { key: "Property", value: new Column("Property", "Property", "Property", ColumnType.String, new GridLength(100)) },
            { key: "Type", value: new Column("Type", "Type", "Type.Name", ColumnType.String, new GridLength(100)) },
            { key: "Width", value: new Column("Width", "Width", "Width.Value", ColumnType.String, new GridLength(100)) },
            { key: "IsHidden", value: new Column("IsHidden", "IsHidden", "IsHidden", ColumnType.String, new GridLength(80)) },
            { key: "HeaderTextAlign", value: new Column("HeaderTextAlign", "HeaderTextAlign", "HeaderTextAlign", ColumnType.String, new GridLength(100)) },
            { key: "CellTextAlign", value: new Column("CellTextAlign", "CellTextAlign",  "CellTextAlign", ColumnType.String, new GridLength(100)) },
            { key: "CellTemplate", value: new Column("CellTemplate", "CellTemplate", "CellTemplate", ColumnType.String, new GridLength(100)) },
            { key: "HeaderTemplate", value: new Column("HeaderTemplate", "HeaderTemplate", "HeaderTemplate", ColumnType.String, new GridLength(100)) },
            { key: "Aggregate", value: new Column("Aggregate", "Aggregate", "Aggregate.Name", ColumnType.String, new GridLength(100)) },
            { key: "IsVisible", value: new Column("IsVisible", "IsVisible", "IsVisible", ColumnType.String, new GridLength(80)) },
        ]);
    } 

    ngOnChanges(changes: SimpleChanges) {
        if (changes['Grid']) {
            var columns = "";
            if (this.Grid.Columns) {
                for (var i = 0; i < this.Grid.Columns.Values.length; i++)
                {
                    var column = this.Grid.Columns.Values[i];
                    var type = column.Type.constructor.name + "." + column.Type.Name;
                    columns += "{ key: \"" + column.Key + "\", value: new Column(\"" + column.Key + "\", \"" + column.Name + "\", \"" + column.Property + "\", " + type + " , new GridLength(" + column.Width.Value + ")) },\r\n"
                }
            }
            this.Code = columns;
            this.changeDetectorRef.detectChanges();
        }
    }

    OnCopy() {
        this.clipboard.Copy(this.Code);
    }

    OnSave() {
        if (this.SelectedTabIndex == 0) {
            var columns = this.GridColumns;
            var index = columns.indexOf(this.SelectedItem);
            columns[index] = this.CurrentColumn;
            var toDictionary = [];
            for (var i = 0; i < columns.length; i++) {
                var column = columns[i];
                toDictionary.push({ key: column.Key, value: column });
            }

            this.Grid.Columns = new Dictionary<Column>(toDictionary);
            this.GridColumns = columns.slice();
            this.changeDetectorRef.detectChanges();
        } else if (this.SelectedTabIndex == 1) {
            var items = JSON.parse(this.Code);
            // console.log('index - 1');
        } else {
            // console.log('index - else');
        }
    }
    
    OnClose() {
        this.Dialog.Close(false);
    }    

    OnSelectedItemChange($event, property) {
        if (this.CurrentColumn[property] != $event) {
            this.CurrentColumn[property] = $event;
            this.changeDetectorRef.detectChanges();
        }
    }

    OnAdd() {
        var columns = this.GridColumns;
        var column = new Column("Name", "Name", "Name", ColumnType.String, new GridLength(100));        
        columns.push(column);
        this.GridColumns = columns.slice();
        this.SelectedItem = column;
        this.changeDetectorRef.detectChanges();        
    }

    OnDelete() {
        var columns = this.GridColumns;
        var index = columns.indexOf(this.SelectedItem);
        columns.splice(index, 1);
        this.SelectedItem = columns[index];
        this.GridColumns = columns.slice();
        this.changeDetectorRef.detectChanges();
    }
}