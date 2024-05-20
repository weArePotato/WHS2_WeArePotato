import { ElementRef } from '@angular/core';
import { ResizeModel } from './resize-model';
export declare class FlexBasisResizeModel implements ResizeModel {
    IsPrevious: boolean;
    IsHorizontal: boolean;
    constructor(element: any, IsPrevious: boolean, IsHorizontal: boolean);
    Element: any;
    resize(event: any, movingEle: ElementRef): any;
    private getMouseMovement(event, movingEle);
}
