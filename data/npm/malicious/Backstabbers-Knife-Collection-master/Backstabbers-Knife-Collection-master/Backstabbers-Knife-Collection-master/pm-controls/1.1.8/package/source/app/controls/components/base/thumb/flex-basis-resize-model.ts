import { ElementRef }  from '@angular/core';
import { ResizeModel } from './resize-model';

export class FlexBasisResizeModel implements ResizeModel {
    constructor(element: any, public IsPrevious: boolean, public IsHorizontal: boolean) {
        if (element)
            this.Element = element.nativeElement ? element.nativeElement : element;
    }

    Element;

    resize(event, movingEle: ElementRef) {
        if (!this.Element) return;

        if (event.stopPropagation) event.stopPropagation();
        if (event.preventDefault) event.preventDefault();

        var isHorizontal = this.IsHorizontal;
        
        var elementOffsetSizeProp = isHorizontal ? "offsetWidth" : "offsetHeight";
        var elementOffsetProp = isHorizontal ? "offsetLeft" : "offsetTop";

        var mouseMovement = this.getMouseMovement(event, movingEle);

        var basis;
        if (this.IsPrevious)
            basis = this.Element[elementOffsetSizeProp] + mouseMovement;
        else 
            basis = this.Element[elementOffsetSizeProp] - mouseMovement;
        this.Element.style['flex-basis'] = basis + "px";

        return basis;
    }

    private getMouseMovement(event, movingEle: ElementRef): number {
        var boundingBox = movingEle.nativeElement.getBoundingClientRect();
        if (this.IsHorizontal)
            return event.clientX - boundingBox.left;
        return event.clientY - boundingBox.top;
    }
}