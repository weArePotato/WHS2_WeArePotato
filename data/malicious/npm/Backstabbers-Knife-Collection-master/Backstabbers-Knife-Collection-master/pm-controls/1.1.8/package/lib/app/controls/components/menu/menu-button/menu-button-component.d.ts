import { EventEmitter, OnInit, OnDestroy, ViewContainerRef } from '@angular/core';
export declare class MenuButtonComponent implements OnInit, OnDestroy {
    IsDropDownOpen: boolean;
    IsDisabled: boolean;
    HorizontalAlignment: string;
    ButtonClass: string;
    DropDownClass: string;
    IsDropDownOpenChange: EventEmitter<boolean>;
    private el;
    private clickEvent;
    constructor(viewContainerRef: ViewContainerRef);
    ngOnInit(): void;
    ngOnDestroy(): void;
    HandleClick(e: any): void;
    click(): void;
}
