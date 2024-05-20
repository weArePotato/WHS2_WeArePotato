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
    selector: 'pm-icon-cloud',
    //templateUrl: './app/controls/components/svg/icon-cloud/icon-cloud.html'
    templateUrl: './icon-cloud.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconCloudComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 15;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}