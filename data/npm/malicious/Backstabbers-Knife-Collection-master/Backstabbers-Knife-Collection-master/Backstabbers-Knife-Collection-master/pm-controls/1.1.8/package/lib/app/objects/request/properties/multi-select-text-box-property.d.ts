import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';
export declare class MultiSelectTextBoxProperty extends Property implements PropertyType {
    Label: PropertyLabel;
    constructor(Label: PropertyLabel, item?: any, watermark?: any, items?: any, orientation?: Orientation, isHidden?: boolean, isDisabled?: boolean);
    Item: any;
    Items: any;
    Watermark: any;
    readonly HasValue: boolean;
    Clear(): void;
}
