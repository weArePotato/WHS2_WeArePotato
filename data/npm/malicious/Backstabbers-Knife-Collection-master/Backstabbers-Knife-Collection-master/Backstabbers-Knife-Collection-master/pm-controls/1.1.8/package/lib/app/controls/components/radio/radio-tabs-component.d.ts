import { EventEmitter } from '@angular/core';
import { RadioTabComponent } from '../radio/radio-tab-component';
export declare class RadioTabsComponent {
    tabs: RadioTabComponent[];
    selected: EventEmitter<{}>;
    addTab(tab: RadioTabComponent): void;
    selectTab(tab: RadioTabComponent): void;
}
