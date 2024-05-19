import { ElementRef } from '@angular/core';

export interface ResizeModel {
    resize(event, movingEle: ElementRef) : any;
}