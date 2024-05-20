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
    selector: 'pm-icon-address-card',
   // templateUrl: './app/controls/components/icons/icon-address-card.html',
    templateUrl: './icon-address-card.html',
    //templateUrl: './icon-address-card.html'),
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconAddressCardComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 16;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}