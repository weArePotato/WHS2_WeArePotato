import {
  ChangeDetectorRef, 
  Component, 
  Input, 
  Output, 
  EventEmitter,
} from '@angular/core';

@Component({
  selector: 'pm-check-box',
  //templateUrl: './app/controls/components/boxes/check-box/check-box.html',
  templateUrl: './check-box.html',
  // animations: [
  //   trigger('animationState', [
  //     state('clickAnimate', style({
  //       transition: '.24s'
  //     })),
  //   ])
  // ]
})
export class CheckBoxComponent {
  constructor(public changeDetectorRef: ChangeDetectorRef) { }
  
  @Input() Label;
  @Input() CheckBoxTheme: string = "check-box-default";
  @Input() IsAnimated: boolean = true;
  @Input() IsReadOnly: boolean;
  @Input() IsChecked: boolean;
  @Input() IsDisabled: boolean;
  @Output() IsCheckedChange: EventEmitter<any> = new EventEmitter<any>();
  CheckBoxStateClass: string;

  OnClick() {
    if (this.IsReadOnly || this.IsDisabled) return;
    this.CheckBoxStateClass = "check-box-click-animate";
    this.IsChecked = !this.IsChecked;
    this.IsCheckedChange.emit(this.IsChecked);
    this.changeDetectorRef.detectChanges();
  }

  get CheckBoxClass() {
    if (this.IsChecked) {
      if (this.IsDisabled)
        return "is-checked-disabled";
      return this.CheckBoxTheme;
      
    }      
    else {
      if (this.IsDisabled)
        return "is-unchecked-disabled";
      return "is-unchecked";
    }
  }
}