import { ElementRef, EventEmitter } from '@angular/core';
export declare class TextBoxComponent {
    Text: string;
    Watermark: string;
    TextBoxClass: string;
    Width: string;
    MaxWidth: string;
    IsDisabled: boolean;
    IsReadOnly: boolean;
    TextChange: EventEmitter<string>;
    BlurChange: EventEmitter<any>;
    FocusChange: EventEmitter<any>;
    KeyUp: EventEmitter<any>;
    KeyDown: EventEmitter<any>;
    textBox: ElementRef;
    constructor();
    onChange(newValue: any): void;
    onBlur(value: any): void;
    onFocus(value: any): void;
    onKeyUp(event: any): void;
    onKeyDown(event: any): void;
    Focus(): void;
}
