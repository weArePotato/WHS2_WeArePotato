import { 
    Component, 
    Input,         
    OnInit, 
    Output,
    EventEmitter,
    ViewContainerRef,
    ViewChild,
    SimpleChanges,
    Renderer,
    ElementRef 
} from '@angular/core'; 
import { Orientation } from '../../../../objects/enums/orientation';


// This is the "standard" Resize-Panel. For more control over styling, use pm-thumb.
@Component({
    selector: 'pm-resize-panel',
    //templateUrl: './app/controls/components/panels/resize-panel/resize-panel.html',
    templateUrl: './resize-panel.html',
    styles: [`
    :host { 
      width: 100%;
    }
    `],  
})
export class ResizePanelComponent { 
    @Input() HeightPx: any = "100%";
    @Input() Orientation: Orientation = Orientation.Vertical;
    @Input() FirstElementFlexGrow: number = .5;
    @Input() SecondElementFlexGrow: number = .5;
    @Input() CustomThumbClass: string = "";

    get Height() {
        if (this.HeightPx)
            return this.HeightPx + 'px';
        return "100%";
    }
    flexDirection() {
        return this.isHorizontal()? "row" : "column";
    }    

    isHorizontal() {
        return this.Orientation == Orientation.Horizontal;
    }    

    logDragStart($event) {
        console.log("drag start"+ $event);
    }
}
