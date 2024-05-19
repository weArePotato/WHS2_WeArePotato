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
    selector: 'pm-icon-file-text-o',
    //templateUrl: './app/controls/components/svg/icon-file-text-o/icon-text-o.html'
    templateUrl: './icon-file-text-o.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconFileTextOComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 12;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}