import { Component,
         Input }     from '@angular/core';

@Component({
  selector: 'pm-grid-panel',
  //templateUrl: './app/controls/components/panel/grid-panel/grid-panel.html',
  templateUrl: './grid-panel.html'
})
export class GridPanelComponent { 
    @Input() HeightPx: any;
    @Input() WidthPx: any;
}