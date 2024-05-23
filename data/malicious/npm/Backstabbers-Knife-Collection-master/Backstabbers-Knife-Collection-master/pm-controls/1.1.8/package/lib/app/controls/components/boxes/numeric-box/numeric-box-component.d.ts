import { OnInit, EventEmitter, ChangeDetectorRef } from '@angular/core';
export declare class NumericBoxComponent implements OnInit {
    changeDetectorRef: ChangeDetectorRef;
    Value: number;
    IsDisabled: boolean;
    ValueChange: EventEmitter<any>;
    Watermark: string;
    MaxValue: number;
    MinValue: number;
    TextChange: EventEmitter<string>;
    constructor(changeDetectorRef: ChangeDetectorRef);
    ngOnInit(): void;
    onKeyPress(e: KeyboardEvent): void;
    onPaste(e: ClipboardEvent): boolean;
    incrementUp(): void;
    incrementDown(): void;
    onTextChange(newValue: any): void;
    SetValue(newValue: any): void;
    private text;
    Text: string;
}
