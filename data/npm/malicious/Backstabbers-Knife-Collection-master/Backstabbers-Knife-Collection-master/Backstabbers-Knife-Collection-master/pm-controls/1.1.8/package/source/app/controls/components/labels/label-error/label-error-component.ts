import { Component, Input, 
         EventEmitter, Output }       from '@angular/core';

@Component({
  selector: 'pm-label-error',
  //templateUrl: './app/controls/components/labels/label-error/label-error.html',
  templateUrl: './label-error.html'
})
export class LabelErrorComponent {  
    @Input() Label;
}