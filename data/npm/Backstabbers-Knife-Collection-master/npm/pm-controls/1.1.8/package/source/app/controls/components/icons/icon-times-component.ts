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
    selector: 'pm-icon-times',
    //templateUrl: './app/controls/components/svg/icon-times/icon-times.html'
    templateUrl: './icon-times.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconTimesComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 11;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}