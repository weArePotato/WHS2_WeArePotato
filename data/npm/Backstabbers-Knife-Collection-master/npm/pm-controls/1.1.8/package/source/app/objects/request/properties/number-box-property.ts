import {
    ComponentFactory,
    Input
} from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';


export class NumericBoxProperty extends Property implements PropertyType {

    constructor(
        public Label: PropertyLabel,
        item?: number,
        minValue?: number,
        orientation?: Orientation,
        isHidden?: boolean,
        isDisabled?: boolean) {

        super(Label, orientation, isHidden, isDisabled);
        this.IsNumericBox = true;
        this.Item = item;
        this.MinValue = minValue;
    }

    @Input() Text: string;
    @Input() Item: number;
    @Input() MinValue: number;

    get HasValue(): boolean {
        return Number.isInteger(this.Item);
    }

    Clear() {
        if (this.Item) {
            this.Item = undefined;
        }

        this.Text = '';
    }
}