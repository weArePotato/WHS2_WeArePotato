import { ModalDialog } from '../../../../controls/components/modal/modal-dialog';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
export declare class GridSettingsDialog extends ModalDialog {
    constructor();
    Grid: GridComponent;
    readonly Dialog: ModalDialog;
    ItemsSource: any;
    SelectedItem: any;
    static Show(grid: GridComponent): void;
}
