import {
    Component,
    Input,
    HostBinding,
    ViewChild,
    ElementRef,
    Renderer,
    ChangeDetectionStrategy,
    EventEmitter,
    Output
} from '@angular/core';

import { ResizeModel }          from './resize-model';
import { FlexBasisResizeModel } from './flex-basis-resize-model';
import { FlexGrowResizeModel }  from './flex-grow-resize-model';
import { Orientation } from '../../../../objects/enums/orientation';

@Component({
    selector: 'pm-thumb',
    //templateUrl: './app/controls/components/base/thumb/thumb.html',
    templateUrl: './thumb.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ThumbComponent {
    resizeEvent;
    dragendEvent;
    dragging: boolean = false;
    Resizer: ResizeModel;
    @Input() ItemOrientation: Orientation = Orientation.Vertical; // orientation of items around thumb.
    @Input() ElementFlexBasis: ElementRef;
    @Input() ElementLocation: string = "previous";
    @Input() FirstElementFlexGrow: string = ".5";
    @Input() SecondElementFlexGrow: string = ".5";
    @Input() CustomClass;
    @Input() BackgroundClass;
    @Input() UseDefaultResizeModel = true;
    @Input() Mode: string = "Grow";
    @Output() DragStart: EventEmitter<any> = new EventEmitter();
    @Output() DragEnd: EventEmitter<any> = new EventEmitter();
    @Output() Resize: EventEmitter<any> = new EventEmitter();
    @ViewChild('gripper') gripperEle: ElementRef;

    get IsFlexGrow() {
        if (this.Mode)
            return this.Mode.toLowerCase() == "grow";
        return false;
    }

    get IsFlexBasis() {
        if (this.Mode)
            return this.Mode.toLowerCase() == "basis";
        return false;
    }

    constructor(private thumbEle: ElementRef) {
        this.resizeEvent = this.resize.bind(this);
        this.dragendEvent = this.dragend.bind(this);
    }

    ngOnInit() {
        if (this.IsFlexGrow) {
            var firstEle = this.thumbEle.nativeElement.previousElementSibling;
            if (!firstEle) return;

            var secondEle = this.thumbEle.nativeElement.nextElementSibling;
            if (!secondEle) return;

            firstEle.style['flex-grow'] = Math.max(0.0, parseFloat(this.FirstElementFlexGrow));
            secondEle.style['flex-grow'] = Math.max(0.0, parseFloat(this.SecondElementFlexGrow));

            this.Resizer = new FlexGrowResizeModel([firstEle], [secondEle], this.isHorizontal());
        } else if (this.IsFlexBasis) {
            if (!this.ElementFlexBasis) return;            
            this.Resizer = new FlexBasisResizeModel(this.ElementFlexBasis, this.isPrevious(), this.isHorizontal());
        }
    }

    useVerticalDefaultClass() {
        return (!this.CustomClass || this.CustomClass == "") && !this.isHorizontal();
    }

    useHorizontalDefaultClass() {
        return (!this.CustomClass || this.CustomClass == "") && this.isHorizontal();
    }

    isHorizontal() {
        return this.ItemOrientation == Orientation.Horizontal;
    }

    isPrevious() {
        return this.ElementLocation.toLowerCase() == "previous";
    }

    get ThumbClass() {
        if (this.CustomClass)
            return;
        return this.useVerticalDefaultClass() ? 'thumb-horizontal-dots' : 'thumb-vertical-dots';
    }

    get GripperClass() {
        if (this.CustomClass)
            return this.CustomClass;
        return this.useVerticalDefaultClass() ? 'default-thumb-ns' : 'default-thumb-ew';
    }

    dragstart(event) {
        this.DragStart.emit(event);
        
        document.addEventListener('mousemove', this.resizeEvent);
        document.addEventListener('mouseup', this.dragendEvent);
                
        this.dragging = true;

        if (event.preventDefault) event.preventDefault();
        if (event.stopPropagation) event.stopPropagation();
    }

    dragend(event) {
        this.DragEnd.emit(event);
        
        if (this.UseDefaultResizeModel)
            this.resize(event);
                
        this.dragging = false;

        document.removeEventListener('mousemove', this.resizeEvent, false);
        document.removeEventListener('mouseup', this.dragendEvent, false);

        if (event.preventDefault) event.preventDefault();
        if (event.stopPropagation) event.stopPropagation();
    }

    resize(event) {
        if (!this.dragging) return;
        
        if (this.Resizer) {
            var size = this.Resizer.resize(event, this.gripperEle);
            this.Resize.emit(size);
        }

        if (event.preventDefault) event.preventDefault();
        if (event.stopPropagation) event.stopPropagation();
        // event.cancelBubble = true;
        // event.returnValue = false;
        // return false;
    }
}