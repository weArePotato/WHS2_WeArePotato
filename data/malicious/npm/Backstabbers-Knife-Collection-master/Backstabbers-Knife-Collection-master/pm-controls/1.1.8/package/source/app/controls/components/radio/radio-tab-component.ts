import { Component, Input, OnInit } from '@angular/core';

import { RadioTabsComponent }            from '../radio/radio-tabs-component';

@Component({
  selector: 'pm-radio-tab',
  //templateUrl: './app/controls/components/radio/radio-tab.html'
  templateUrl: './radio-tab.html'
})

export class RadioTabComponent implements OnInit {
  @Input() Name: string;
  @Input() selected: boolean;

  constructor(private tabs: RadioTabsComponent) {}
  
  ngOnInit() {
    this.tabs.addTab(this);
  }
 }