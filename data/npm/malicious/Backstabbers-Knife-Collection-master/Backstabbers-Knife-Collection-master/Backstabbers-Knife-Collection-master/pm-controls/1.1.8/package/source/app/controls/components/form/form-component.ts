import { 
  Component, 
  EventEmitter,
  TemplateRef,
  Input, 
  Output
} from '@angular/core';
import { BaseRequest } from '../../../objects/request/base-request';
import { HorizontalAlignment } from '../../../objects/enums/horizontal-alignment';

@Component({
  selector: 'pm-form',
  //templateUrl: './app/controls/components/form/form.html'
  templateUrl: './form.html'
})
export class FormComponent {
  @Output() onSubmit = new EventEmitter();
  @Output() onClear = new EventEmitter();
  @Output() onCancel = new EventEmitter();
  @Input() Request: BaseRequest = new BaseRequest();
  @Input() ButtonTemplate: TemplateRef<any>;
  @Input() Header: string;
  @Input() ActivityTypes;
  @Input() IsBusy: boolean;
  @Input() CanClear: boolean = false; 
  @Input() ButtonClearLabel: string = "Clear";
  @Input() CanCancel: boolean = false; 
  @Input() ButtonCancelLabel: string = "Cancel";
  @Input() ButtonLabel: string = "Submit";
  @Input() ButtonHorizontalAlignment: HorizontalAlignment = HorizontalAlignment.Left;
  
  DevMode: boolean;
  
  Submit() {
    if (this.Request.Validate())
      this.onSubmit.emit({});
  }

  Clear() {
    this.onClear.emit({});
  }

  Cancel() {
    this.onCancel.emit({});
  }

  ShowSettings() {
    
  }

  get ButtonClass() {
    if (this.ButtonHorizontalAlignment == HorizontalAlignment.Right)
      return "form-button-right";
  }
}