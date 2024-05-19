import { ChangeDetectorRef, ViewContainerRef } from '@angular/core';
import { Column } from '../../../../objects/request/column';
export declare class GridCellTemplateComponent {
    private changeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    Column: Column;
    Row: any;
    viewContainer: ViewContainerRef;
    ngOnInit(): void;
}
