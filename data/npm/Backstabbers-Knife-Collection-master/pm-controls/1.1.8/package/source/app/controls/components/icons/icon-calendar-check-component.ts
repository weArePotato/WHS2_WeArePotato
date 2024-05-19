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
    selector: 'pm-icon-calendar-check',
    //templateUrl: './app/controls/components/svg/icon-calendar-check/icon-calendar-check.html'
    templateUrl: './icon-calendar-check.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconCalendarCheckComponent extends Icon {
    OriginalHeight = 16;
    OriginalWidth = 16;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}