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
    selector: 'pm-icon-search-minus',
    //templateUrl: './app/controls/components/svg/icon-search-minus/icon-search-minus.html'
    templateUrl: './icon-search-minus.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconSearchMinusComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 13;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}