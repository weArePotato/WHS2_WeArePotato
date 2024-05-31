import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';
export declare class DateTimePickerProperty extends Property implements PropertyType {
    Label: PropertyLabel;
    constructor(Label: PropertyLabel, item?: any, watermark?: any, orientation?: Orientation, isHidden?: boolean, isDisabled?: boolean);
    Text: string;
    Item: any;
    Watermark: any;
    readonly HasValue: boolean;
    Clear(): void;
    DefaultValidation(): void;
}
