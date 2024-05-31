import {
    Component,
    EventEmitter,
    HostBinding,
    TemplateRef,
    Input,
    Output
} from '@angular/core';
import { Icon } from '../../../objects/icon/icon';

@Component({
    selector: 'pm-icon-caret-down',
    //templateUrl: './app/controls/components/svg/icon-caret-down/icon-caret-down.html'
    templateUrl: './icon-caret-down.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconCaretDownComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 8;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}