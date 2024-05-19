import {
    ComponentFactory,
    Input
} from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { DateRange } from '../../../objects/date-range';
import { Orientation } from '../../../objects/enums/orientation';


export class DateRangePickerProperty extends Property implements PropertyType {

    constructor(
        public Label: PropertyLabel,
        item?: DateRange,
        watermark?: string, 
        orientation?: Orientation,
        isHidden?: boolean,
        isDisabled?: boolean) {

        super(Label, orientation, isHidden, isDisabled);
        this.IsDateRangePicker = true;
        this.Item = item || new DateRange();
        this.Watermark = watermark;
    }

    @Input() Item: DateRange; 
    @Input() Watermark: string;

    get HasValue(): boolean {
        if (this.Item && this.Item.Start && this.Item.Finish)
            return true;
        return false;
    }

    Clear() {
        if (this.Item) {
            this.Item.Start = undefined;
            this.Item.Finish = undefined;

            this.Item.StartText = '';
            this.Item.FinishText = '';
        }
    }

    DefaultValidation() {
        if (this.Item) {
            if (!this.Item.Start && this.Item.StartText)
            {
                this.Validation.Set("Invalid date format.");
            }

            if (!this.Item.Finish && this.Item.FinishText)
            {
                this.Validation.Set("Invalid date format.");
            }
        }
    }
}