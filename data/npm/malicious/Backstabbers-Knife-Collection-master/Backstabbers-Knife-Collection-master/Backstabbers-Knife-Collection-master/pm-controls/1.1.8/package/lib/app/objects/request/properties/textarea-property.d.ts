import { Property } from '../../../objects/request/properties/property';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';
export declare class TextareaProperty extends Property {
    Label: PropertyLabel;
    constructor(Label: PropertyLabel, item?: any, watermark?: any, orientation?: Orientation, isHidden?: boolean, isDisabled?: boolean);
    Item: any;
    Watermark: any;
    readonly HasValue: boolean;
    Clear(): void;
}
