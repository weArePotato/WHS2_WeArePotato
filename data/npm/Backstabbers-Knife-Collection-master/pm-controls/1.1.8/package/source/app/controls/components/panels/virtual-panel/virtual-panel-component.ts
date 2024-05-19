import {
    ChangeDetectionStrategy,
    ChangeDetectorRef,
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    Output,
    ViewChild,
    ViewContainerRef
} from '@angular/core';
import { ElementExtensions } from '../../../../objects/extensions/element-extensions';
 

@Component({
    selector: 'pm-virtual-panel',
    //templateUrl: './app/controls/components/panels/virtual-panel/virtual-panel.html'
    templateUrl: './virtual-panel.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
    styles: [`
    :host { 
      display: block;
      height: 100%;
    }
    `],
})
export class VirtualPanelComponent {

    constructor(
        private changeDetectorRef: ChangeDetectorRef,
        private viewContainerRef: ViewContainerRef) {
        this.changeDetectorRef.detach();
        //this.el = viewContainerRef.element.nativeElement;
      }

    @Input() HeightPx: number;
    @Input() CalculateItemSize: Function;  
    @Input() ItemHeight: any;  
    @Input() ControlHeight: any;
    @Input() ItemTemplate: TemplateRef<any>;
    @Input() ItemClass: any;
    @Input() LastItemClass: any;
    @Input() DisplayMemberPath: any; // should be property name or function.
    @Input() ShowHighlight: boolean;
    @Input() ItemHighlightClass: any;
    @Input() Items: any;
    @Input() VisibleItems: Array<any>;
    @Input() ScrollTop: any = 0;
    @Input() ContainerHeight: any;
    @Input() WidthPx: any;
    ShowHorizontalScrollbar: boolean = false;
    ShowVerticalScrollbar: boolean = false;
    @Input() SelectedItems: any;    
    @Input() Text: any;
    @Input() ItemSelectedClass: any;    
    @Output() ItemSelected: EventEmitter<any> = new EventEmitter<any>();

    @ViewChild('virtualItemContainer') virtualItemContainer: any;
    @ViewChild('itemScrollbarVerticalContainer') itemScrollbarVerticalContainer: any;
    
    ngAfterViewChecked(){
        setTimeout(()=>{ 
            this.SizeHorizontalScrollbar();
            this.SizeVerticalScrollbar();
        }, 0); 
     }

    ngDoCheck() {
        this.SizeHorizontalScrollbar();
        this.SizeVerticalScrollbar();
    }

    ActualControlHeight: any; 

    private highlightedItem: any;
    @Input('HighlightedItem')
    get HighlightedItem(): any {
      return this.highlightedItem;
    }
  
    set HighlightedItem(value: any) {        
      this.highlightedItem = value;
      this.changeDetectorRef.detectChanges();
    }

    private itemsSource: Array<any> = [];
    @Input('ItemsSource')
    get ItemsSource(): Array<any> {
      return this.itemsSource;
    }
  
    set ItemsSource(value: Array<any>) {
      if (value === this.itemsSource) return;
      this.itemsSource = value;
      this.createCollectionView();
      this.SizeHorizontalScrollbar();
      this.handleVerticalScroll(this.ScrollTop);
    }

    createCollectionView() {
        if (!this.ItemsSource) return;
        var items = this.ItemsSource.slice();    
        //items = this.getAllItems(items);
        this.calculateRowHeights(items);        
        this.Items = items;
    }

    calculateRowHeights(items: Array<any>) {
        var totalHeight = 0;
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            item['_top'] = totalHeight;

            if (item['_itemResizeHeight'])
                item['_itemHeight'] = item['_itemResizeHeight'];
            else if (this.CalculateItemSize)
                item['_itemHeight'] = this.CalculateItemSize(item);
            else
                item['_itemHeight'] = parseInt(this.ItemHeight);
            
            totalHeight += item['_itemHeight'];
        }

        this.HeightPx = totalHeight;
        this.SizeVerticalScrollbar();
    }

    onVerticalScroll(event) {
        const currentScrollTop = this.virtualItemContainer.nativeElement.scrollTop = event.target.scrollTop;
        this.handleVerticalScroll(currentScrollTop);        
    }
    
    private handleVerticalScroll(scrollTop: number) {
        if (!this.Items) return;

        this.ScrollTop = scrollTop;
        const currentViewPortIndex = Math.floor(scrollTop / this.ItemHeight);        
         
        const isPixelHeight = (this.ControlHeight + "").endsWith("px");
        var itemsPerViewPort;
        if (isPixelHeight)
            itemsPerViewPort = (Math.ceil(+(<string>this.ControlHeight).substr(0,(<string>this.ControlHeight).indexOf("px")) / this.ItemHeight) + 1);
        else
            itemsPerViewPort = (Math.ceil(this.ContainerHeight / this.ItemHeight) + 1);
    
        this.VisibleItems = this.Items.slice(currentViewPortIndex, currentViewPortIndex + itemsPerViewPort);
        
        if (isPixelHeight) // absolute height
            this.ActualControlHeight = (this.Items.length * this.ItemHeight)+"px";
        else  // relative height
            this.ActualControlHeight= this.ControlHeight;
        
        this.SizeHorizontalScrollbar();
        this.changeDetectorRef.detectChanges();
    }

    onHorizontalScroll(event) {
        const currentScrollLeft = this.virtualItemContainer.nativeElement.scrollLeft = event.target.scrollLeft;
    }

    mouseWheelUp(event: any) {
        if (this.itemScrollbarVerticalContainer)
            this.itemScrollbarVerticalContainer.nativeElement.scrollTop -= event.wheelDelta;
    }
    
    mouseWheelDown(event: any) {
        if (this.itemScrollbarVerticalContainer)
            this.itemScrollbarVerticalContainer.nativeElement.scrollTop -= event.wheelDelta;
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
    
    isHighlight(item: any) : boolean {
        return this.HighlightedItem == item;
    }

    ScrollToItem(item: any) {
        if (this.itemScrollbarVerticalContainer)  {      
            if (item['_top'] || item['_top'] === 0) {
                var top = item['_top'];            
                this.itemScrollbarVerticalContainer.nativeElement.scrollTop = top;
            }
        }
    }

    SelectItem(item: any) {
     //   this.VisibleItems = this.VisibleItems.slice(); // get new reference of array to force change detection
        this.ItemSelected.emit(item);
        this.changeDetectorRef.detectChanges();

    }
    
    IsItemSelected(item: any) : string {
        if (this.SelectedItems && this.SelectedItems.includes(item))
            return this.ItemSelectedClass;
        return;
    }

    GetItemClass(item: any) : string {
        if (this.LastItemClass && this.VisibleItems[this.VisibleItems.length - 1] == item) {
            return this.LastItemClass;
        }

        return this.ItemClass;
    }

    ResetScroll() {
        this.ScrollTop = 0;
        this.handleVerticalScroll(this.ScrollTop);
    }

    SizeVerticalScrollbar() {
        if (this.ContainerHeight != ElementExtensions.height(this.virtualItemContainer))
        {
            this.ContainerHeight = ElementExtensions.height(this.virtualItemContainer);
            this.ShowVerticalScrollbar = ElementExtensions.scrollHeight(this.virtualItemContainer) > ElementExtensions.height(this.virtualItemContainer);
            if (this.itemScrollbarVerticalContainer)
                this.ScrollTop = this.virtualItemContainer.nativeElement.scrollTop = this.itemScrollbarVerticalContainer.nativeElement.scrollTop;
            this.handleVerticalScroll(this.ScrollTop);
        }
    }

    SizeHorizontalScrollbar() {
        if (this.WidthPx != ElementExtensions.scrollWidth(this.virtualItemContainer))
        {
            var width = ElementExtensions.width(this.virtualItemContainer);
            if (width <= 0) 
                return;

            this.WidthPx = ElementExtensions.scrollWidth(this.virtualItemContainer);
            this.ShowHorizontalScrollbar = this.WidthPx > ElementExtensions.width(this.virtualItemContainer);
        }
    }

    RaiseChange() {
        this.changeDetectorRef.detectChanges();
    }
}