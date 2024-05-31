import { ElementRef } from '@angular/core';
import { ResizeModel } from './resize-model';
export declare class FlexGrowResizeModel implements ResizeModel {
    FirstElements: Array<HTMLElement>;
    SecondElements: Array<HTMLElement>;
    IsHorizontal: boolean;
    constructor(FirstElements: Array<HTMLElement>, SecondElements: Array<HTMLElement>, IsHorizontal: boolean);
    resize(event: any, movingEle: ElementRef): any;
    private getMouseMovement(event, movingEle);
}
