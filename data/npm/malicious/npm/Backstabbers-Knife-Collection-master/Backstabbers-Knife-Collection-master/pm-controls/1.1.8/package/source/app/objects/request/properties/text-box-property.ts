import {
    ComponentFactory,
    Input
} from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';

export class TextBoxProperty extends Property {

    constructor(
        public Label: PropertyLabel,
        item?: any,
        watermark?: any,
        orientation?: Orientation,
        isHidden?: boolean,
        isDisabled?: boolean) {
        
        super(Label, orientation, isHidden, isDisabled);
        this.IsTextBox = true;
        this.Item = item;
        this.Watermark = watermark;
    }

    @Input() Item: any;
    @Input() Watermark: any;

    get HasValue(): boolean {
        if (this.Item == null || this.Item == "")
            return false;
        return true;
    }

    Clear() {
        if (this.Item) {
            this.Item = undefined;
        }
    }
}