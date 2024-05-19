import {
    ComponentFactory,
    Input
} from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';

export class MultiSelectTextBoxProperty extends Property implements PropertyType {

    constructor(
        public Label: PropertyLabel,
        item?: any,
        watermark?: any,
        items?: any,
        orientation?: Orientation,
        isHidden?: boolean,
        isDisabled?: boolean) {

        super(Label, orientation, isHidden, isDisabled);
        this.IsMultiSelectTextBox = true;        
        this.Item = item;
        this.Items = items || [];
    }

    @Input() Item: any;
    @Input() Items: any;
    @Input() Watermark: any;

    get HasValue(): boolean {
        if (this.Item)
            return true;
        return false;
    }

    Clear() {
        if (this.Item) {
            this.Item = undefined;
        }
    }
}