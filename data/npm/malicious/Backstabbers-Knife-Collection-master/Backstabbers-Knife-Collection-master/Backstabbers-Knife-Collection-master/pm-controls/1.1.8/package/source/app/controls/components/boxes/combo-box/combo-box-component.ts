import {
  ChangeDetectionStrategy, 
  ChangeDetectorRef,
  Component,   
  EventEmitter,
  Input,
  OnInit,
  OnDestroy,   
  Output, 
  SimpleChanges, 
  TemplateRef,
  ViewContainerRef,
  ViewChild
} from '@angular/core';

import { CompatibilityService } from '../../../services/compatibility/compatibility-service';
import { SelectionMode } from '../../../../objects/enums/selection-mode';
import { TextBoxComponent } from '../text-box/text-box-component';
import { VirtualPanelComponent } from '../../panels/virtual-panel/virtual-panel-component';
import { StringExtensions } from '../../../../objects/extensions/string-extensions';
import { KeyCodes } from '../../../../objects/key-codes';
import { ArrayExtensions } from '../../../../objects/extensions/array-extensions';

@Component({
  selector: 'pm-combo-box',
  //templateUrl: './app/controls/components/boxes/combo-box/combo-box.html',
  templateUrl: './combo-box.html',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ComboBoxComponent implements OnInit, OnDestroy {  
  constructor(
    public changeDetectorRef: ChangeDetectorRef,
    public viewContainerRef: ViewContainerRef,
    public CompatibilityService: CompatibilityService) {
      if(this.CompatibilityService.IsLegacyBrowser)
        this.DropDownWidth = "";
      this.changeDetectorRef.detach();
      this.el = viewContainerRef.element.nativeElement;
      this.clickEvent = this.HandleClick.bind(this);
  }
  
  @Input() Label;
  @Input() ComboBoxItemClass: string = "combo-box-item";
  @Input() ComboBoxPanelClass: string = "combo-box-panel-default";
  @Input() ComboBoxButtonClass: string = "button-icon-default";
  @Input() ItemHeight: number = 30; 
  @Input() Watermark: string;
  @Input() Width: string;
  @Input() IsBusy: boolean;
  @Input() IsDisabled: boolean;
  @Input() IsReadOnly: boolean;
  @Input() ShowRemoveItem: boolean = true;
  @Input() IsDropDownOpen: boolean;
  @Output() IsDropDownOpenChange: EventEmitter<boolean> = new EventEmitter();
  @Input() SelectionMode: SelectionMode = SelectionMode.Single; 
  @Input() ShowClearButton: boolean = true;
  @Input() ItemsSource: Array<any>;
  @Input() SelectedItems: Array<any> = [];  
  @Input() DisplayMemberPath: any; // should be property name or function.
  @Output() SelectedItemsChange: EventEmitter<any> = new EventEmitter<any>();
  @Output() SelectedItemChange: EventEmitter<any> = new EventEmitter<any>();  
  @Output() TextChange: EventEmitter<string> = new EventEmitter<string>();
  @ViewChild(TextBoxComponent) textBox: TextBoxComponent;
  @Input() ItemTemplate: TemplateRef<any>;
  @Input() ComboBoxListItemSelectedClass: string = "combo-box-list-item-selected";
  @Input() ShowHighlight: boolean = true;
  @Input() HighlightedItem: any;
  @ViewChild('virtualPanel') virtualPanel: VirtualPanelComponent;

  DropDownWidth : string = "100%";

  public filteredItemSource: any;
  private el: Element;  
  private clickEvent;

  ngOnInit() {
    this.IsDropDownOpen = this.IsDropDownOpen || false;
    this.IsDropDownOpenChange.emit(this.IsDropDownOpen);

    this.filterItemSource();

    let body = document.querySelector('body');
    body.addEventListener('click', this.clickEvent, false);
  }

  private text: any;
  @Input('Text')
  get Text(): any {
    return this.text;
  }

  set Text(value: any) {
    if (this.text != value){
      this.text = value;
      this.TextChange.emit(this.text);
      this.changeDetectorRef.detectChanges();
    }
  }

  private selectedItem: any;
  @Input('SelectedItem')
  get SelectedItem(): any {
    return this.selectedItem;
  }

  set SelectedItem(value: any) {
    this.selectedItem = value;
    
    if (this.SelectionMode == SelectionMode.Single)
      this.SelectedItems.length = 0;

    if (this.selectedItem && this.SelectedItems.indexOf(this.selectedItem) == -1)
      this.SelectedItems.push(this.selectedItem);
    
    if (this.SelectionMode == SelectionMode.Single)
      this.IsDropDownOpen = false;
    else 
      this.SelectedItemsChange.emit(this.SelectedItems);

    this.Text = "";
    this.TextChange.emit(this.Text);
    this.filterItemSource();
    this.SelectedItemChange.emit(this.SelectedItem);
  }

  SelectItem(item: any) {
    if (!this.SelectedItems) this.SelectedItems = [];
    if (this.SelectedItems.indexOf(item) == -1)
      this.SelectedItem = item;
    else {
      this.RemoveSelectedItem(item);
    }
    this.changeDetectorRef.detectChanges();
  }

  ngOnDestroy() {
    let body = document.querySelector('body');
    body.removeEventListener('click', this.clickEvent, false);
  }

  HandleClick(e) {
    if (!this.IsDropDownOpen || !e.target) { return; };
    if (this.el !== e.target && !this.el.contains((<any>e.target))) {
      this.IsDropDownOpen = false;
      this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
      this.virtualPanel.ResetScroll();
      this.changeDetectorRef.detectChanges();
    }
  }

  get AllSelected(): boolean {
    if (this.SelectedItems && this.ItemsSource && this.ItemsSource.length > 1)
      return this.ItemsSource.every(r => this.SelectedItems.includes(r));
    return false;
  }

  highlight() {
    if (this.filteredItemSource && this.filteredItemSource.length > 0)
    {
      this.HighlightedItem = this.filteredItemSource[0];
    }
  }
  
  filterItemSource() {
    if(this.Text) {
      var lowerCaseText = this.Text.toLowerCase();
      this.filteredItemSource = this.ItemsSource.filter(item => this.getItemDisplay(item).toLowerCase().indexOf(lowerCaseText)!=-1); 
    }
    else {
      this.filteredItemSource = this.ItemsSource;
    }

    this.highlight();
    this.changeDetectorRef.detectChanges();
  }

  OnClickClear() {
    this.IsDropDownOpen = false;
    this.Clear();
  }

  Clear() {
    this.SelectedItems.length = 0;
    this.SelectedItem = undefined;    
    this.changeDetectorRef.detectChanges();
  }

  SelectAll() {
    this.SelectedItems = this.ItemsSource.slice();
    this.SelectedItemsChange.emit(this.SelectedItems);
    this.changeDetectorRef.detectChanges();
  }

  get WatermarkDisplay() {
    if (this.SelectedItem || (this.SelectedItems && this.SelectedItems.length > 0))
      return;
    return this.Watermark;
  }

  RemoveSelectedItem(item:any) {
    var idx = this.SelectedItems.indexOf(item);
    if(idx<0) {
      console.error("Could not find selected item to remove.");
      console.trace();
      return;
    }
    this.SelectedItems.splice(idx,1);

    if (this.SelectedItem == item) {
      this.SelectedItem = undefined;
    } else {
      this.SelectedItemsChange.emit(this.SelectedItems);
    }

    this.textBox.Focus();
  }

  RemoveAllItem() {
    this.Clear();
  }

  onDropDownClick(event) {
    this.IsDropDownOpen = !this.IsDropDownOpen;
    this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
    if (this.IsDropDownOpen)
      this.textBox.Focus();
    this.changeDetectorRef.detectChanges();
  }

  onFocusChange(event) {
    this.IsDropDownOpen = true; 
    this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
    this.filterItemSource();
  }

  onTextChange(value) {
    this.Text = value;
    this.TextChange.emit(this.Text);
    this.filterItemSource();

    if (StringExtensions.isNullOrEmpty(this.Text) == false) {
      this.IsDropDownOpen = true;
    }
  }

  onKeyDown(event) {
    if (event.keyCode == KeyCodes.DOWN)
    {
      var item = ArrayExtensions.findNextItem(this.filteredItemSource, this.HighlightedItem);
      if (item) {
        this.HighlightedItem = item;
        this.virtualPanel.ScrollToItem(item);
        this.changeDetectorRef.detectChanges();
      }
    }

    if (event.keyCode == KeyCodes.UP)
    {
      var item = ArrayExtensions.findPreviousItem(this.filteredItemSource, this.HighlightedItem);
      if (item) {
        this.HighlightedItem = item;
        this.virtualPanel.ScrollToItem(item);
        this.changeDetectorRef.detectChanges();
      }
    }

    if (event.keyCode == KeyCodes.BACKSPACE)
    {
      if (StringExtensions.isNullOrEmpty(this.Text)) {
        if(this.SelectedItems.length>0)
          this.RemoveSelectedItem(this.SelectedItems[this.SelectedItems.length-1]);
      }
      
      if (this.SelectionMode == SelectionMode.Single) 
        this.IsDropDownOpen = true;
    }
  }

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

  onKeyUp(event) {
    if (event.keyCode == KeyCodes.ESCAPE) {
      this.IsDropDownOpen = false;
      this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
      this.virtualPanel.ResetScroll();
      this.changeDetectorRef.detectChanges();      
    }

    if (event.keyCode == KeyCodes.ENTER)
      this.SelectedItem = this.HighlightedItem;
  }

   get ComboBoxModeClass() {
     return this.SelectionMode == SelectionMode.Single ? "combo-box-panel-single" : "combo-box-panel-multiple";
   }

  RaiseChange() {
    this.changeDetectorRef.detectChanges();
  }
}