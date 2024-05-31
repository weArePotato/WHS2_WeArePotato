import { Property } from '../../../objects/request/properties/property';
import { PropertyLabel } from '../../../objects/request/property-label';
import { RadioButtonItem } from '../../../objects/request/properties/radio-button-item';
import { Orientation } from '../../../objects/enums/orientation';
export declare class RadioGroupProperty extends Property {
    Label: PropertyLabel;
    constructor(Label: PropertyLabel, items?: Array<RadioButtonItem>, orientation?: Orientation, isHidden?: boolean, isDisabled?: boolean);
    Items: Array<RadioButtonItem>;
    private item;
    Item: any;
    readonly HasValue: boolean;
    Clear(): void;
}
