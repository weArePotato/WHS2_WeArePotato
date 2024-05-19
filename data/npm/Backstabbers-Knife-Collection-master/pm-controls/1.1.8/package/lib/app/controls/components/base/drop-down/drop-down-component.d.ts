import { ChangeDetectorRef, OnDestroy, OnInit, ElementRef, ViewContainerRef } from '@angular/core';
import { CompatibilityService } from '../../../services/compatibility/compatibility-service';
export declare class DropDownComponent implements OnInit, OnDestroy {
    changeDetectorRef: ChangeDetectorRef;
    viewContainerRef: ViewContainerRef;
    CompatibilityService: CompatibilityService;
    constructor(changeDetectorRef: ChangeDetectorRef, viewContainerRef: ViewContainerRef, CompatibilityService: CompatibilityService);
    ngOnInit(): void;
    ngDoCheck(): void;
    ngOnDestroy(): void;
    private el;
    private scrollEvent;
    private clickEvent;
    private resizeEvent;
    Width: string;
    MaxWidth: string;
    MinWidth: string;
    ContainerWidth: number;
    ContainerTop: number;
    HorizontalAlignment: string;
    Padding: string;
    DropDownPane: ElementRef;
    private isDropDownOpen;
    IsDropDownOpen: boolean;
    HandleScroll(e: any): void;
    HandleClick(e: any): void;
    HandleResize(): void;
}
