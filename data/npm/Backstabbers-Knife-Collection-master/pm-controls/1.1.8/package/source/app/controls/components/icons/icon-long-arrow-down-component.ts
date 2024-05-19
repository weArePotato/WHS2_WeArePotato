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
    selector: 'pm-icon-long-arrow-down',
    //templateUrl: './app/controls/components/svg/icon-long-arrow-down/icon-long-arrow-down.html'
    templateUrl: './icon-long-arrow-down.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconLongArrowDownComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 6;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}