import { 
  Component,
  ChangeDetectorRef,
  Input, 
  Output,
  ViewChild,
  EventEmitter,
  ComponentFactoryResolver,
  ViewContainerRef 
} from '@angular/core';
import { ModalDialog } from '../../../controls/components/modal/modal-dialog';
import { ControlsModule } from '../../../controls/controls-module';
@Component({
  //templateUrl: './app/controls/services/dialog/alert-dialog.html',
  templateUrl: './alert-dialog.html',
  styles: [`
    :host {   
      position: absolute;
      height: 100%;
      width: 100%;
      top: 0px;
      z-index: 1000;
    }
  `]
})
export class AlertDialog extends ModalDialog {
  constructor(public changeDetectorRef: ChangeDetectorRef) {
    super();
  }

  Header: string = "Alert";
  Content: string;

  static Show(header: string, content: string) : AlertDialog {
      var dialog = <AlertDialog> ControlsModule.dialog.Show(AlertDialog);
      dialog.Header = header;
      dialog.Content = content;
      dialog.RaiseChange();
      return dialog;
  }
  
  RaiseChange() {
      this.changeDetectorRef.detectChanges();
  }
}