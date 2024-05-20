import {
  ChangeDetectionStrategy, 
  ChangeDetectorRef,
  Component,   
  forwardRef,
  EventEmitter,
  Input,
  OnInit,   
  Output, 
  SimpleChanges, 
  ViewContainerRef,
  ViewChild,
  IterableDiffers,
  IterableDiffer
} from '@angular/core';
import { SelectionMode } from '../../../../objects/enums/selection-mode';
import { ComboBoxComponent } from '../combo-box/combo-box-component';

@Component({
  selector: 'pm-check-box-combo-box',
  //templateUrl: './app/controls/components/boxes/check-box-combo-box/check-box-combo-box.html',
  templateUrl: './check-box-combo-box.html',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class CheckBoxComboBoxComponent implements OnInit {  
  iterableDiffer: IterableDiffer<{}>;
  
  @Input() Watermark: string;
  @Input() DisplayMemberPath: any; // should be property name or function.
  SelectionMode: SelectionMode = SelectionMode.Multiple;
  @Output() SelectedItemsChange: EventEmitter<any> = new EventEmitter<any>();
  @Input() IsDisabled: boolean;
  
  @ViewChild(forwardRef(() => ComboBoxComponent)) comboBox: ComboBoxComponent;

  constructor(
    public changeDetectorRef: ChangeDetectorRef,
    public viewContainerRef: ViewContainerRef,
    private _iterableDiffers: IterableDiffers) {
      this.iterableDiffer = this._iterableDiffers.find([]).create(null);
      this.changeDetectorRef.detach();
  }

  ngOnInit() {
    this.changeDetectorRef.detectChanges();
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes['SelectedItems']) {
      this.comboBox.RaiseChange();
      this.SelectedItemsChange.emit(this.selectedItems);
      this.changeDetectorRef.detectChanges();
    }
  }

  ngDoCheck() {
    let changes = this.iterableDiffer.diff(this.selectedItems);
    if (changes) {
      this.comboBox.RaiseChange();
      this.SelectedItemsChange.emit(this.selectedItems);
      this.changeDetectorRef.detectChanges();
    }
}

  OnUncheckAllClick() {
    this.comboBox.Clear();
    this.changeDetectorRef.detectChanges();
  }

  OnCheckAllClick() {
    this.comboBox.SelectAll();
    this.changeDetectorRef.detectChanges();
  }

  IsCheckedChange() {
    this.changeDetectorRef.detectChanges();
  }

  IsChecked(item: any) {
    if (this.comboBox.SelectedItems && this.comboBox.SelectedItems.includes(item))
      return true;
    return false;
  }

  private itemsSource: Array<any>;
  @Input('ItemsSource')
  get ItemsSource(): any {
    return this.itemsSource;
  }

  set ItemsSource(value: any) {
    this.itemsSource = value;
    this.comboBox.RaiseChange();
  }

  private selectedItems: Array<any>;
  @Input('SelectedItems')
  get SelectedItems(): any {
    return this.selectedItems;
  }

  set SelectedItems(value: any) {
    this.selectedItems = value;
  }
}