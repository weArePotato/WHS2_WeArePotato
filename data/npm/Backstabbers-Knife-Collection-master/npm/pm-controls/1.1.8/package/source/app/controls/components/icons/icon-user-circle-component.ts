import {
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    Output
} from '@angular/core';
import { Icon } from '../../../objects/icon/icon';

@Component({
    selector: 'pm-icon-user-circle',
    //templateUrl: './app/controls/components/svg/icon-user-circle/icon-user-circle.html'
    templateUrl: './icon-user-circle.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconUserCircleComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 14;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}