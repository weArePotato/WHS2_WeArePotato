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
    selector: 'pm-icon-angle-left',
    //templateUrl: './app/controls/components/svg/icon-angle-left/icon-angle-left.html'
    templateUrl: './icon-angle-left.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconAngleLeftComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 5;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}