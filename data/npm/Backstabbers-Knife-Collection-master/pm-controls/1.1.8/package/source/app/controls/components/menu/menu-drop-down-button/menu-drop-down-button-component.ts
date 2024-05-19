import { Component, 
         EventEmitter,
         Input,
         OnDestroy,         
         OnInit,
         Output,
         ViewContainerRef } from '@angular/core';

@Component({
  selector: 'pm-menu-drop-down-button',
  //templateUrl: './app/controls/components/menu/menu-drop-down-button/menu-drop-down-button.html',
  templateUrl: './menu-drop-down-button.html'
})
export class MenuDropDownButtonComponent implements OnInit, OnDestroy {
  @Input() IsDropDownOpen: boolean;
  @Input() IsDisabled: boolean;
  @Input() HorizontalAlignment: string;
  @Input() ButtonClass: string = "menu-button-button";
  @Input() ContainerClass: string = "menu-button-container";
  @Input() DropDownClass: string;
  @Input() OpenDropDownOnHover: boolean;
  @Output() IsDropDownOpenChange: EventEmitter<boolean> = new EventEmitter();

  private el: Element;
  private clickEvent;

  constructor(viewContainerRef: ViewContainerRef) {
    this.el = viewContainerRef.element.nativeElement;
    this.clickEvent = this.HandleClick.bind(this);
  }

  ngOnInit() {
    this.IsDropDownOpen = this.IsDropDownOpen || false;

    let body = document.querySelector('body');
    body.addEventListener('click', this.clickEvent, false);
  }

  ngOnDestroy() {
    let body = document.querySelector('body');
    body.removeEventListener('click', this.clickEvent, false);
  }

  HandleClick(e) {
    if (!this.IsDropDownOpen || !e.target) { return; };
    if (this.el !== e.target && !this.el.contains((<any>e.target))) {
      this.IsDropDownOpen = false;
      this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
    }
  }

  click() {
    this.IsDropDownOpen = !this.IsDropDownOpen;
    this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
  }

  mouseenter() {
    if(this.IsDropDownOpen) return;
    
    this.IsDropDownOpen = true;
    this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
  }

  mouseleave() {
    if (!this.IsDropDownOpen) return;

    this.IsDropDownOpen = false;
    this.IsDropDownOpenChange.emit(this.IsDropDownOpen);  
  }
}