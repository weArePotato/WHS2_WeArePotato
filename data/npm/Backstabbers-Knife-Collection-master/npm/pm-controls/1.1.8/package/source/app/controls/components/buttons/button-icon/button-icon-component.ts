import { 
  Component, 
  EventEmitter,
  Input, 
  Output }       from '@angular/core';

@Component({
  selector: 'pm-button-icon',
  //templateUrl: './app/controls/components/buttons/button-icon/button-icon.html',
  templateUrl: './button-icon.html',
  styles: [`
    :host {
      display: flex;
    }
  `],
})
export class ButtonIconComponent {  
  @Output() Click = new EventEmitter();
  @Input() ButtonClass: string = "button-icon-default";
  @Input() IsDisabled: boolean;
  @Input() MaxHeight: string;
  
  OnClick() {
    if (this.IsDisabled) return;
    this.Click.emit();    
  }
}