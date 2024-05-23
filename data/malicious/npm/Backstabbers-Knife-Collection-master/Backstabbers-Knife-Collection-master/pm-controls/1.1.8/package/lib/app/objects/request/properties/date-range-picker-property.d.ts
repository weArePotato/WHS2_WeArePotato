import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { DateRange } from '../../../objects/date-range';
import { Orientation } from '../../../objects/enums/orientation';
export declare class DateRangePickerProperty extends Property implements PropertyType {
    Label: PropertyLabel;
    constructor(Label: PropertyLabel, item?: DateRange, watermark?: string, orientation?: Orientation, isHidden?: boolean, isDisabled?: boolean);
    Item: DateRange;
    Watermark: string;
    readonly HasValue: boolean;
    Clear(): void;
    DefaultValidation(): void;
}
