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
    selector: 'pm-icon-cogs',
    //templateUrl: './app/controls/components/svg/icon-cogs/icon-cogs.html'
    templateUrl: './icon-cogs.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconCogsComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 15;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}