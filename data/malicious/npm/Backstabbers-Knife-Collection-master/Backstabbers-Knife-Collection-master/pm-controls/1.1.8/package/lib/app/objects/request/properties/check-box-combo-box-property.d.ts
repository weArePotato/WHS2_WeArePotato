import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';
export declare class CheckBoxComboBoxProperty extends Property implements PropertyType {
    Label: PropertyLabel;
    constructor(Label: PropertyLabel, items?: any, displayMemberPath?: string, watermark?: string, itemsSource?: any, orientation?: Orientation, isHidden?: boolean, isDisabled?: boolean);
    Items: any;
    ItemsSource: any;
    Watermark: string;
    DisplayMemberPath: string;
    readonly HasValue: boolean;
    Clear(): void;
}
