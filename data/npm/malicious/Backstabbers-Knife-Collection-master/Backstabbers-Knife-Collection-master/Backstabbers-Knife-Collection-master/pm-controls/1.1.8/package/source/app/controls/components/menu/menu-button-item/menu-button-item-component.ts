import { 
    Component, 
    EventEmitter,
    Input,         
    OnInit,
    Output,
    OnDestroy,
    ViewContainerRef 
  } from '@angular/core';
  
  @Component({
    selector: 'pm-menu-button-item',
    //templateUrl: './app/controls/components/menu/menu-button-item/menu-button-item.html',
    templateUrl: './menu-button-item.html'
  })
  export class MenuButtonItemComponent {
    @Input() IsDisabled: boolean;
    
    get MenuButtonItemClass() {
        if (this.IsDisabled)
            return "menu-button-item-disabled";
        return "menu-button-item";
    }
  }