import { 
  Component
} from '@angular/core';
import { ModalDialog } from '../../../../controls/components/modal/modal-dialog';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { ControlsModule } from '../../../../controls/controls-module';
        

@Component({
  //templateUrl: './app/controls/components/grid/grid-settings-dialog.html',
  templateUrl: './grid-settings-dialog.html',
  styles: [`
    :host {   
      position: absolute;
      height: 100%;
      width: 100%;
      top: 0px;
      z-index: 1000;
      pointer-events: none;
    }
  `]
})
export class GridSettingsDialog extends ModalDialog {   
  constructor() {
    super();
    this.Header = 'Grid Settings';

    this.ItemsSource = 
    [
      { Name:'General' },
      { Name:'Columns' },
      { Name:'ColumnGroups' },
      { Name:'Rows' }
    ];

    this.SelectedItem = this.ItemsSource[0];
  }

  Grid: GridComponent;

  get Dialog(): ModalDialog {
    return this;
  }

  ItemsSource;
  SelectedItem;

  static Show(grid: GridComponent) {
    var dialog = <GridSettingsDialog> ControlsModule.dialog.Show(GridSettingsDialog);
    dialog.Grid = grid;
  }
}