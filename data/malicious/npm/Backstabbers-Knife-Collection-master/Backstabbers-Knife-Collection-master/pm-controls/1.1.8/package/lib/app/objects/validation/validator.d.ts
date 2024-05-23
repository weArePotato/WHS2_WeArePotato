import { Property } from "../../objects/request/properties/property";
import { DatePickerProperty } from "../../objects/request/properties/date-picker-property";
import { DateRangePickerProperty } from "../../objects/request/properties/date-range-picker-property";
export declare class Validators {
    static IsRequired(property: Property): void;
    static IsMinMax(property: Property, min?: Number, max?: Number): void;
    static IsDateBeforeAfter(beforeProperty: DatePickerProperty, afterProperty: DatePickerProperty, format?: string): void;
    static IsDateRangeBeforeAfter(property: DateRangePickerProperty, format?: string): void;
}
