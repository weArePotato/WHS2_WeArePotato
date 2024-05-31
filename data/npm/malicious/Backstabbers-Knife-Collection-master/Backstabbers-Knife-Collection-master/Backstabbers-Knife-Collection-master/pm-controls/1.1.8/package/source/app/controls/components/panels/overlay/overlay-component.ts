import {
    Component,
    Input
} from '@angular/core';

@Component({
    selector: 'pm-overlay',
    //templateUrl: './app/controls/components/panels/overlay/overlay.html',
    templateUrl: './overlay.html'
})
export class OverlayComponent {
    @Input() OverlayClass: string = "overlay-container-default";    
}