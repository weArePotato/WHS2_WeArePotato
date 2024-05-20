import { EventEmitter, TemplateRef } from '@angular/core';
export declare class TreeItemComponent {
    ItemsSource: Array<any>;
    ItemTemplate: TemplateRef<any>;
    SelectedItems: Array<any>;
    SelectedItem: any;
    DisplayMemberPath: any;
    ChildPath: any;
    SelectionMode: string;
    SelectedItemsChange: EventEmitter<any>;
    SelectedItemChange: EventEmitter<any>;
    OnClick(item: any): void;
    HasChildren(item: any): boolean;
    GetChildren(item: any): Array<any>;
}
