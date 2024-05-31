import { EventEmitter, OnDestroy, OnInit, ViewContainerRef } from '@angular/core';
export declare class MenuDropDownButtonComponent implements OnInit, OnDestroy {
    IsDropDownOpen: boolean;
    IsDisabled: boolean;
    HorizontalAlignment: string;
    ButtonClass: string;
    ContainerClass: string;
    DropDownClass: string;
    OpenDropDownOnHover: boolean;
    IsDropDownOpenChange: EventEmitter<boolean>;
    private el;
    private clickEvent;
    constructor(viewContainerRef: ViewContainerRef);
    ngOnInit(): void;
    ngOnDestroy(): void;
    HandleClick(e: any): void;
    click(): void;
    mouseenter(): void;
    mouseleave(): void;
}
