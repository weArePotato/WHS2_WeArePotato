import { 
  Component, 
  HostBinding,
  Input }       from '@angular/core';

@Component({
  selector: 'pm-busy-indicator-overlay',
  //templateUrl: './app/controls/components/busy-indicator/busy-indicator-overlay/busy-indicator-overlay.html',
  templateUrl: './busy-indicator-overlay.html',
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
  }
  `]
})
export class BusyIndicatorOverlayComponent {
  @Input() BusyMessage = "Please Wait...";    
  @Input() Header;    
  @Input() IsBusy;
  @Input() BackgroundColor = '#FFFFFF';
  @HostBinding('class.left-bar') leftBarClass = true;
}