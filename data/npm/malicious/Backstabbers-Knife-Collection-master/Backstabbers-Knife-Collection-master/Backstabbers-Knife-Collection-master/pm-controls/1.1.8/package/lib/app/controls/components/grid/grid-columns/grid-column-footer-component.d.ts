import { ChangeDetectorRef, SimpleChanges } from '@angular/core';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { Column } from '../../../../objects/request/column';
export declare class GridColumnFooterComponent {
    private changeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    Columns: Array<any>;
    Grid: GridComponent;
    Row: any;
    ngOnChanges(changes: SimpleChanges): void;
    private static GetPropertyByPath(path, row);
    getAggregate(column: Column): number;
    GridColumnFooterClass(column: Column): "" | "grid-table-column-cell";
}
