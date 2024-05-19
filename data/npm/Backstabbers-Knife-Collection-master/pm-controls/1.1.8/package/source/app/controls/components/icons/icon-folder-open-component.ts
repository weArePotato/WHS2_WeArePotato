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
    selector: 'pm-icon-folder-open',
    //templateUrl: './app/controls/components/svg/icon-folder-open/icon-folder-open.html'
    templateUrl: './icon-folder-open.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconFolderOpenComponent extends Icon {
    OriginalHeight = 16;
    OriginalWidth = 16;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}