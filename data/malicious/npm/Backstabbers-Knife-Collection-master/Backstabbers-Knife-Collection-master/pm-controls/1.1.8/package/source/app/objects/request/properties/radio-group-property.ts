import {
    ComponentFactory,
    Input
} from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { PropertyLabel } from '../../../objects/request/property-label';
import { RadioButtonItem } from '../../../objects/request/properties/radio-button-item';
import { Orientation } from '../../../objects/enums/orientation';

export class RadioGroupProperty extends Property {

    constructor(
        public Label: PropertyLabel,
        items?: Array<RadioButtonItem>,
        orientation?: Orientation,
        isHidden?: boolean,
        isDisabled?: boolean) {

        super(Label, orientation, isHidden, isDisabled);
        this.IsRadioGroup = true;
        this.Items = items;
    }

    @Input() Items: Array<RadioButtonItem>;

    private item: any;
    @Input('Item')
    get Item(): any {        
        return this.item;
    }
  
    set Item(value: any) {
        this.item = value;

        for (var i=0; i<this.Items.length; i++) {
            var item = this.Items[i];
            item.IsChecked = this.item == item.Value;
        }
    }

    get HasValue(): boolean {
        return true;
    }

    Clear() {        
        // if (this.Item) {
        //     this.Item = undefined;
        // }
    }
}