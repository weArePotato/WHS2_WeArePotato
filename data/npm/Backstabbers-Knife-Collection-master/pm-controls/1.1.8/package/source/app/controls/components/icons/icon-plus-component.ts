import {
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    Output
} from '@angular/core';
import { Icon } from '../../../objects/icon/icon';

@Component({
    selector: 'pm-icon-plus',
    //templateUrl: './app/controls/components/svg/icon-plus/icon-plus.html'
    templateUrl: './icon-plus.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconPlusComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 11;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}