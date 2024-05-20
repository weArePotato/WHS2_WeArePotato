import {
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    Output
} from '@angular/core';
import { Icon } from '../../../objects/icon/icon';

@Component({
    selector: 'pm-icon-ellipsis-v',
    //templateUrl: './app/controls/components/svg/icon-ellipsis-v/icon-ellipsis-v.html'
    templateUrl: './icon-ellipsis-v.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconEllipsisVComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 14;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}