import { Component, 
         Input,
         ElementRef,
         ViewChild }       from '@angular/core';

@Component({
  selector: 'pm-busy-indicator-circular',
  //templateUrl: './app/controls/components/busy-indicator/busy-indicator-circular/busy-indicator-circular.html',
  templateUrl: './busy-indicator-circular.html'
})
export class BusyIndicatorCircularComponent {
  @Input() BusyMessage;
  @Input() IsBusy;
  @ViewChild('busy-indicator-circular-path') path: ElementRef;
   
  ngOnInit() { }
}