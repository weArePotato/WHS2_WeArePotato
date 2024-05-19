import { ModalDialog } from '../../../../controls/components/modal/modal-dialog';
import { ContextMenuComponent } from '../../../../controls/components/context-menu/context-menu-component';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { ListBoxComponent } from '../../../../controls/components/boxes/list-box/list-box-component';
import { Column } from '../../../../objects/request/column';
export declare class ColumnFilterPopup extends ModalDialog {
    constructor();
    ContextMenu: ContextMenuComponent;
    Grid: GridComponent;
    ColumnFilter: any;
    ColumnFilterSearchOptions: Array<any>;
    SelectedColumnFilterSearchOption: any;
    listBox: ListBoxComponent;
    Column: Column;
    private columnFilterDistinctItems;
    ColumnFilterDistinctItems: Array<any>;
    private selectedColumnFilterDistinctItems;
    SelectedColumnFilterDistinctItems: Array<any>;
    onClick(event: any): void;
    InitializeFilters(): void;
    OnHideColumn(): void;
    OnSortAscendingColumn(): void;
    OnSortDescendingColumn(): void;
    OnClearFilter(): void;
    OnSetFilter(): void;
    OnColumnSetSize(column: Column): void;
    OnDistinctColumnFilter(column: Column): void;
    SetFilterOptions(): void;
    IsChecked(item: any): boolean;
    GetDistinctItems(column: Column): any[];
    GetItemsSortedByDataType(items: Array<any>): any[];
    SetDistinctItems(column: Column): void;
    SortByNumber(a: any, b: any): number;
    SortByDateAscending(a: any, b: any): number;
    static Show(event: MouseEvent, grid: GridComponent, column: Column): void;
}
