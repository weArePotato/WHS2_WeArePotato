import { 
  ChangeDetectorRef,
  Component, 
  Input, 
  OnInit }               from '@angular/core';

import { TabsComponent } from '../tabs/tabs-component';

@Component({
  selector: 'pm-tab',
  //templateUrl: './app/controls/components/tab/tab.html',
  templateUrl: './tab.html'
})

export class TabComponent implements OnInit {
 
  constructor(private tabs: TabsComponent, private changeDetectorRef: ChangeDetectorRef) {}

  @Input() Name: string;
  @Input() Height: any;

  private isSelected: boolean;
  @Input('IsSelected')
  get IsSelected(): boolean {
    return this.isSelected;
  }

  set IsSelected(value: boolean) {
    this.isSelected = value;
    this.changeDetectorRef.detectChanges();
  }

  ngOnInit() {
    this.tabs.AddTab(this);
  }

  get TabHeaderHeight() {
    return "calc(100% - " + this.tabs.TabHeaderHeight + "px)";    
  }
 }