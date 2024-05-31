import { ElementRef } from '@angular/core';
export interface ResizeModel {
    resize(event: any, movingEle: ElementRef): any;
}
