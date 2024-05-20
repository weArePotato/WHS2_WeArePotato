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
    selector: 'pm-icon-times-circle',
    //templateUrl: './app/controls/components/svg/icon-times-circle/icon-times-circle.html'
    templateUrl: './icon-times-circle.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconTimesCircleComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 12;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}