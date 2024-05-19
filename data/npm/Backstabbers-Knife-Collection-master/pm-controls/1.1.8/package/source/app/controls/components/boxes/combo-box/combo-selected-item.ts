import {ChangeDetectorRef,
        Component,
        Input,
        OnInit,
        Output,
        EventEmitter,
        SimpleChanges } from '@angular/core';
import { CompatibilityService } from '../../../services/compatibility/compatibility-service';

@Component({
  selector: 'pm-combo-selected-item',
  //templateUrl: './app/controls/components/boxes/combo-box/combo-selected-item.html',
  templateUrl: './combo-selected-item.html',
  styles: [`
  :host { 
    margin-right: 1px;
    display: inline-block;
    max-height:80px;
    white-space: normal;
  }
  `],
})
export class ComboSelectedItemComponent {

  @Input() Item: any; 
  @Input() DisplayMemberPath: any;
  @Input() ShowRemoveItem: boolean;
  @Output() OnDelete : EventEmitter<any> = new EventEmitter();

  constructor(public CompatibilityService: CompatibilityService) {
  }

  removeItem() {
    this.OnDelete.emit(this.Item);
  }

  getItemDisplay(item) :string {
    if (!item)
      return;
            
    if (!this.DisplayMemberPath)
      return item;
    
    if(typeof this.DisplayMemberPath === "function")
      return this.DisplayMemberPath(item);
    else if (item[this.DisplayMemberPath])
      return <string>item[this.DisplayMemberPath];
    return item;
  }
}