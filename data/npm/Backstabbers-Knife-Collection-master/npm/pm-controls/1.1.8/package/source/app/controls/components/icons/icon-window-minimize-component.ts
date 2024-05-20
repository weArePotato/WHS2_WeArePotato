import {
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    Output
} from '@angular/core';
import { Icon } from '../../../objects/icon/icon';

@Component({
    selector: 'pm-icon-window-minimize',
    //templateUrl: './app/controls/components/svg/icon-window-minimize/icon-window-minimize.html'
    templateUrl: './icon-window-minimize.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconWindowMinimizeComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 14;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}