import { ChangeDetectorRef, EventEmitter } from '@angular/core';
export declare class CheckBoxComponent {
    changeDetectorRef: ChangeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    Label: any;
    CheckBoxTheme: string;
    IsAnimated: boolean;
    IsReadOnly: boolean;
    IsChecked: boolean;
    IsDisabled: boolean;
    IsCheckedChange: EventEmitter<any>;
    CheckBoxStateClass: string;
    OnClick(): void;
    readonly CheckBoxClass: string;
}
