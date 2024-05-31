import { 
    Component,
    Input
  } from '@angular/core';
    
  @Component({
    selector: 'pm-menu-drop-down-item',
    //templateUrl: './app/controls/components/menu-drop-down-item/menu-drop-down-item.html',
    templateUrl: './menu-drop-down-item.html'
  })
  export class MenuDropDownItemComponent {
    @Input() IsDisabled: boolean;
  
    get DisabledClass() {
      if (this.IsDisabled)
        return "menu-drop-down-item-disabled";
    }
  }