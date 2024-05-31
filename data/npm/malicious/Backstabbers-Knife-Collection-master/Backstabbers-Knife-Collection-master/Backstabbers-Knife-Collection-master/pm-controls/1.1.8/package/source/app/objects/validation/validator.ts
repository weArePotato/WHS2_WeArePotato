import { Property } from "../../objects/request/properties/property";
import { PropertyType } from "../../objects/request/properties/property-type";
import { NumericBoxProperty } from "../../objects/request/properties/number-box-property";
import { DatePickerProperty } from "../../objects/request/properties/date-picker-property";
import { DateExtensions } from "../../objects/extensions/date-extensions";
import { DateRangePickerProperty } from "../../objects/request/properties/date-range-picker-property";



export class Validators {
    
    public static IsRequired(property: Property)
    {
        var type = <PropertyType><any>property;
        if (type.HasValue == false) {
            property.Validation.Set("* Required");
            return;
        }
    }

    public static IsMinMax(property: Property, min?: Number, max?: Number) 
    {
        var number = (<NumericBoxProperty>property).Item;
        if (Number.isInteger(number))
        {
            if (min && max && number < min || number > max)
                property.Validation.Set(property.Label.Name + " must be between " + min + " and " + max + ".");
            else if (min && number < min)
                property.Validation.Set(property.Label.Name + " must be greater than or equal to " + min + ".");
            else if (max && number > max)
                property.Validation.Set(property.Label.Name + " must be less than or equal to " + max + ".");
        }
    }

    public static IsDateBeforeAfter(beforeProperty: DatePickerProperty, afterProperty: DatePickerProperty, format?: string) {
        
        var before = DateExtensions.GetDate(beforeProperty.Item, format);
        var after = DateExtensions.GetDate(afterProperty.Item, format);

        if (before && after && before > after)
            beforeProperty.Validation.Set("The " + afterProperty.Label.Name + " cannot be before the " + beforeProperty.Label.Name + ".");
    }

    public static IsDateRangeBeforeAfter(property: DateRangePickerProperty, format?: string) {

        var before = DateExtensions.GetDate(property.Item.Start, format);
        var after = DateExtensions.GetDate(property.Item.Finish, format);

        if (before && after && before > after)
            property.Validation.Set("The finish date cannot be before the start date.");
    }
}
