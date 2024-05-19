import {
    ComponentFactory,
    Input
} from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';


export class CheckBoxComboBoxProperty extends Property implements PropertyType {
    
    constructor(
        public Label: PropertyLabel,
        items?: any,
        displayMemberPath?: string,
        watermark?: string,
        itemsSource?: any,
        orientation?: Orientation,
        isHidden?: boolean,
        isDisabled?: boolean) {

        super(Label, orientation, isHidden, isDisabled);

        this.IsCheckBoxComboBox = true;
        this.Items = items;
        this.ItemsSource = itemsSource;
        this.Watermark = watermark;
        this.DisplayMemberPath = displayMemberPath;
    }
    
    @Input() Items: any;
    @Input() ItemsSource: any;
    @Input() Watermark: string;
    @Input() DisplayMemberPath: string;

    get HasValue(): boolean {
        if (this.Items && this.Items.length > 0)
            return true;

        return false;
    }

    Clear() {
        if (this.Items)
            this.Items.length = 0;        
    }
}