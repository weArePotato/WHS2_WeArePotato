import { ElementRef } from '@angular/core';
export declare class SidebarComponent extends ElementRef {
    private element;
    constructor(element: ElementRef);
    ngDoCheck(): void;
    Header: string;
    RibbonHeader: string;
    IsCollapsed: boolean;
    FlexBasisPx: number;
    MinWidthPx: number;
    PreviousFlexBasis: any;
    OnToggleHeader(): void;
}
