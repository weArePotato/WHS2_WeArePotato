import {    
    ChangeDetectorRef, 
    Component,
    Input,
    SimpleChanges
} from '@angular/core';
import { ClipboardService } from '../../../services/clipboard/clipboard-service';
import { GridComponent } from '../grid-component';
import { ModalDialog } from '../../modal/modal-dialog';
import { Dictionary } from '../../../../objects/dictionary';
import { Column } from '../../../../objects/request/column';
import { ColumnType } from '../../../../objects/request/column-type';
import { GridLength } from '../../../../objects/request/grid-length';
 
@Component({
    selector: 'pm-grid-settings-row-panel',
    //templateUrl: './app/controls/components/grid/grid-settings/grid-settings-row-panel.html',
    templateUrl: './grid-settings-row-panel.html'
})
export class GridSettingsRowPanelComponent  {
    constructor(
        private changeDetectorRef: ChangeDetectorRef, 
        private clipboard: ClipboardService) {
        changeDetectorRef.detach();
    }
    
    @Input() Grid: GridComponent;
    @Input() Dialog: ModalDialog;

    Data: any;

    ngOnChanges(changes: SimpleChanges) {
        if (changes['Grid']) {
            this.Data = JSON.stringify(this.Grid.ItemsSource, null, 4);
            this.changeDetectorRef.detectChanges();
        }
    }

    OnAutoGenerate() {
        var items = JSON.parse(this.Data);
        if (items && items.length > 0)
        {
            var columns = new Dictionary<Column>();

            var item = items[0];

            for (var key in item) {
                if (key.startsWith('_')) {
                    continue;
                }

                var type;
                var column = new Column(key, key, key, ColumnType.String, new GridLength(100));
                columns.add(column.Key, column);
            }

            this.Grid.Columns = columns;
            this.Grid.RefreshGrid();
        }
    }

    OnCopy() {
        this.clipboard.Copy(this.Data);
    }

    OnSave() {
        this.Grid.ItemsSource = JSON.parse(this.Data);
    }

    OnClose() {
        this.Dialog.Close(false);
    }
}