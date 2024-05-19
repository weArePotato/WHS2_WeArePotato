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
    selector: 'pm-icon-arrows',
    //templateUrl: './app/controls/components/svg/icon-arrows/icon-arrows.html'
    templateUrl: './icon-arrows.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconArrowsComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 14;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}