import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { SelectionMode } from '../../../objects/enums/selection-mode';
import { Orientation } from '../../../objects/enums/orientation';
export declare class ComboBoxProperty extends Property implements PropertyType {
    Label: PropertyLabel;
    constructor(Label: PropertyLabel, item?: any, displayMemberPath?: string, watermark?: string, selectionMode?: SelectionMode, items?: any, itemsSource?: any, orientation?: Orientation, isHidden?: boolean, isDisabled?: boolean);
    Item: any;
    Items: any;
    ItemsSource: any;
    Watermark: string;
    DisplayMemberPath: string;
    SelectionMode: SelectionMode;
    Text: string;
    readonly HasValue: boolean;
    Clear(): void;
}
