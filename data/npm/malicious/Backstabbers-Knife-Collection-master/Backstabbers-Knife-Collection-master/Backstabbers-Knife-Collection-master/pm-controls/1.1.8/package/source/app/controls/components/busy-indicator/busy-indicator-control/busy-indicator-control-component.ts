import { Component, Input }       from '@angular/core';

@Component({
  selector: 'pm-busy-indicator-control',
  //templateUrl: './app/controls/components/busy-indicator/busy-indicator-control/busy-indicator-control.html',
  templateUrl: './busy-indicator-control.html'
})
export class BusyIndicatorControlComponent {
   @Input() BusyMessage;
   @Input() IsBusy;
}