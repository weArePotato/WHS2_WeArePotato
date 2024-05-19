import {
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    Output
} from '@angular/core';
import { Icon } from '../../../objects/icon/icon';

@Component({
    selector: 'pm-icon-left-arrow',
    //templateUrl: './app/controls/components/svg/icon-left-arrow/icon-left-arrow.html'
    templateUrl: './icon-left-arrow.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconLeftArrowComponent extends Icon {
    OriginalHeight = 20;
    OriginalWidth = 20;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}