import {
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    Output
} from '@angular/core';
import { Icon } from '../../../objects/icon/icon';

@Component({
    selector: 'pm-icon-refresh',
    //templateUrl: './app/controls/components/svg/icon-refresh/icon-refresh.html'
    templateUrl: './icon-refresh.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconRefreshComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 12;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}