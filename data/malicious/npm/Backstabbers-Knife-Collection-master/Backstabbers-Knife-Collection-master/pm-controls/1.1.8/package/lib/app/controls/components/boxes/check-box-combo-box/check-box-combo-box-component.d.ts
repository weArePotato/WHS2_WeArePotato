import { ChangeDetectorRef, EventEmitter, OnInit, SimpleChanges, ViewContainerRef, IterableDiffers, IterableDiffer } from '@angular/core';
import { SelectionMode } from '../../../../objects/enums/selection-mode';
import { ComboBoxComponent } from '../combo-box/combo-box-component';
export declare class CheckBoxComboBoxComponent implements OnInit {
    changeDetectorRef: ChangeDetectorRef;
    viewContainerRef: ViewContainerRef;
    private _iterableDiffers;
    iterableDiffer: IterableDiffer<{}>;
    Watermark: string;
    DisplayMemberPath: any;
    SelectionMode: SelectionMode;
    SelectedItemsChange: EventEmitter<any>;
    IsDisabled: boolean;
    comboBox: ComboBoxComponent;
    constructor(changeDetectorRef: ChangeDetectorRef, viewContainerRef: ViewContainerRef, _iterableDiffers: IterableDiffers);
    ngOnInit(): void;
    ngOnChanges(changes: SimpleChanges): void;
    ngDoCheck(): void;
    OnUncheckAllClick(): void;
    OnCheckAllClick(): void;
    IsCheckedChange(): void;
    IsChecked(item: any): boolean;
    private itemsSource;
    ItemsSource: any;
    private selectedItems;
    SelectedItems: any;
}
