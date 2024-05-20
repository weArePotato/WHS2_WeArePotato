import { EventEmitter } from '@angular/core';
import 'rxjs/add/observable/fromEvent';
import { Subscription } from 'rxjs/Subscription';
export declare class ModalDialog {
    KeyPress: Subscription;
    ShowModal: boolean;
    Header: string;
    CanResize: boolean;
    OnClosed: EventEmitter<boolean>;
    Close(result: boolean): void;
    Initialize(): void;
    Destroy(): void;
}
