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
    selector: 'pm-icon-cubes',
    //templateUrl: './app/controls/components/svg/icon-cubes/icon-cubes.html'
    templateUrl: './icon-cubes.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconCubesComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 17;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}