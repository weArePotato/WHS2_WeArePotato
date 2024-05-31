import {
    Input
} from '@angular/core';

export class PropertyLabel {
    constructor(
        name?: string,
        label?: string,
        widthPx?: string,
        isRequired?: boolean) {

        this.Name = name;
        this.Label = label || this.Name;
        this.WidthPx = widthPx;
        this.IsRequired = isRequired;
    }

    @Input() Name: string;
    @Input() Label: string;
    @Input() WidthPx: string;
    @Input() IsRequired?: boolean;
}