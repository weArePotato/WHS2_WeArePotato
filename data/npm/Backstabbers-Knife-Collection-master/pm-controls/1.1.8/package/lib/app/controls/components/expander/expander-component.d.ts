import { EventEmitter } from '@angular/core';
export declare class ExpanderComponent {
    ExpanderClass: string;
    CaretAlignment: string;
    IsExpanded: boolean;
    IsExpandedChange: EventEmitter<boolean>;
    readonly ExpanderHeaderClass: string;
    OnClick(): void;
}
