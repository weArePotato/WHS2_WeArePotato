import {
    Directive,
    HostListener,
    Input
} from '@angular/core';

import { ContextMenuComponent } from '../../components/context-menu/context-menu-component';

@Directive({
    selector: '[popupMenu]',
})
export class PopupMenuDirective {
    @Input() public popupMenu: ContextMenuComponent;
    @Input() public popupMenuDataContext: any;
    @Input() public popupContextMenuTemplate: any;
    
    @HostListener('click', ['$event'])
    public onPopupMenu(event: MouseEvent): void {        
        this.popupMenu.DataContext = this.popupMenuDataContext;
        this.popupMenu.ContextMenuTemplate = this.popupContextMenuTemplate;
        this.popupMenu.Show(event.clientX, event.clientY);        
        event.preventDefault();
        event.stopPropagation();
    }
}