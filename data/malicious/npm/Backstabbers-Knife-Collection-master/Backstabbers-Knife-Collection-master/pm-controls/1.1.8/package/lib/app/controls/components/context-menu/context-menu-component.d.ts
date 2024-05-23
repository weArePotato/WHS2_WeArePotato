import { ChangeDetectorRef, EventEmitter, ViewContainerRef } from '@angular/core';
export declare class ContextMenuComponent {
    private changeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef, viewContainerRef: ViewContainerRef);
    ContextMenuTemplate: any;
    ContextMenuContainerElement: any;
    private el;
    private isOpen;
    private clickEvent;
    IsOpen: boolean;
    Top: any;
    Left: any;
    DataContext: any;
    Open: EventEmitter<boolean>;
    Show(left: number, top: number): void;
    HandleClick(e: any): void;
}
