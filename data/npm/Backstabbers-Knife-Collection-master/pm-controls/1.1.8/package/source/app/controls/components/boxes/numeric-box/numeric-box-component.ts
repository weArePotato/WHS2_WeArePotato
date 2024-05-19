import { 
  Component, 
  Input, 
  OnInit,
  Output, 
  EventEmitter, 
  ChangeDetectorRef
} from '@angular/core';

@Component({
  selector: 'pm-numeric-box',
  //templateUrl: './app/controls/components/boxes/numeric-box/numeric-box.html',
  templateUrl: './numeric-box.html',
})
export class NumericBoxComponent implements OnInit {
  @Input() Value: number;
  @Input() IsDisabled: boolean;
  @Output() ValueChange: EventEmitter<any> = new EventEmitter<any>();
  @Input() Watermark: string;
  @Input() MaxValue: number;
  @Input() MinValue: number;
  @Output() TextChange: EventEmitter<string> = new EventEmitter<string>();

  constructor(
    public changeDetectorRef: ChangeDetectorRef) {
      this.changeDetectorRef.detach();
  }

  ngOnInit() {
    if (this.Value) {
      this.Text = this.Value.toString();
    }
  }

  onKeyPress(e: KeyboardEvent) {
    var key = e.key;
    if (isNaN(+key) || key == " ")
      e.preventDefault();
  }

  onPaste(e: ClipboardEvent) {
      var pastedText = undefined;
      if ((<any>window).clipboardData && (<any>window).clipboardData.getData) { // IE
        pastedText = (<any>window).clipboardData.getData('Text');
      } else if (e.clipboardData && e.clipboardData.getData) {
        pastedText = e.clipboardData.getData('text/plain');
      }
     
      // Prevent the default handler from running.
      if (isNaN(pastedText)) return false; 
      if (this.MinValue && pastedText < this.MinValue) return false;
      if (this.MaxValue && pastedText > this.MaxValue) return false;
      if (pastedText != Math.floor(pastedText)) return false;
  }

  incrementUp() {
    if (!isNaN(+this.Text)) {
      var value = +this.Text;
      value++;
      if (this.MaxValue && value > this.MaxValue)
        return;
      this.SetValue(String(value));
    }
    else
       this.SetValue("1");
  }

  incrementDown() {
    if (!isNaN(+this.Text)) {
      var value = +this.Text;
      value--;
      if (this.MinValue && value < this.MinValue)
        return;
      this.SetValue(String(value));
    }
    else
      this.SetValue("0"); 
  }

  onTextChange(newValue) {
    this.SetValue(newValue);
  }

  SetValue(newValue) {   
    this.Text = newValue;
    this.Value = this.Text && !isNaN(+this.Text) ? +this.Text : undefined;
    this.ValueChange.emit(this.Value);
  }

  private text: string;
  @Input()
  get Text() : string 
  {
    return this.text;
  }

  set Text(value: string) {
    this.text = value;
    this.TextChange.emit(value);
    this.changeDetectorRef.detectChanges();
  }
}