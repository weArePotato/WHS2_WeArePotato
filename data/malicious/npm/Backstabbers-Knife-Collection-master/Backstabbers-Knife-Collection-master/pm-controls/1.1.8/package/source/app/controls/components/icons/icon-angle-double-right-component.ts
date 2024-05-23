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
    selector: 'pm-icon-angle-double-right',
    //templateUrl: './app/controls/components/svg/icon-angle-double-right/icon-angle-double-right.html'
    templateUrl: './icon-angle-double-right.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconAngleDoubleRightComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 8;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}