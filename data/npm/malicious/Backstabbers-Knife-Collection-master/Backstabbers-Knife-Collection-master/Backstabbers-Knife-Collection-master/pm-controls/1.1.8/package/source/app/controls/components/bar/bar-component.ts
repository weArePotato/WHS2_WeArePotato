import { Component, Input, Output, EventEmitter }       from '@angular/core';

@Component({
  selector: 'pm-bar',
  //templateUrl: './app/controls/components/bar/bar.html',
  templateUrl: './bar.html',
  // styles: [`
  // :host { 
  //   z-index: 5;
  // }
  // `],
})
export class BarComponent {
  @Input() Name = '';
  @Input() Items;
  title: string;

  @Output() onExportToExcel = new EventEmitter();
  @Output() onTogglePanel = new EventEmitter();

  exportToExcel() {
    this.onExportToExcel.emit({});
  }

  togglePanel() {
    this.onTogglePanel.emit({});
  }
}