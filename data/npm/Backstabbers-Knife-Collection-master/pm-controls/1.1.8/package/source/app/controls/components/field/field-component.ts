import { Component, Input, 
         EventEmitter, Output }       from '@angular/core';

@Component({
  selector: 'pm-field',
  //templateUrl: './app/controls/components/field/field.html',
  templateUrl: './field.html'
})
export class FieldComponent {
  @Input() Label: string;
  @Input() LabelWidth: string;
  @Input() Content: string;
}