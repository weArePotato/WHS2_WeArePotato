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
    selector: 'pm-icon-angle-right',
    //templateUrl: './app/controls/components/svg/icon-angle-right/icon-angle-right.html'
    templateUrl: './icon-angle-right.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconAngleRightComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 5;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}