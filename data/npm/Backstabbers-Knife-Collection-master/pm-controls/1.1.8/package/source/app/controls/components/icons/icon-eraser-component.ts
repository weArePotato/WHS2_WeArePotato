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
    selector: 'pm-icon-eraser',
    //templateUrl: './app/controls/components/svg/icon-eraser/icon-eraser.html'
    templateUrl: './icon-eraser.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconEraserComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 15;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}