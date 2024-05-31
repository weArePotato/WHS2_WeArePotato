import { EventEmitter } from '@angular/core';
export declare class ButtonComponent {
    Click: EventEmitter<{}>;
    IsDisabled: boolean;
    ButtonClass: string;
    OnClick(): void;
}
