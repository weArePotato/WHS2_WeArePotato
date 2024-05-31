import { ChangeDetectorRef, SimpleChanges } from '@angular/core';
import { GridComponent } from '../../../../../controls/components/grid/grid-component';
import { ColumnGroup } from '../../../../../objects/request/column-group';
export declare class GridColumnGroupingComponent {
    private changeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    ColumnGroups: Array<any>;
    Grid: GridComponent;
    Row: any;
    ngOnChanges(changes: SimpleChanges): void;
    ColumnHeaderAlignmentClass(column: ColumnGroup): "column-alignment-left" | "column-alignment-right" | "column-alignment-center";
}
