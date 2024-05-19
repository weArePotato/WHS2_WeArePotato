import {
    ComponentFactory,
    Input
} from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';

export class CheckBoxProperty extends Property {

    constructor(
        public Label: PropertyLabel,
        item?: boolean,
        display?: string,
        orientation?: Orientation,
        isHidden?: boolean,
        isDisabled?: boolean) {

        super(Label, orientation, isHidden, isDisabled);
        this.IsCheckBox = true;
        this.Item = item;
        this.Display = display;
    }

    @Input() Item: boolean;
    @Input() Display: string;

    get HasValue(): boolean {
        return true;
    }

    Clear() {
        if (this.Item)
            this.Item = false;
    }
}