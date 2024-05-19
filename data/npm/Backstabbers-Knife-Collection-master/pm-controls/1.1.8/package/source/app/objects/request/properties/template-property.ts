import {
    ComponentFactory,
    Input
} from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';

export class TemplateProperty extends Property {

    constructor(
        public Label: PropertyLabel,
        item?: any,
        template?: any,        
        templateModules?: any,
        orientation?: Orientation,
        isHidden?: boolean,
        isDisabled?: boolean) {

        super(Label, orientation, isHidden, isDisabled);
        this.IsTemplate = true;
        this.Item = item;
        this.Template = template;
        this.TemplateModules = templateModules;
    }

    @Input() Item: any;
    @Input() Template: string;
    TemplateComponent: ComponentFactory<any>;
    public TemplateModules?: any[];

    get HasValue(): boolean {
        return true;
        // if (this.Item)
        //     return true;
        // return false;
    }
}