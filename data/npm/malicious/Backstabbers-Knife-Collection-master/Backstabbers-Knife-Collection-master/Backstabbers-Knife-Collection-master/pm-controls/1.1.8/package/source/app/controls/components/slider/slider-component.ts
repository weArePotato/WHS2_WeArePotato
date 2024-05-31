import {
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    Output,
    ViewChild,
    ElementRef
} from '@angular/core';
import { concat } from 'rxjs/operator/concat';
import { ElementExtensions } from '../../../objects/extensions/element-extensions';

@Component({
    selector: 'pm-slider',
    //templateUrl: './app/controls/components/slider/slider.html'
    templateUrl: './slider.html'
})
export class SliderComponent {
    constructor() {
        this.moveEvent = this.move.bind(this);
        this.dragendEvent = this.dragend.bind(this);
    }

    moveEvent;
    dragendEvent;
    dragging: boolean = false;
    @Output() DragStart: EventEmitter<any> = new EventEmitter();
    @Output() DragEnd: EventEmitter<any> = new EventEmitter();
    @ViewChild('sliderthumb') sliderthumb: ElementRef;
    @ViewChild('slidercontainer') slidercontainer: ElementRef;
    
    dragstart(event) {
        this.DragStart.emit(event);
        
        document.addEventListener('mousemove', this.moveEvent);
        document.addEventListener('mouseup', this.dragendEvent);
                
        this.dragging = true;

        if (event.preventDefault) event.preventDefault();
        if (event.stopPropagation) event.stopPropagation();
    }

    dragend(event) {
        this.DragEnd.emit(event);
        
        this.dragging = false;

        document.removeEventListener('mousemove', this.moveEvent, false);
        document.removeEventListener('mouseup', this.dragendEvent, false);

        if (event.preventDefault) event.preventDefault();
        if (event.stopPropagation) event.stopPropagation();
    }

    getOffsetLeft( elem )
    {
        var offsetLeft = 0;
        do {
        if ( !isNaN( elem.offsetLeft ) )
        {
            offsetLeft += elem.offsetLeft;
        }
        } while( elem = elem.offsetParent );
        return offsetLeft;
    }

    move(event) {
        if (!this.dragging) return;
        
        var raw1OffsetLeft = this.getOffsetLeft(this.slidercontainer.nativeElement);

        var maxWidth = ElementExtensions.width(this.slidercontainer);

        console.log("raw1OffsetLeft " + raw1OffsetLeft);

        var offset1 = event.pageX - raw1OffsetLeft;


        if (offset1 < 0) {
            offset1 = 0;
        } else if (offset1 >  maxWidth) {
            offset1 = maxWidth;
        }

        this.sliderthumb.nativeElement.style['left'] = offset1 + 'px';


        
        // this.sliderthumb.nativeElement.style['left'] = x + 'px';
        //var pos = this.getRelativePosition(e);
        //var setPos = (this.orientation === 'vertical') ? (this.maxHandlePos - (pos - this.grabPos)) : (pos - this.grabPos);
        //this.setPosition(setPos);
        //value = this.getValueFromPosition(this.cap(pos, 0, this.maxHandlePos));
        //newPos = this.getPositionFromValue(value);

        // if (this.Resizer) {
        //     var size = this.Resizer.resize(event, this.gripperEle);
        //     this.Resize.emit(size);
        // }

        if (event.preventDefault) event.preventDefault();
        if (event.stopPropagation) event.stopPropagation();
        // event.cancelBubble = true;
        // event.returnValue = false;
        // return false;
    }
}