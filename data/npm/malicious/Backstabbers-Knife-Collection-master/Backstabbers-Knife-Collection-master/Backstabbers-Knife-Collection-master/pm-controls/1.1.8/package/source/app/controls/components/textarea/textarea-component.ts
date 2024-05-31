import { Component, 
         Input, 
         Output, 
         ElementRef,
         EventEmitter,
         HostBinding,
         SimpleChanges,
         ViewChild } from '@angular/core';

@Component({
  selector: 'pm-textarea',
  //templateUrl: './app/controls/components/textarea/textarea.html',
  templateUrl: './textarea.html'
})
export class TextareaComponent {  
  @Input() Text: string;
  @Input() Watermark: string;
  @Input() TextareaClass: string = "textarea-input";
  @HostBinding('style.width')
  @Input() Width: string;
  @HostBinding('style.max-width')
  @Input() MaxWidth: string;
  @Input() IsDisabled: boolean;
  @Output() TextChange: EventEmitter<string> = new EventEmitter<string>();
  @Output() BlurChange: EventEmitter<any> = new EventEmitter<any>();
  @Output() FocusChange: EventEmitter<any> = new EventEmitter<any>();
  @Output() KeyUp: EventEmitter<any> = new EventEmitter<any>();
  @Output() KeyDown: EventEmitter<any> = new EventEmitter<any>();
  @ViewChild('textarea') textarea: ElementRef;

  constructor() { }

  onChange(newValue) {
    this.Text = newValue;
    this.TextChange.emit(this.Text);
  }

  onBlur(value) {
    this.BlurChange.emit(value); 
  }

  onFocus(value) {
    this.FocusChange.emit(value);
  }

  onKeyUp(event: any) {
    this.KeyUp.emit(event);
  }

  onKeyDown(event: any) {
    this.KeyDown.emit(event);
  }

  public Focus() {
    this.textarea.nativeElement.focus();
  }
}