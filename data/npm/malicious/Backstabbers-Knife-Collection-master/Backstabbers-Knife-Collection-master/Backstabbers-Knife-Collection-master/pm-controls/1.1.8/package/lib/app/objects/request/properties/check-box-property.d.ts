import { Property } from '../../../objects/request/properties/property';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';
export declare class CheckBoxProperty extends Property {
    Label: PropertyLabel;
    constructor(Label: PropertyLabel, item?: boolean, display?: string, orientation?: Orientation, isHidden?: boolean, isDisabled?: boolean);
    Item: boolean;
    Display: string;
    readonly HasValue: boolean;
    Clear(): void;
}
