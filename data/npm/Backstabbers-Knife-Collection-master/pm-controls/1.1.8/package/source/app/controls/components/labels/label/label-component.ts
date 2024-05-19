import { Component, Input, 
         EventEmitter, Output }       from '@angular/core';

@Component({
  selector: 'pm-label',
  //templateUrl: './app/controls/components/labels/label/label.html',
  templateUrl: './label.html',
  styles: [`
    :host { 
        display: flex;
        align-items: center;
        flex-shrink: 0;
    }
  `]
})
export class LabelComponent {  
    @Input() Label;
    @Input() LabelWidth: string;
}