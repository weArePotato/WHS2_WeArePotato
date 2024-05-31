import { EventEmitter, ElementRef } from '@angular/core';
export declare class SliderComponent {
    constructor();
    moveEvent: any;
    dragendEvent: any;
    dragging: boolean;
    DragStart: EventEmitter<any>;
    DragEnd: EventEmitter<any>;
    sliderthumb: ElementRef;
    slidercontainer: ElementRef;
    dragstart(event: any): void;
    dragend(event: any): void;
    getOffsetLeft(elem: any): number;
    move(event: any): void;
}
