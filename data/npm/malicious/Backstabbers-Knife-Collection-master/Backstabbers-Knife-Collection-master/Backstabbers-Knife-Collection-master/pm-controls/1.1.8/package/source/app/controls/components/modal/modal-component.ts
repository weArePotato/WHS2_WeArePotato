import { Component, 
         Input, 
         OnInit,
         Output, 
         EventEmitter, 
         NgModule,
         ViewChild }      from '@angular/core';

import { ModalDialog }   from './modal-dialog';

@Component({
  selector: 'pm-modal',
  //templateUrl: './app/controls/components/modal/modal.html',
  templateUrl: './modal.html'
})
export class ModalComponent implements OnInit {
  constructor() {
  }

  ngOnInit() { 
    this.PreviousHeight = this.HeightPx ? this.HeightPx + "px" : "auto";
    this.PreviousWidth = this.WidthPx ? this.WidthPx + "px" : "auto";
    this.PreviousBodyHeight = this.BodyHeightPx + "px";
    this.PreviousBodyWidth = this.BodyWidthPx + "px";
    this.ResetContainer();
    this.ResetBody();    
  }

  @Input() BackgroundColor: any;
  IsMinimized: boolean;
  IsMaximized: boolean;
  @Input() ShowModal: boolean;
  @Input() Header: string;
  @Output() OnClosed: EventEmitter<boolean> = new EventEmitter<boolean>();   
  @ViewChild('modal') modal: any;
  dragging :boolean = false;
  HeightPx: any;
  PreviousHeight: any;
  @Input() BodyHeightPx: any;
  PreviousBodyHeight: any;  
  BodyHeight: any;
  WidthPx: any;
  PreviousWidth: any;
  @Input() BodyWidthPx: any;
  PreviousBodyWidth: any;  
  BodyWidth: any;
  Bottom: any;
  Top: any;
  PreviousTop: any;
  Left: any;
  PreviousLeft: any;
  Right: any;
  Position: any;
  Height: any;
  Width: any;
  Display:any;
  CanResize:boolean;
  
  Show() {
    this.ShowModal = true;
  }

  Close(result: boolean) {
     this.OnClosed.emit(result);
     this.ShowModal = false;
  }

  Minimize() {
    if (this.IsMinimized)
    {
      this.IsMinimized = false;
      this.Right = this.Bottom = "auto";
      this.Left = this.PreviousLeft;
      this.Top = this.PreviousTop;      
      this.Position = "relative";
      
      this.ResetBody();
      this.ResetContainer();
    }
    else
    {
      this.IsMinimized = true;
      this.IsMaximized = false;
      this.Bottom = "10px";
      this.PreviousLeft = this.modal.nativeElement.style.left;
      this.PreviousTop = this.modal.nativeElement.style.top;
      this.Top = this.Left = "auto";
      this.Right  = "10px";
      this.Position = "absolute";

      this.SetContainer("30px", "200px");
    }
  }

  Maximize() {
    if (this.IsMaximized)
    {
      this.IsMaximized = false;
      this.Left = this.PreviousLeft;
      this.Top = this.PreviousTop;
      this.Position = "relative";

      this.ResetBody();
      this.ResetContainer();
    }
    else
    {
      this.IsMaximized = true;
      this.IsMinimized = false;
      this.PreviousLeft = this.modal.nativeElement.style.left;
      this.PreviousTop = this.modal.nativeElement.style.top;
      this.Top = this.Left = "0px";
      this.Position = "absolute";

      this.SetBody("100%", "100%");
      this.SetContainer("calc(100% - 40px)", "100%");
    }
  }

  SetBody(height: any, width: any) {
    // this.PreviousBodyHeight = this.BodyHeightPx + "px";
    // this.PreviousBodyWidth =  this.BodyWidthPx + "px";

    this.BodyWidth = width;
    this.BodyHeight = height;
  }

  ResetBody() {
    this.BodyHeight = this.PreviousBodyHeight;
    this.BodyWidth = this.PreviousBodyWidth;
  }

  SetContainer(height: any, width: any) {
    // this.PreviousHeight = this.Height;
    // this.PreviousWidth = this.Width;

    this.Width = width;
    this.Height = height;
  }

  ResetContainer() {
    this.Height = this.PreviousHeight;
    this.Width = this.PreviousWidth;
  }

  OnDoubleClick() {
    if (this.IsMaximized)
      this.Maximize();
    else
      this.Minimize();
  }
}