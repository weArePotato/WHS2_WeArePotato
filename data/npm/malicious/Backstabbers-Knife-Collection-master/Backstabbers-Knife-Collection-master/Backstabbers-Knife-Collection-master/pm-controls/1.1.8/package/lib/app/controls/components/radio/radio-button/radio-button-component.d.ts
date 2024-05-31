import { ChangeDetectorRef, EventEmitter } from '@angular/core';
export declare class RadioButtonComponent {
    changeDetectorRef: ChangeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    ngOnInit(): void;
    IsDisabled: boolean;
    Label: string;
    Value: any;
    RadioGroup: any;
    RadioGroupChange: EventEmitter<any>;
    RadioButtonOuterTheme: string;
    RadioButtonInnerTheme: string;
    OnClick(): void;
    readonly OuterClass: string;
    readonly InnerClass: string;
    private isChecked;
    IsChecked: boolean;
}
