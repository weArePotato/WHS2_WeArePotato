import { ComponentFactory } from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';
export declare class TemplateProperty extends Property {
    Label: PropertyLabel;
    constructor(Label: PropertyLabel, item?: any, template?: any, templateModules?: any, orientation?: Orientation, isHidden?: boolean, isDisabled?: boolean);
    Item: any;
    Template: string;
    TemplateComponent: ComponentFactory<any>;
    TemplateModules?: any[];
    readonly HasValue: boolean;
}
