import { Component, Input,
         OnInit, Output,
         EventEmitter,
         ViewContainerRef,
         ViewChild,
         TemplateRef,
         SimpleChanges }    from '@angular/core';

@Component({
  selector: 'pm-tree',
  //templateUrl: './app/controls/components/tree/tree.html',
  templateUrl: './tree.html'
})
export class TreeComponent {
  @Input() ItemsSource: Array<any>;
  @Input() ItemTemplate: TemplateRef<any>;
  @Input() SelectedItems: Array<any> = [];
  @Input() SelectedItem: any;
  @Input() DisplayMemberPath: any; // should be property name or function.
  @Input() ChildPath: any;
  @Input() SelectionMode: string = "SelectionMode.Single"; 
  @Output() SelectedItemsChange: EventEmitter<any> = new EventEmitter<any>();
  @Output() SelectedItemChange: EventEmitter<any> = new EventEmitter<any>();

  getItemDisplay(item) :string {
    if (!item)
      return;
            
    if (!this.DisplayMemberPath)
      return item;
    
    if(typeof this.DisplayMemberPath === "function")
      return this.DisplayMemberPath(item);
    else if (item[this.DisplayMemberPath])
      return <string>item[this.DisplayMemberPath];
    return item;
  }
}