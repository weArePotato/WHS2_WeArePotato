import { OnDestroy, ViewContainerRef, TemplateRef, ElementRef, Renderer, NgZone, ChangeDetectorRef } from '@angular/core';
import { VsForPanel } from './vs-for-panel';
export declare class VsFor implements OnDestroy {
    private _element;
    private _viewContainer;
    private _templateRef;
    private _renderer;
    private _ngZone;
    private _changeDetectorRef;
    private static readonly MAX_SCROLL_SIZE;
    private itemHeight;
    ItemHeight: any;
    vsForPanel: VsForPanel;
    virtualVsForPanel: VsForPanel;
    scrollParent: HTMLElement;
    vsScrollParent: string;
    private _originalCollection;
    originalCollection: any[];
    constructor(_element: ElementRef, _viewContainer: ViewContainerRef, _templateRef: TemplateRef<any>, _renderer: Renderer, _ngZone: NgZone, _changeDetectorRef: ChangeDetectorRef);
    ngOnChanges(): void;
    ngOnInit(): void;
    ngOnDestroy(): void;
    moveItemIntoView(item: any): void;
    moveItemToTop(item: any): void;
    moveItemToBottom(item: any): void;
    calcTop(index: number): string;
}
