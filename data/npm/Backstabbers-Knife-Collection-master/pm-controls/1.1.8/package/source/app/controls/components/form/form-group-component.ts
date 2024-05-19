import { 
  Component,
  Input,
  EventEmitter, 
  Output 
} from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { Orientation } from '../../../objects/enums/orientation';

@Component({
  selector: 'pm-form-group',
  //templateUrl: './app/controls/components/form/form-group.html',
  templateUrl: './form-group.html'
})
export class FormGroupComponent {   
   @Input() Property: Property;
   @Input() ShowTooltip: boolean;


  get OrientationClass() {
    if (this.Property && this.Property.Orientation == Orientation.Horizontal)
      return "form-horizontal";
  }

  get GroupContainerClass() {
    if (this.Property && this.Property.Orientation == Orientation.Horizontal)
      return "layout-flex layout-flex-fill";
  }

  get GroupClass() {
    if (this.Property && this.Property.Orientation == Orientation.Horizontal)
      return "layout-flex-fill";
  }
}