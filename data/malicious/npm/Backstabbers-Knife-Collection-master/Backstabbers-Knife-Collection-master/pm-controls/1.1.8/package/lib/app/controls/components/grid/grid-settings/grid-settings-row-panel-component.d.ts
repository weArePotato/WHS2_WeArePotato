import { ChangeDetectorRef, SimpleChanges } from '@angular/core';
import { ClipboardService } from '../../../services/clipboard/clipboard-service';
import { GridComponent } from '../grid-component';
import { ModalDialog } from '../../modal/modal-dialog';
export declare class GridSettingsRowPanelComponent {
    private changeDetectorRef;
    private clipboard;
    constructor(changeDetectorRef: ChangeDetectorRef, clipboard: ClipboardService);
    Grid: GridComponent;
    Dialog: ModalDialog;
    Data: any;
    ngOnChanges(changes: SimpleChanges): void;
    OnAutoGenerate(): void;
    OnCopy(): void;
    OnSave(): void;
    OnClose(): void;
}
