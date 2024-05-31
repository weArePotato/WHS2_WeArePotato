import { ChangeDetectorRef, ElementRef, EventEmitter } from '@angular/core';
import { TabComponent } from '../tab/tab-component';
export declare class TabsComponent extends ElementRef {
    private element;
    private changeDetectorRef;
    constructor(element: ElementRef, changeDetectorRef: ChangeDetectorRef);
    Tabs: TabComponent[];
    TabsClass: string;
    SelectedTabIndex: number;
    SelectedTabIndexChange: EventEmitter<{}>;
    Selected: EventEmitter<{}>;
    TabHeaderHeight: string;
    AddTab(tab: TabComponent): void;
    SelectTab(tab: TabComponent): void;
}
