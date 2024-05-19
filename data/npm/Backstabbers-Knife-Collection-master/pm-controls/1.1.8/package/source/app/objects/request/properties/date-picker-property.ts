import {
    ComponentFactory,
    Input
} from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';

export class DatePickerProperty extends Property implements PropertyType {

    constructor(
        public Label: PropertyLabel,
        item?: any,
        watermark?: any,
        orientation?: Orientation,
        isHidden?: boolean,
        isDisabled?: boolean) {

        super(Label, orientation, isHidden, isDisabled);
        this.IsDatePicker = true;
        this.Item = item;
    }

    @Input() Item: any;
    @Input() Text: string;
    @Input() Watermark: any;

    get HasValue(): boolean {
        if (this.Item)
            return true;
        return false;
    }

    Clear() {
        this.Item = undefined;
        this.Text = '';
    }

    DefaultValidation() {
        if (!this.Item && this.Text)
        {
            this.Validation.Set("Invalid date format.");
        }
    }
}