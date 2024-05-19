import { Component, Input, 
         EventEmitter, Output }       from '@angular/core';

@Component({
  selector: 'pm-button',
  //templateUrl: './app/controls/components/buttons/button/button.html',
  templateUrl: './button.html',
  styles: [`
    :host { 
      margin-top: 6px;
      margin-bottom: 6px;
    }
  `]  
})
export class ButtonComponent {
  @Output() Click = new EventEmitter();
  @Input() IsDisabled: boolean;
  @Input() ButtonClass: string = "button-primary";

  OnClick() {
    if (this.IsDisabled) return;
    this.Click.emit();    
  }
}