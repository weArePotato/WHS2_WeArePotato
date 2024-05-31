import { OnInit } from '@angular/core';
import { RadioTabsComponent } from '../radio/radio-tabs-component';
export declare class RadioTabComponent implements OnInit {
    private tabs;
    Name: string;
    selected: boolean;
    constructor(tabs: RadioTabsComponent);
    ngOnInit(): void;
}
