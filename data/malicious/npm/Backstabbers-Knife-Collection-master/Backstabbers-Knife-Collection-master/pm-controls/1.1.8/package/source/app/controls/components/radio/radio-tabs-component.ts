import { NgModule, Component, 
         EventEmitter, Output } from '@angular/core';
import { RadioTabComponent }            from '../radio/radio-tab-component';

@Component({
  selector: 'pm-radio-tabs',
  //templateUrl: './app/controls/components/radio/radio-tabs.html',
  templateUrl: './radio-tabs.html'
})

export class RadioTabsComponent {
  tabs:RadioTabComponent[] = [ ];
  @Output() selected = new EventEmitter();

  addTab(tab: RadioTabComponent) {
    if (this.tabs.length === 0) {
      tab.selected = true;
    }
    this.tabs.push(tab);
  }

  selectTab(tab: RadioTabComponent) {
    this.tabs.map((tab) => {
      tab.selected = false;
    })
    tab.selected = true;
    this.selected.emit({selectedTab: tab});    
  }
}