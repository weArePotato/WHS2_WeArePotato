import { 
  ChangeDetectorRef,
  ChangeDetectionStrategy,
  Component, 
  Input,
  OnInit, 
  Output,
  EventEmitter,
  ViewContainerRef,
  ViewChild,
  TemplateRef,
  SimpleChanges
} from '@angular/core';
import { VirtualPanelComponent } from '../../panels/virtual-panel/virtual-panel-component';

@Component({
  selector: 'pm-list-box',
  //templateUrl: './app/controls/components/boxes/list-box/list-box.html',
  templateUrl: './list-box.html',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ListBoxComponent implements OnInit {
  constructor(
    public changeDetectorRef: ChangeDetectorRef) {
      this.changeDetectorRef.detach();
  }

  @Input() ListBoxClass: string = "list-box-container-border";
  @Input() ListBoxItemClass: string = "list-box-item";
  @Input() LastListBoxItemClass: string = "last-list-box-item";  
  @Input() ListBoxSelectedItemClass: string = "list-box-list-item-selected";
  @Input() ListBoxItemBackgroundClass: string;
  @Input() ListBoxBorderClass: string = "list-box-border";
  @Input() ItemHeight: number = 30;
  @Input() ControlHeight: any;
  @Input() ControlWidth: any;
  @Input() SelectedItem: any;
  @Input() DisplayMemberPath: any; // should be property name or function.
  @Input() ItemTemplate: TemplateRef<any>;
  @Input() SelectionMode: string = "SelectionMode.Single"; 
  @Output() SelectedItemsChange: EventEmitter<any> = new EventEmitter<any>();
  @Output() SelectedItemChange: EventEmitter<any> = new EventEmitter<any>(); 
  @ViewChild('virtualPanel') virtualPanel: VirtualPanelComponent;

  moveItemIntoViewFunc: Function;
  @Input() filteredItemSource: any;
  private highlightedItem: any;

  private itemsSource: Array<any> = [];
  @Input('ItemsSource')
  get ItemsSource(): Array<any> {
    return this.itemsSource;
  }
  
  set ItemsSource(value: Array<any>) {
    this.itemsSource = value;
  }

  private selectedItems: Array<any> = [];
  @Input('SelectedItems')
  get SelectedItems(): Array<any> {
    return this.selectedItems;
  }
  
  set SelectedItems(value: Array<any>) {
    this.selectedItems = value;
  }

  ngOnInit() { 
    this.filterItemSource();
    if (this.SelectedItem)
      this.SelectItem(this.SelectedItem);
    this.changeDetectorRef.detectChanges();
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes['ItemsSource']) {
        this.filterItemSource();
    }
  }

  filterItemSource() {
    this.filteredItemSource = this.ItemsSource;    
    this.changeDetectorRef.detectChanges();
  }

  UpdateSelectedItem() {
    this.SelectedItem = this.SelectedItems.length>0? this.SelectedItems[0]:null;
    this.SelectedItemChange.emit(this.SelectedItem);    
  }

  isLastItem(item: any) : boolean {
    return item === this.filteredItemSource[this.filteredItemSource.length - 1];
  }

  getItemDisplay(item) :string {
    if (!item)
      return;
            
    if (!this.DisplayMemberPath)
      return item;
    
    if(typeof this.DisplayMemberPath === "function")
      return this.DisplayMemberPath(item);
    else
      return <string>item[this.DisplayMemberPath];
  }

  SelectItem(item: any) {
    if (this.SelectionMode == "SelectionMode.Single") 
      this.SelectedItems.length = 0;

    // only include unique items.
    if(this.SelectedItems.indexOf(item)==-1)
      this.SelectedItems.push(item);
    else {
      // remove the item if it's already selected
      this.removeSelectedItem(item);
      this.UpdateSelectedItem();
      return;
    }

    this.UpdateSelectedItem();
    this.SelectedItemsChange.emit(this.SelectedItems);
    this.virtualPanel.RaiseChange();
  }

  removeSelectedItem(item:any) {
    var idx = this.SelectedItems.indexOf(item);
    if(idx<0) {
      console.error("Could not find selected item to remove.");
      console.trace();
      return;
    }
    this.SelectedItems.splice(idx,1);
    this.UpdateSelectedItem();    
    this.SelectedItemsChange.emit(this.SelectedItems);    
  }
}