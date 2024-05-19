import { 
    Component, 
    Input, 
    OnInit,
    Output, 
    EventEmitter, 
    ViewChild
  } from '@angular/core';
import { TextBoxComponent } from '../text-box/text-box-component';
import { KeyCodes } from '../../../../objects/key-codes';

  @Component({
    selector: 'pm-multi-select-text-box',
    //templateUrl: './app/controls/components/boxes/multi-select-text/multi-select-text-box.html',
    templateUrl: './multi-select-text-box.html',
  })
  export class MultiSelectTextBoxComponent {
    @Input() IsDisabled: boolean;
    @Input() Watermark: string;
    @Input() Text: string;
    @Input() SelectedItems: Array<any> = []; 
    @Output() SelectedItemsChange: EventEmitter<any> = new EventEmitter<any>();
    @Input() ShowRemoveItem: boolean = true;    
    @ViewChild(TextBoxComponent) textBox: TextBoxComponent;
    
    @Input() MultiSelectTextBoxClass: string = "text-box-input";
    @Input() MultiSelectTextBoxButtonClass: string = "button-icon-default";
    @Input() MultiSelectTextBoxSelectedItemsClass: string = "multi-select-text-box-selected-items";
    Width:any;
    MultiSelectTextBoxPanelClass:any;
    
    AddClick() {
      if (this.Text)
      {
        this.SelectedItems.push(this.Text);
        this.Text = undefined;
      }
    }

    RemoveSelectedItem(item:any) {
      var idx = this.SelectedItems.indexOf(item);
      if(idx<0) {
        console.error("Could not find selected item to remove.");
        console.trace();
        return;
      }
      this.SelectedItems.splice(idx,1);
      this.SelectedItemsChange.emit(this.SelectedItems);
      this.textBox.Focus();
    }

    OnKeyUp(event) {
      if (event.keyCode == KeyCodes.ENTER) {
        if (this.Text) {          
          this.SelectedItems.push(this.Text);
          this.Text = undefined;
        }
      }
    }
  }