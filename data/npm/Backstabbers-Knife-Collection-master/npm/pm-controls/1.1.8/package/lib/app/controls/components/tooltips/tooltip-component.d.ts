import { ElementRef, ChangeDetectorRef } from '@angular/core';
export declare class TooltipComponent {
    changeDetectorRef: ChangeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    DEFAULT_TOOLTIP_WIDTH: number;
    private targetWidth;
    Top: any;
    Left: any;
    DataContext: any;
    Content: string;
    EnableTooltip: boolean;
    Delay: number;
    Duration: number;
    TooltipBorder: ElementRef;
    TooltipText: ElementRef;
    ShowTooltip: boolean;
    private width;
    Width: any;
    Show(left: number, top: number): void;
    Hide(): void;
}
