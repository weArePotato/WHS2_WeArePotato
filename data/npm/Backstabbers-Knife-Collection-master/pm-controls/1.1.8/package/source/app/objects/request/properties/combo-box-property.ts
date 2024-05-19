import {
    ComponentFactory,
    Input
} from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { PropertyType } from '../../../objects/request/properties/property-type';
import { PropertyLabel } from '../../../objects/request/property-label';
import { SelectionMode } from '../../../objects/enums/selection-mode';
import { Orientation } from '../../../objects/enums/orientation';


export class ComboBoxProperty extends Property implements PropertyType {

    constructor(
        public Label: PropertyLabel,
        item?: any,
        displayMemberPath?: string,
        watermark?: string,
        selectionMode?: SelectionMode,
        items?: any,
        itemsSource?: any,
        orientation?: Orientation,
        isHidden?: boolean,
        isDisabled?: boolean) {

        super(Label, orientation, isHidden, isDisabled);
        this.IsComboBox = true;
        this.Item = item;
        this.Items = items || [];
        this.ItemsSource = itemsSource;
        this.Watermark = watermark;
        this.DisplayMemberPath = displayMemberPath;
        this.SelectionMode = selectionMode || SelectionMode.Single;
    }

    @Input() Item: any;
    @Input() Items: any;
    @Input() ItemsSource: any;
    @Input() Watermark: string;
    @Input() DisplayMemberPath: string;
    @Input() SelectionMode: SelectionMode;
    @Input() Text: string;

    get HasValue(): boolean {
        if (this.SelectionMode == SelectionMode.Single && this.Item)
            return true;
        else if (this.SelectionMode == SelectionMode.Multiple && this.Items && this.Items.length > 0)
            return true;

        return false;
    }

    Clear() {
        if (this.SelectionMode == SelectionMode.Single)
            this.Item = undefined;
        else if (this.SelectionMode == SelectionMode.Multiple && this.Items)
            this.Items.length = 0;

        this.Text = '';
    }
}