import {
    ComponentFactory,
    Input
} from '@angular/core';

export class RadioButtonItem {

    constructor(isChecked: boolean, label?: string, value?: string, isDisabled?: boolean) {
        this.IsChecked = isChecked;
        this.Label = label;
        this.Value = value || label;
        this.IsDisabled = isDisabled;
    }

    Label: string;
    Value: string;
    IsChecked: boolean;
    IsDisabled: boolean;    
}