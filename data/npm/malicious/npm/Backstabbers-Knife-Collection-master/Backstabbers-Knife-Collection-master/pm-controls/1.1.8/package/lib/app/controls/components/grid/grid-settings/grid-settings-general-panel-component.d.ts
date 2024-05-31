import { ChangeDetectorRef } from '@angular/core';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { ModalDialog } from '../../../../controls/components/modal/modal-dialog';
export declare class GridSettingsGeneralPanelComponent {
    private changeDetectorRef;
    constructor(changeDetectorRef: ChangeDetectorRef);
    private grid;
    Grid: GridComponent;
    Dialog: ModalDialog;
    CurrentGrid: any;
    TopHeightPx: any;
    TransformY: any;
    OnSave(): void;
    OnClose(): void;
}
