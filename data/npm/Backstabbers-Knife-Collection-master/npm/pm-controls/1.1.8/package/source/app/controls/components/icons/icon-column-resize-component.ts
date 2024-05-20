import {
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    Output
} from '@angular/core';
import { Icon } from '../../../objects/icon/icon';

@Component({
    selector: 'pm-icon-column-resize',
    //templateUrl: './app/controls/components/svg/icon-column-resize/icon-column-resize.html'
    templateUrl: './icon-column-resize.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconColumnResizeComponent extends Icon {
    OriginalHeight = 16;
    OriginalWidth = 16;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}