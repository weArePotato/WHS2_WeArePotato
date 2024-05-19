import { ViewContainerRef, TemplateRef, ElementRef, Renderer, EmbeddedViewRef, NgZone, ChangeDetectorRef } from '@angular/core';
export declare class VsForPanel {
    private _element;
    private _viewContainer;
    private _templateRef;
    private _renderer;
    private _ngZone;
    private _changeDetectorRef;
    private static readonly MAX_SCROLL_SIZE;
    originalLength: number;
    view: EmbeddedViewRef<any>;
    parent: HTMLElement;
    tagName: string;
    autoSize: boolean;
    scrollParent: HTMLElement;
    clientSizeProp: string;
    offsetSizeProp: string;
    scrollPosProp: string;
    layoutProp: string;
    numOfScreenElements: number;
    totalSize: number;
    scrollSize: number;
    numberOfPages: number;
    pageSize: number;
    pageCoefficient: number;
    elementSize: number;
    currentPage: number;
    previousScrollTop: number;
    currentPageOffset: number;
    sizes: number[];
    startIndex: number;
    endIndex: number;
    private _prevStartIndex;
    private _prevEndIndex;
    onWindowResize: any;
    onZone: any;
    private _originalCollection;
    originalCollection: any[];
    private _slicedCollection;
    slicedCollection: any[];
    constructor(_element: ElementRef, _viewContainer: ViewContainerRef, _templateRef: TemplateRef<any>, _renderer: Renderer, _ngZone: NgZone, _changeDetectorRef: ChangeDetectorRef);
    onChanges(): void;
    postDigest(fn: any): void;
    init(scrollParentClass: string, itemHeight?: number): void;
    destroy(): void;
    refresh(): void;
    updateTotalSize(size: number): void;
    reinitialize(): void;
    updateInnerCollection(): boolean;
    moveItemIntoView(item: any): void;
    moveItemToTop(index: number): void;
    moveItemToBottom(index: number): void;
    pageForward(curScrollTop: number): void;
    pageBack(curScrollTop: number): void;
    onScroll(viewportSize: number): number;
    onSmallScroll(scrollTop: number): number;
    getWindowScroll(): {
        scrollTop: any;
        scrollLeft: any;
    };
    getViewportSize(element: Node | Window, sizeProp: string): number;
    getScrollPos(element: Node | Window, scrollProp: string): number;
    getScrollOffset(vsElement: HTMLElement, scrollElement: HTMLElement | Window): number;
    nextElementSibling(el: any): any;
    onBigScroll(scrollTop: number, viewportSize: number): number;
    calcTopNum(index: number): number;
    calcTop(index: number): string;
    getScrollBottom(): number;
    getScrollSize(): number;
    getPageSize(): number;
    getNumberOfPages(): number;
    getPageCoefficient(): number;
    private getOffset(index);
    dde: any;
    matchingFunction: string;
    closestElement(el: Node, selector: string): HTMLElement;
}
