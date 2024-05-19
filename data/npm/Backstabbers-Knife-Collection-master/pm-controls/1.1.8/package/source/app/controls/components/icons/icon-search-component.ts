import {
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    Output
} from '@angular/core';
import { Icon } from '../../../objects/icon/icon';

@Component({
    selector: 'pm-icon-search',
    //templateUrl: './app/controls/components/svg/icon-search/icon-search.html'
    templateUrl: './icon-search.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconSearchComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 13;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}