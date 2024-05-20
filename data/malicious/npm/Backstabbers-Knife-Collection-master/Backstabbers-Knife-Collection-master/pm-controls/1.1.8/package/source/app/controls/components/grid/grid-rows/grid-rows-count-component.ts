import { 
    Component,
    ChangeDetectorRef, 
    ChangeDetectionStrategy,
    Input,
    SimpleChanges,
    ViewContainerRef 
} from '@angular/core';
import { GridComponent } from '../../../../controls/components/grid/grid-component';

@Component({
    selector: 'pm-grid-rows-count',
    //templateUrl: './app/controls/components/grid/grid-rows-count.html',
    templateUrl: './grid-rows-count.html',
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class GridRowsCountComponent {
    constructor(private changeDetectorRef: ChangeDetectorRef) {
        changeDetectorRef.detach();
    }
   
    @Input() Rows: Array<any> = [];
    @Input() RowFocus;
    @Input() Grid: GridComponent;

    ngOnChanges(changes: SimpleChanges) {
        if (changes['Rows']) {
            this.changeDetectorRef.detectChanges();
        }

        if (changes['RowFocus']) {
            this.changeDetectorRef.detectChanges();
        }
    }

    IsRowFocused(row: any) {
        if (this.RowFocus) {
            return this.RowFocus[row['_rowNumber']];
        }
        return false;
    }

    OnCellSelect(row: any) {
        this.Grid.SelectRow(row);
    }

    OnRowResize(size: any, row: any) {
        if (size < 0)
            size = 0;
        row['_rowResizeHeight'] = size;
        this.Grid.ResizeRow(row);
    }
}