import { Component, Input, 
         EventEmitter, Output }       from '@angular/core';

@Component({
  selector: 'pm-button-block',
  //templateUrl: './app/controls/components/buttons/button-block/button-block.html',
  templateUrl: './button-block.html',
  styles: [`
    :host {
      display: flex;
    }
  `],
})
export class ButtonBlockComponent {  
  @Output() Click = new EventEmitter();
  @Input() ButtonClass: string = "button-block";
  @Input() IsDisabled: boolean;

  OnClick() {
    if (this.IsDisabled) return;
    this.Click.emit();    
  }
}