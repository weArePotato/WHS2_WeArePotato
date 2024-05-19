/*
    Incorporated paging as described here:
    http://jsfiddle.net/SDa2B/4/

Visual representation of the approach:

--------
   --------
      --------
         --------
            --------
               --------
                  --------
                     --------
                        --------
                           --------
                              --------
                                 --------
                                    --------
                                       --------
                                          --------

==================================================

[=] - real scrollable height (MAX_SCROLL_SIZE)
[-] - "pages";  total height of all (n) pages is (th) = (ph) * (n)

The overlap between pages is (cj) and is the distance the scrollbar
will jump when we adjust the scroll position during page switch.

To keep things smooth, we need to minimize both (n) and (cj).
Setting (ph) at 1/100 of (h) is a good start.        
*/
import {
  Directive,
  Input,
  OnDestroy,
  ViewContainerRef,
  TemplateRef,
  ElementRef,
  Renderer,
  EmbeddedViewRef,
  NgZone,
  ChangeDetectorRef,
} from '@angular/core';
import {VsForPanel} from './vs-for-panel';


@Directive({
  selector: '[vsFor]',
  // inputs: [
  //   'originalCollection: vsFor',
  //   'vsScrollParent: vsForScrollParent'
  // ]
})
export class VsFor implements OnDestroy {
  private static readonly MAX_SCROLL_SIZE : number = 1300000;
  
  private itemHeight: any;
  @Input('vsForItemHeight')
  set ItemHeight(value: any) {
    this.itemHeight = value;    
    //this.virtualPanel.originalCollection = this._originalCollection;
  }  
  get ItemHeight() {
    return this.itemHeight;
  }  

  vsForPanel        : VsForPanel;
  virtualVsForPanel : VsForPanel; // virtual panel on the view's context
  scrollParent      : HTMLElement;
  @Input('vsForScrollParent')
  vsScrollParent  : string;
  
  private _originalCollection : Array<any> = [];
  @Input('vsFor')  
  set originalCollection(value: any[]) {    
    this._originalCollection = value || [];
    this.vsForPanel.originalCollection = this._originalCollection;
  }  
  get originalCollection() {
    return this._originalCollection;
  }

  constructor(
    private _element       : ElementRef,
    private _viewContainer : ViewContainerRef,
    private _templateRef   : TemplateRef<any>,
    private _renderer      : Renderer,
    private _ngZone        : NgZone,
    private _changeDetectorRef: ChangeDetectorRef
  ) {
    let _prevClientSize;

    this.vsForPanel = new VsForPanel(_element,
                                         _viewContainer,
                                         _templateRef,
                                         _renderer,
                                         _ngZone,
                                         _changeDetectorRef);
  }
  ngOnChanges() {
    this.vsForPanel.onChanges();
  }

  ngOnInit() {
    this.vsForPanel.init(this.vsScrollParent, this.itemHeight);
    this.vsForPanel.view.context.vsCalcTop = this.calcTop;
    this.vsForPanel.view.context.vsMoveItemIntoView = this.moveItemIntoView.bind(this);
    this.vsForPanel.view.context.vsVirtualPanel = this.vsForPanel;
  }

  ngOnDestroy() {
  	this.vsForPanel.destroy();
  }

  moveItemIntoView(item : any) {
    this.vsForPanel.moveItemIntoView(item);
  }

  moveItemToTop(item : any) {
    this.vsForPanel.moveItemToTop(item);
  }

  moveItemToBottom(item : any) {
    this.vsForPanel.moveItemToBottom(item);
  }

  calcTop(index: number) : string {
    return this.virtualVsForPanel.calcTop(index); 
  }
}