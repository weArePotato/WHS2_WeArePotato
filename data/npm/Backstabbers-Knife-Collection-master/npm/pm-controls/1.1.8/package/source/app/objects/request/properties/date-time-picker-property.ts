import {
    ComponentFactory,
    Input
} from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';

export class DateTimePickerProperty extends Property implements PropertyType {

    constructor(
        public Label: PropertyLabel,
        item?: any,
        watermark?: any,
        orientation?: Orientation,
        isHidden?: boolean,
        isDisabled?: boolean) {

        super(Label, orientation, isHidden, isDisabled);
        this.IsDateTimePicker = true;        
        this.Item = item;
    }

    @Input() Text: string;
    @Input() Item: any;
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
        this.Text = '';
    }

    DefaultValidation() {
        if (!this.Item && this.Text)
        {
            this.Validation.Set("Invalid date format.");
        }
    }
}