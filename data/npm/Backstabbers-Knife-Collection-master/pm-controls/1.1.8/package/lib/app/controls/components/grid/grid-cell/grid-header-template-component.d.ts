import { ChangeDetectorRef, ViewContainerRef } from '@angular/core';
import { Column } from '../../../../objects/request/column';
export declare class GridHeaderTemplateComponent {
    private changeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    Column: Column;
    viewContainer: ViewContainerRef;
    ngOnInit(): void;
}
