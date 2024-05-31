import { 
    Component,
    ChangeDetectorRef,
    Input,
} from '@angular/core';
import { Toast } from '../../../controls/components/toast/toast';

@Component({    
    //templateUrl: './app/controls/services/logging/error-toast.html',
    templateUrl: './error-toast.html',
    styles: [`
    :host {
      pointer-events: none;
      position: absolute;
      height: 100%;
      width: 100%;
      top: 0px;
      z-index: 1000;
    }
  `]
})
export class ErrorToast extends Toast {
    constructor(
        public changeDetectorRef: ChangeDetectorRef) {
        super();
    }

    @Input() Name: string;
    @Input() Message: string;
    @Input() Stack: string;
    
    CopyToClipBoard(e: MouseEvent) {
        var t = document.createElement("textarea");
        
        t.style.position = 'fixed';
        t.style.top = '0';
        t.style.left = '0';
        t.style.opacity = '0';
        t.value = this.Name + "\n" + this.Message + "\n" + this.Stack;
        document.body.appendChild(t);
        t.select();
        try {
            document.execCommand('copy');
        } catch { }
        document.body.removeChild(t);
    }

    RaiseChange() {
        this.changeDetectorRef.detectChanges();
    }
}