import { EventEmitter } from '@angular/core';
export declare class ToastComponent {
    ShowToast: boolean;
    OnClosed: EventEmitter<boolean>;
    Bottom: string;
    Left: string;
    Position: string;
    Height: string | number;
    Width: string | number;
    Top: string;
    Right: string;
    Show(): void;
    Close(result: boolean): void;
}
