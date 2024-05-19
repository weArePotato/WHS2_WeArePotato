import { 
  Component,
  Input
} from '@angular/core';
  
@Component({
  selector: 'pm-context-menu-item',
  //templateUrl: './app/controls/components/context-menu/context-menu-item.html',
  templateUrl: './context-menu-item.html'
})
export class ContextMenuItemComponent {
  @Input() IsDisabled: boolean;

  get DisabledClass() {
    if (this.IsDisabled)
      return "context-menu-item-disabled";
  }
}