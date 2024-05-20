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
    selector: 'pm-icon-calendar',
    //templateUrl: './app/controls/components/svg/icon-calendar/icon-calendar.html'
    templateUrl: './icon-calendar.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconCalendarComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 13;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}