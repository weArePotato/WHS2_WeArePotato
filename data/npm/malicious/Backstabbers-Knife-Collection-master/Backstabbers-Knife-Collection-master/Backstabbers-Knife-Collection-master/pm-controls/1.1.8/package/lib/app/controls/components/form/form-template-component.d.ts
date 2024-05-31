import { ChangeDetectorRef, ViewContainerRef } from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
export declare class FormTemplateComponent {
    private changeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    Property: Property;
    viewContainer: ViewContainerRef;
    ngOnInit(): void;
}
