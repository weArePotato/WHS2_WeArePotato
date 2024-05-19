import { 
  Component, 
  HostBinding,
  Input }       from '@angular/core';

@Component({
  selector: 'pm-busy-indicator-overlay-circular',
  //templateUrl: './app/controls/components/busy-indicator/busy-indicator-overlay/busy-indicator-overlay-circular.html',
  templateUrl: './busy-indicator-overlay-circular.html',
  host: {
    '[style.background-color]': 'BackgroundColor',
  },
  styles: [`
  :host { 
    position: absolute;
    top: 0px;
    left: 0px;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 100%;
    z-index: 1000;
    opacity: .8;
    flex-direction: column;
  }
  `]
})
export class BusyIndicatorOverlayCircularComponent {
   @Input() BusyMessage = "Please Wait...";
   @Input() IsBusy;
   @Input() BackgroundColor = '#FFFFFF';
   @HostBinding('class.left-bar') leftBarClass = true;
}