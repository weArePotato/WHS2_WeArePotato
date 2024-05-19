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
    selector: 'pm-icon-pencil',
    //templateUrl: './app/controls/components/svg/icon-pencil/icon-pencil.html'
    templateUrl: './icon-pencil.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconPencilComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 12;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}