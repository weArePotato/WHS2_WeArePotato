import { 
    Component,
    Input,
    HostBinding,
    ViewChild,
    ElementRef,
    Renderer,
    ChangeDetectionStrategy 
} from '@angular/core';
import { Orientation } from '../../../../objects/enums/orientation';

@Component({
    selector: 'pm-gripper',
    //templateUrl: './app/controls/components/base/gripper/gripper.html',
    templateUrl: './gripper.html',
    styles: [`
    :host { 
      height: 100%;
    }
    `],
})
export class GripperComponent {

    @Input() ItemOrientation: Orientation = Orientation.Vertical; // orientation of items around thumb.
}