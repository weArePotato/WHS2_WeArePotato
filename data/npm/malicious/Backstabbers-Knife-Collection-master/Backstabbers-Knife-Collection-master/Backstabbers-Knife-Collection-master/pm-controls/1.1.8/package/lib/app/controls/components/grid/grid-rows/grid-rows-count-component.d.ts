import { ChangeDetectorRef, SimpleChanges } from '@angular/core';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
export declare class GridRowsCountComponent {
    private changeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    Rows: Array<any>;
    RowFocus: any;
    Grid: GridComponent;
    ngOnChanges(changes: SimpleChanges): void;
    IsRowFocused(row: any): any;
    OnCellSelect(row: any): void;
    OnRowResize(size: any, row: any): void;
}
