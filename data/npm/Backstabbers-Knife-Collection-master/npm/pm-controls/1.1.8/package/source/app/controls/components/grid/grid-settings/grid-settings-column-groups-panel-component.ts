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
import { ColumnGroup } from '../../../../objects/request/column-group';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { Dictionary } from '../../../../objects/dictionary';
import { Column } from '../../../../objects/request/column';
import { GridLength } from '../../../../objects/request/grid-length';

@Component({
    selector: 'pm-grid-settings-column-groups-panel',
    //templateUrl: './app/controls/components/grid/grid-settings/grid-settings-column-panel.html',
    templateUrl: './grid-settings-column-groups-panel.html',
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class GridSettingsColumnGroupsPanelComponent {
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
    @Input() GridColumnGroups: ColumnGroup[];

    private grid: GridComponent;
    @Input('Grid')
    get Grid(): GridComponent {
        return this.grid;
    }

    set Grid(value: GridComponent) {
        this.grid = value;
        this.GridColumnGroups = this.grid.ColumnGroups ? this.grid.ColumnGroups.Values : [];
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

    get Columns() {
        return new Dictionary<Column>([
            { key: "Name", value: new Column("Name", "Name", "Name", ColumnType.String, new GridLength(140)) },
            { key: "Header", value: new Column("Header", "Header", "Header", ColumnType.String, new GridLength(100)) },
        ]);
    }

    ngOnChanges(changes: SimpleChanges) {
        if (changes['Grid']) {
            var columnGroups = "";
            if (this.Grid.ColumnGroups) {
                for (var i = 0; i < this.Grid.ColumnGroups.Values.length; i++) {
                    var columnGroup = this.Grid.ColumnGroups.Values[i];                    
                    columnGroups += "{ key: \"" + columnGroup.Name + "\", value: new ColumnGroup(\"" + columnGroup.Name + "\", \"" + columnGroup.Header + ")) },\r\n";
                }
            }
            this.Code = columnGroups;
            this.changeDetectorRef.detectChanges();
        }
    }

    OnCopy() {
        this.clipboard.Copy(this.Code);
    }

    OnSave() {
        if (this.SelectedTabIndex == 0) {
            var columnGroups = this.GridColumnGroups;
            var index = columnGroups.indexOf(this.SelectedItem);
            columnGroups[index] = this.CurrentColumn;
            var toDictionary = [];
            for (var i = 0; i < columnGroups.length; i++) {
                var columnGroup = columnGroups[i];
                toDictionary.push({ key: columnGroup.Name, value: columnGroup });
            }

            this.Grid.ColumnGroups = new Dictionary<ColumnGroup>(toDictionary);
            this.GridColumnGroups = columnGroups.slice();
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
        var columnGroups = this.GridColumnGroups;
        var columnGroup = new ColumnGroup("Name", "Name");
        columnGroups.push(columnGroup);
        this.GridColumnGroups = columnGroups.slice();
        this.SelectedItem = columnGroup;
        this.changeDetectorRef.detectChanges();
    }

    OnDelete() {
        var columns = this.GridColumnGroups;
        var index = columns.indexOf(this.SelectedItem);
        columns.splice(index, 1);
        this.SelectedItem = columns[index];
        this.GridColumnGroups = columns.slice();
        this.changeDetectorRef.detectChanges();
    }
}