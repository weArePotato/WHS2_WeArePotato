import { Component, 
         Input,
         OnInit, 
         Output,
         EventEmitter,
         ViewContainerRef,
         ViewChild,
         TemplateRef,
        SimpleChanges }     from '@angular/core';

@Component({
    selector: 'pm-tree-item',
    //templateUrl: './app/controls/components/tree/tree-item.html',
    templateUrl: './tree-item.html'
})
export class TreeItemComponent {
    @Input() ItemsSource: Array<any>;
    @Input() ItemTemplate: TemplateRef<any>;
    @Input() SelectedItems: Array<any> = [];
    @Input() SelectedItem: any;
    @Input() DisplayMemberPath: any; // should be property name or function.
    @Input() ChildPath: any; // should be property name or function.
    @Input() SelectionMode: string = "SelectionMode.Single"; 
    @Output() SelectedItemsChange: EventEmitter<any> = new EventEmitter<any>();
    @Output() SelectedItemChange: EventEmitter<any> = new EventEmitter<any>();

    OnClick(item: any) {
        item._isExpanded = !item._isExpanded;
        //this.IsExpanded = !this.IsExpanded;
    }

    HasChildren(item) : boolean {
        if (!item)
            return false;

        if (!this.ChildPath)
            return false;

        var items = <Array<any>> item[this.ChildPath];
        return items && items.length > 0;
    }

    GetChildren(item) : Array<any> {
        if (!item)
            return;

        if (!this.ChildPath)
            return;

        return item[this.ChildPath];
    }
}