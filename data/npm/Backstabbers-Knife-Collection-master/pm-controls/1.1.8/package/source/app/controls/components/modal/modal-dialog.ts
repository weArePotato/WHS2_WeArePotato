import { 
    Component, 
    Input, 
    Output, 
    EventEmitter, 
    NgModule
} from '@angular/core';

import 'rxjs/add/observable/fromEvent';

import { Observable }   from 'rxjs/Observable';
import { Subscription } from 'rxjs/Subscription';
import { KeyCodes } from '../../../objects/key-codes';
    
export class ModalDialog {
  KeyPress: Subscription;
  ShowModal: boolean; 
  @Input() Header: string;
  @Input() CanResize: boolean = true;
  @Output() OnClosed: EventEmitter<boolean> = new EventEmitter<boolean>();   
  Close(result: boolean) { this.OnClosed.emit(result); }

  Initialize() {
    var that = this;
    this.KeyPress = Observable.fromEvent(document, 'keydown').subscribe(function(e : KeyboardEvent) {
      if (e.keyCode == KeyCodes.ESCAPE)        
        that.Close(false);
    });  
  }

  Destroy() {
    this.KeyPress.unsubscribe();
  }
}