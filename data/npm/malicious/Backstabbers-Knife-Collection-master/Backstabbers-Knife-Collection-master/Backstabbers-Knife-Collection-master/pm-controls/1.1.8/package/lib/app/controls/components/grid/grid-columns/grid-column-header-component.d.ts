import { ChangeDetectorRef, SimpleChanges } from '@angular/core';
import { DialogService } from '../../../../controls/services/dialog/dialog-service';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { Column } from '../../../../objects/request/column';
export declare class GridColumnHeaderComponent {
    private dialog;
    private changeDetectorRef;
    constructor(dialog: DialogService, changeDetectorRef: ChangeDetectorRef);
    Columns: Array<any>;
    Grid: GridComponent;
    Row: any;
    ColumnFocus: any;
    ngOnChanges(changes: SimpleChanges): void;
    ColumnHeaderAlignmentClass(column: Column): "column-alignment-left" | "column-alignment-right" | "column-alignment-center";
    isColumnSelected(column: any): any;
    OnColumnHeaderClick(event: MouseEvent, column: Column): void;
    OnColumnResize(size: any, column: Column): void;
    OnColumnFilterOpen(event: MouseEvent, column: Column): void;
    ColumnSortDirection(column: Column): any;
    GridColumnHeaderClass(column: Column): "" | "grid-table-column-cell";
}
