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
    selector: 'pm-icon-search-plus',
    //templateUrl: './app/controls/components/svg/icon-search-plus/icon-search-plus.html'
    templateUrl: './icon-search-plus.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconSearchPlusComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 13;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}