import { EventEmitter } from '@angular/core';
import { TextBoxComponent } from '../text-box/text-box-component';
export declare class MultiSelectTextBoxComponent {
    IsDisabled: boolean;
    Watermark: string;
    Text: string;
    SelectedItems: Array<any>;
    SelectedItemsChange: EventEmitter<any>;
    ShowRemoveItem: boolean;
    textBox: TextBoxComponent;
    MultiSelectTextBoxClass: string;
    MultiSelectTextBoxButtonClass: string;
    MultiSelectTextBoxSelectedItemsClass: string;
    Width: any;
    MultiSelectTextBoxPanelClass: any;
    AddClick(): void;
    RemoveSelectedItem(item: any): void;
    OnKeyUp(event: any): void;
}
