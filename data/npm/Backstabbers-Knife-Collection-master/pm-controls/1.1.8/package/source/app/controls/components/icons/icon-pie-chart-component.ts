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
    selector: 'pm-icon-pie-chart',
    //templateUrl: './app/controls/components/svg/icon-pie-chart/icon-pie-chart.html'
    templateUrl: './icon-pie-chart.html',
    styles: [`
    :host { 
      display: flex;
      align-items: center;
    }
    `],
})
export class IconPieChartComponent extends Icon {
    OriginalHeight = 14;
    OriginalWidth = 13;

    get Height(): number {
        return this.OriginalHeight * this.IconSize;
    }

    get Width(): number {
        return this.OriginalWidth * this.IconSize;
    }
}