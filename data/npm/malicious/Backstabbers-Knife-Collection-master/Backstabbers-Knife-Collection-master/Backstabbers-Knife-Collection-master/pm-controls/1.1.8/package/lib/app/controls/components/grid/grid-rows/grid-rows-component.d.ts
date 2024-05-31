import { ChangeDetectorRef, SimpleChanges } from '@angular/core';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
export declare class GridRowsComponent {
    private changeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    Columns: Array<any>;
    Rows: Array<any>;
    SelectedCells: any;
    SelectedRows: any;
    IsFrozen: boolean;
    Grid: GridComponent;
    ngOnChanges(changes: SimpleChanges): void;
    readonly RowMouseOver: string;
}
