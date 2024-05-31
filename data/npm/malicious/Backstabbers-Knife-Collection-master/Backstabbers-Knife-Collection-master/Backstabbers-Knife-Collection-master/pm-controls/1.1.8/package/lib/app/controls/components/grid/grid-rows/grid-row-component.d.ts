import { ChangeDetectorRef, Injector, SimpleChanges } from '@angular/core';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { Column } from '../../../../objects/request/column';
export declare class GridRowComponent {
    private changeDetectorRef;
    private injector;
    constructor(changeDetectorRef: ChangeDetectorRef, injector: Injector);
    Columns: Array<any>;
    Row: any;
    SelectedCells: any;
    SelectedRows: any;
    Grid: GridComponent;
    IsFrozen: boolean;
    ngOnChanges(changes: SimpleChanges): void;
    getProperty(column: Column): any;
    onCellSelect(column: any): void;
    hasHierarchy(column: any): boolean;
    isCellSelected(column: any): any;
    isRowSelected(): any;
    isRowHighlighted(): any;
    onToggleExpandCollapse(event: MouseEvent): void;
    CellAlignmentClass(column: Column): "cell-alignment-left" | "cell-alignment-right" | "cell-alignment-center";
    CellClass(column: Column): "" | "grid-table-row-cell";
    readonly RowSelectClass: string;
    readonly CellMouseOver: string;
}
