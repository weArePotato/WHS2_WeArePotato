import {
  Component,
  ComponentRef,
  ChangeDetectorRef,
  ElementRef,
  EventEmitter,
  HostBinding,
  Inject,
  Input,
  OnChanges,
  OnDestroy,
  Optional,
  Output,
  QueryList,
  SimpleChanges,
  TemplateRef,
  ViewChild,
  ViewContainerRef
} from '@angular/core';

@Component({
  selector: 'pm-context-menu',
  //templateUrl: './app/controls/components/context-menu/context-menu.html',
  templateUrl: './context-menu.html'
})
export class ContextMenuComponent {

  constructor(
    private changeDetectorRef: ChangeDetectorRef, 
    viewContainerRef: ViewContainerRef) {
    this.el = viewContainerRef.element.nativeElement;
    this.clickEvent = this.HandleClick.bind(this);
  }

  @Input() ContextMenuTemplate: any;
  @ViewChild('ContextMenuContainer') ContextMenuContainerElement: any;
  
  private el: Element;
  private isOpen: boolean;
  private clickEvent;  

  @Input()
  get IsOpen() {
    return this.isOpen;
  }
  set IsOpen(value: boolean) {
    if (this.isOpen != value)
    {
      let body = document.querySelector('body');
      if (value) {
        body.addEventListener('click', this.clickEvent, false);
        this.Open.emit(true);
      }        
      else
      {
        body.removeEventListener('click', this.clickEvent, false);
        this.Open.emit(false);
      }
    }
    this.isOpen = value;    
    this.changeDetectorRef.detectChanges();
  }

  @Input() Top: any;
  @Input() Left: any;
  @Input() DataContext: any;
  @Output() Open: EventEmitter<boolean> = new EventEmitter();

  public Show(left: number, top: number) {
    this.IsOpen = true;

    this.changeDetectorRef.detectChanges();
    var menu = this.ContextMenuContainerElement.nativeElement.getBoundingClientRect();

    if(left + menu.width > window.innerWidth){
        // Part of the menu is off the right side of the viewable part of the screen.
        // Recalculate a new position for the left side of the menu.
        var viewableWidthOfMenu = window.innerWidth - left;
        var hiddenWidthOfMenu = menu.width - viewableWidthOfMenu;
        var buffer = 50;
        var potentialNewLeft = left - hiddenWidthOfMenu - buffer;

        // Guard against a wide menu and a narrow window that could push the
        // left side of the menu off the left side of the screen.
        this.Left = potentialNewLeft < 0 ? buffer : potentialNewLeft;
        this.changeDetectorRef.detectChanges();
    }
    else{
      this.Left = left;
    }

    this.Top = top;
  }

  HandleClick(e) {
    if (this.el !== e.target && !this.el.contains((<any>e.target))) {
      this.IsOpen = false;
    }
  }
}