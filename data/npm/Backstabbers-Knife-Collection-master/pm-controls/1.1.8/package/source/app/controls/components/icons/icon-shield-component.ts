import {
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    Output
} from '@angular/core';
import { Icon } from '../../../objects/icon/icon';

@Component({
    selector: 'pm-icon-shield',
    //templateUrl: './app/controls/components/svg/icon-shield/icon-shield.html'
    templateUrl: './icon-shield.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconShieldComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 10;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}