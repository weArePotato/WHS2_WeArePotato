import { EventEmitter, TemplateRef } from '@angular/core';
export declare class TreeComponent {
    ItemsSource: Array<any>;
    ItemTemplate: TemplateRef<any>;
    SelectedItems: Array<any>;
    SelectedItem: any;
    DisplayMemberPath: any;
    ChildPath: any;
    SelectionMode: string;
    SelectedItemsChange: EventEmitter<any>;
    SelectedItemChange: EventEmitter<any>;
    getItemDisplay(item: any): string;
}
