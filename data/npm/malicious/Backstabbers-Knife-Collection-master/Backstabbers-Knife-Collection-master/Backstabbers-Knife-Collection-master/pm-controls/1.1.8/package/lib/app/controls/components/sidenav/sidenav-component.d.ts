import { OnInit, OnDestroy, ChangeDetectorRef, ViewContainerRef } from '@angular/core';
export declare class SidenavComponent implements OnInit, OnDestroy {
    changeDetectorRef: ChangeDetectorRef;
    viewContainerRef: ViewContainerRef;
    constructor(changeDetectorRef: ChangeDetectorRef, viewContainerRef: ViewContainerRef);
    private el;
    private clickEvent;
    ngOnInit(): void;
    private isSidenavOpen;
    IsSidenavOpen: boolean;
    ToggleSidenav(): void;
    HandleClick(e: any): void;
    ngOnDestroy(): void;
}
