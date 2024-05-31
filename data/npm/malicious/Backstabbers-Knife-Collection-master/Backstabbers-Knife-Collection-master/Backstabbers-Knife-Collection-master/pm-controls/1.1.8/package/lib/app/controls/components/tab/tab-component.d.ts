import { ChangeDetectorRef, OnInit } from '@angular/core';
import { TabsComponent } from '../tabs/tabs-component';
export declare class TabComponent implements OnInit {
    private tabs;
    private changeDetectorRef;
    constructor(tabs: TabsComponent, changeDetectorRef: ChangeDetectorRef);
    Name: string;
    Height: any;
    private isSelected;
    IsSelected: boolean;
    ngOnInit(): void;
    readonly TabHeaderHeight: string;
}
