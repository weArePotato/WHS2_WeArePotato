import { Directive, 
         HostListener, 
         Input }                from '@angular/core';
         
import { ContextMenuComponent } from '../../components/context-menu/context-menu-component';

@Directive({
  selector: '[contextMenu]',
})
export class ContextMenuDirective {
  @Input() public contextMenu: ContextMenuComponent;

  constructor() { }

  @HostListener('contextmenu', ['$event'])
  public onContextMenu(event: MouseEvent): void {    
    this.contextMenu.Show(event.clientX, event.clientY);    
    event.preventDefault();
    event.stopPropagation();
  }
}