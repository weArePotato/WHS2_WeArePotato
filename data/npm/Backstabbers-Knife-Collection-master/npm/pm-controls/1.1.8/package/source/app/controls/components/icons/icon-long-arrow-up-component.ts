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
    selector: 'pm-icon-long-arrow-up',
    //templateUrl: './app/controls/components/svg/icon-long-arrow-up/icon-long-arrow-up.html'
    templateUrl: './icon-long-arrow-up.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconLongArrowUpComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 6;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}