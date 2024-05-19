import { Component, Input, 
         EventEmitter, Output }       from '@angular/core';

@Component({
  selector: 'pm-toast',
  //templateUrl: './app/controls/components/toast/toast.html',
  templateUrl: './toast.html',
  styles: [`
  :host {   
    position: relative;
  }
`]
})
export class ToastComponent {
  @Input() ShowToast: boolean;
  @Output() OnClosed: EventEmitter<boolean> = new EventEmitter<boolean>();   

  @Input() Bottom: string = "20px";
  @Input() Left: string = "20px";
  @Input() Position: string = "absolute";
  Height:string|number;
  Width: string | number;
  Top: string;
  Right: string;
  
  Show() {
    this.ShowToast = true;
  }

  Close(result: boolean) {
     this.OnClosed.emit(result);
     this.ShowToast = false;
  }
}