import { 
  ChangeDetectorRef, 
  Component,
  ElementRef,
  EventEmitter,
  Input,
  OnInit, 
  Output 
} from '@angular/core';

import { CommonModule }  from "@angular/common";

import { TabComponent }  from '../tab/tab-component';

@Component({
  selector: 'pm-tabs',
  //templateUrl: './app/controls/components/tabs/tabs.html',
  templateUrl: './tabs.html'
})
export class TabsComponent extends ElementRef {
  constructor(
    private element: ElementRef,
    private changeDetectorRef: ChangeDetectorRef) {
    super(element.nativeElement);
  }
  Tabs:TabComponent[] = [ ];
  
  @Input() TabsClass: string;
  @Input() SelectedTabIndex: number = 0;
  @Output() SelectedTabIndexChange = new EventEmitter();
  @Output() Selected = new EventEmitter();
  @Input() TabHeaderHeight = "40";
  
  AddTab(tab: TabComponent) {    
    this.Tabs.push(tab);
    if (this.Tabs.indexOf(tab) == this.SelectedTabIndex)
      tab.IsSelected = true;
  }

  SelectTab(tab: TabComponent) {
    this.Tabs.map((tab) => {
      tab.IsSelected = false;
    })
    tab.IsSelected = true;
    this.Selected.emit({selectedTab: tab});
    this.SelectedTabIndex = this.Tabs.indexOf(tab);
    this.SelectedTabIndexChange.emit(this.SelectedTabIndex);    
    this.changeDetectorRef.detectChanges();
  }
}