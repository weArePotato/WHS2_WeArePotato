import {
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    Output
} from '@angular/core';
import { Icon } from '../../../objects/icon/icon';

@Component({
    selector: 'pm-icon-right-arrow',
    //templateUrl: './app/controls/components/svg/icon-right-arrow/icon-right-arrow.html'
    templateUrl: './icon-right-arrow.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconRightArrowComponent extends Icon {
    OriginalHeight = 20;
    OriginalWidth = 20;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}