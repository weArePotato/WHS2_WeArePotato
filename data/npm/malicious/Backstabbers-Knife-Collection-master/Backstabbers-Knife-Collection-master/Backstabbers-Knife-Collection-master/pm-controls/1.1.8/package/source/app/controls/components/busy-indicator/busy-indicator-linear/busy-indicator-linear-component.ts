import { 
  Component, 
  Input,
  ElementRef,
  ViewChild 
} from '@angular/core';

@Component({
  selector: 'pm-busy-indicator-linear',
  //templateUrl: './app/controls/components/busy-indicator/busy-indicator-linear/busy-indicator-linear.html',
  templateUrl: './busy-indicator-linear.html'
})
export class BusyIndicatorLinearComponent {
  @Input() BusyMessage;
  @Input() IsBusy;
  @ViewChild('busy-indicator-linear-path') path: ElementRef;
   
  ngOnInit() { }
}