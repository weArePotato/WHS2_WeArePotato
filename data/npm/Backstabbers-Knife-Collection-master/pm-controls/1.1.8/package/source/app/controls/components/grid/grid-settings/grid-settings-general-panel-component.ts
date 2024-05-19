import { 
    ChangeDetectorRef,
    Component, 
    Input
} from '@angular/core';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { ModalDialog } from '../../../../controls/components/modal/modal-dialog';

@Component({
    selector: 'pm-grid-settings-general-panel',
    //templateUrl: './app/controls/components/grid/grid-settings/grid-settings-general-panel.html',
    templateUrl: './grid-settings-general-panel.html'
})
export class GridSettingsGeneralPanelComponent  {
    constructor(private changeDetectorRef: ChangeDetectorRef) {
        changeDetectorRef.detach();
    }

    private grid: GridComponent;
    @Input('Grid')
    get Grid(): GridComponent {
        return this.grid;
    }
  
    set Grid(value: GridComponent) {
        this.grid = value;
        this.CurrentGrid =
        {
            "ColumnHeaderHeight": value.ColumnHeaderHeight,
            "FrozenColumnCount": value.FrozenColumnCount,
            "HierarchyColumnIndex": value.HierarchyColumnIndex,
            "HierarchyColumnProperty": value.HierarchyColumnProperty,
            "ShowFooter": value.ShowFooter,
            "ShowRowNumbers": value.ShowRowNumbers,
            "ShowColumnGroups": value.ShowColumnGroups,
            "RowHeight": value.RowHeight            
        }

        this.changeDetectorRef.detectChanges();
    }

    @Input() Dialog: ModalDialog;
    CurrentGrid;    
    TopHeightPx;
    TransformY;

    OnSave() {
        this.Grid.ColumnHeaderHeight = this.CurrentGrid.ColumnHeaderHeight;
        this.Grid.FrozenColumnCount = this.CurrentGrid.FrozenColumnCount;
        this.Grid.HierarchyColumnIndex = this.CurrentGrid.HierarchyColumnIndex;
        this.Grid.HierarchyColumnProperty = this.CurrentGrid.HierarchyColumnProperty;
        this.Grid.ShowFooter = this.CurrentGrid.ShowFooter;
        this.Grid.ShowColumnGroups = this.CurrentGrid.ShowColumnGroups;
        this.Grid.ShowRowNumbers = this.CurrentGrid.ShowRowNumbers;
        this.Grid.RowHeight = this.CurrentGrid.RowHeight;
        this.Grid.RaiseChange();
    }

    OnClose() {
        this.Dialog.Close(false);
    }
}