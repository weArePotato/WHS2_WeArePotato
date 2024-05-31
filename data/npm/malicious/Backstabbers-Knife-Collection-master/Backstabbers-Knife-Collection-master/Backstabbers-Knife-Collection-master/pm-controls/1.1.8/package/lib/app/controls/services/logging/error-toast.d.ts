import { ChangeDetectorRef } from '@angular/core';
import { Toast } from '../../../controls/components/toast/toast';
export declare class ErrorToast extends Toast {
    changeDetectorRef: ChangeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    Name: string;
    Message: string;
    Stack: string;
    CopyToClipBoard(e: MouseEvent): void;
    RaiseChange(): void;
}
