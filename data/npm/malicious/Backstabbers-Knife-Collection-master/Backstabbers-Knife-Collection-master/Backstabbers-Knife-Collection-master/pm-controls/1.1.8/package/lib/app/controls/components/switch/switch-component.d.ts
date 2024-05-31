import { ChangeDetectorRef, EventEmitter } from '@angular/core';
export declare class SwitchComponent {
    changeDetectorRef: ChangeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    ngOnInit(): void;
    IsDisabled: boolean;
    IsCheckedChange: EventEmitter<any>;
    SwitchTheme: string;
    SwitchButtonClass: string;
    SwitchBarClass: string;
    OnClick(): void;
    OnSetState(): void;
    private isChecked;
    IsChecked: boolean;
}
