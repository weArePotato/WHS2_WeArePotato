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
    selector: 'pm-icon-angle-double-left',
   // templateUrl: './app/controls/components/svg/icon-angle-double-left/icon-angle-double-left.html',
    templateUrl: './icon-angle-double-left.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconAngleDoubleLeftComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 8;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}