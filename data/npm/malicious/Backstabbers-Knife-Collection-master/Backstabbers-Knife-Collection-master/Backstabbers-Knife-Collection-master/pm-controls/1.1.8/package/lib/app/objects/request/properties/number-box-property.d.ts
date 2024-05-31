import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';
export declare class NumericBoxProperty extends Property implements PropertyType {
    Label: PropertyLabel;
    constructor(Label: PropertyLabel, item?: number, minValue?: number, orientation?: Orientation, isHidden?: boolean, isDisabled?: boolean);
    Text: string;
    Item: number;
    MinValue: number;
    readonly HasValue: boolean;
    Clear(): void;
}
