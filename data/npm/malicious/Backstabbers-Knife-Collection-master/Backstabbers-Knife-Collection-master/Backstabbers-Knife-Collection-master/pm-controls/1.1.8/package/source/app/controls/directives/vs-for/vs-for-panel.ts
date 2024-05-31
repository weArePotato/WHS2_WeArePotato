import {
  Directive,
  ViewContainerRef,
  TemplateRef,
  ElementRef,
  Renderer,
  EmbeddedViewRef,
  NgZone,
  ChangeDetectorRef,
} from '@angular/core';


export class VsForPanel {
    private static readonly MAX_SCROLL_SIZE : number = 1300000;

    originalLength        : number;
    view                  : EmbeddedViewRef<any>;
    parent                : HTMLElement;
    tagName               : string = 'div';
    autoSize              : boolean;
    scrollParent          : HTMLElement;
    clientSizeProp        : string;
    offsetSizeProp        : string;
    scrollPosProp         : string;
    layoutProp            : string;
    numOfScreenElements   : number = 6;

    totalSize             : number;
    scrollSize            : number;
    numberOfPages         : number;
    pageSize              : number;
    pageCoefficient       : number;
    elementSize           : number;
    currentPage           : number = 0;
    previousScrollTop     : number = 0;
    currentPageOffset     : number = 0;

    sizes                 : number[];
    startIndex            : number;
    endIndex              : number;
    private _prevStartIndex       : number;
    private _prevEndIndex         : number;
    onWindowResize        : any;
    onZone							  : any;

  private _originalCollection : Array<any> = [];
  set originalCollection(value: any[]) {
    this._originalCollection = value || [];
    if (this.scrollParent) {
      this.refresh();
    }
    else {
    	this.postDigest(this.refresh.bind(this));
    }
  }
  get originalCollection() {
    return this._originalCollection;
  }

  private _slicedCollection : Array<any> = [];
  set slicedCollection(value: any[]) {
    this._slicedCollection = value;
    this.view.context.vsCollection = this._slicedCollection;
  }
  get slicedCollection() {
    return this._slicedCollection;
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
    const reinitOnClientHeightChange = () => {
      if (!this.scrollParent) {
        return;
      }

      let ch = this.getViewportSize(this.scrollParent, this.clientSizeProp);
      if (ch !== _prevClientSize) {
        _prevClientSize = ch;
        this._ngZone.run(() => {
          this.refresh();
        });
      }
      else {
        _prevClientSize = ch;
      }
    };

    this.onZone = this._ngZone.onStable.subscribe(reinitOnClientHeightChange);
  }
  onChanges() {
    if (this.scrollParent) {
      this.refresh();
    }
    else {
      this.postDigest(this.refresh.bind(this));
    }
  }
  postDigest(fn) {
    const subscription:any = this._ngZone.onStable.subscribe(() => {
      fn();
      subscription.unsubscribe();
    });
  }

  init(scrollParentClass: string, itemHeight?: number) {
    this.view = this._viewContainer.createEmbeddedView(this._templateRef);
    this.parent = this.nextElementSibling(this._element.nativeElement);

    this.autoSize = true;
    this.clientSizeProp = 'clientHeight'; // this.__horizontal ? 'clientWidth' : ..
    this.offsetSizeProp = 'offsetHeight'; // this.__horizontal ? 'offsetWidth' : 'offsetHeight';
    this.scrollPosProp = 'scrollTop'; //this.__horizontal ? 'scrollLeft' : 'scrollTop';
    this.layoutProp =  'height'; //this.__horizontal ? 'width' : 'height';

    if (scrollParentClass) {
      this.scrollParent = this.closestElement(this.parent, scrollParentClass);
    }
    else {
      this.scrollParent = this.parent;
    }
    
    this.scrollParent.style['position'] = "relative";
    this.elementSize = itemHeight || 50;

    this.totalSize = 0;

    this.startIndex = 0;
    this.endIndex = 0;
    this.currentPage = 0;
    this.currentPageOffset = 0;
    this.previousScrollTop = 0;

    this.scrollParent.addEventListener('scroll', () => {
      this.updateInnerCollection();
    });

    this.onWindowResize = () => {
	    this._ngZone.run(() => {
	      	this.updateInnerCollection();
	    });
    }

    window.addEventListener('resize', this.onWindowResize);
  }

  destroy() {
  	if (this.onWindowResize) {
	  	window.removeEventListener('resize', this.onWindowResize);
  	}

  	if (this.onZone) {
  		this.onZone.unsubscribe();
  	}
  }
  refresh() {
    if(!this.view) return; 

    if (!this.originalCollection || this.originalCollection.length < 1) {
      this.slicedCollection = [];
      this.originalLength = 0;
      this.updateTotalSize(0);
    }
    else {
      this.originalLength = this.originalCollection.length;
      this.autoSize = true;
      //this.postDigest(this.setAutoSize.bind(this));
    }

    this.reinitialize();
  }
  updateTotalSize(size: number) {
    this.totalSize = size;
    this.numberOfPages = this.getNumberOfPages();
    this.pageCoefficient = this.getPageCoefficient();
    this.pageSize = this.getPageSize();
    this.scrollSize = this.getScrollSize();
  }
  reinitialize() {
    this._prevStartIndex = void 0;
    this._prevEndIndex = void 0;

    this.updateTotalSize(this.elementSize * this.originalLength);

    this.parent.style[this.layoutProp] = this.scrollSize + "px";
    
    this.updateInnerCollection();
  }
  //setAutoSize() {
  //   if (this.autoSize) {
  //     let gotSomething = false;
  //   	if (this.parent.offsetHeight || this.parent.offsetWidth) { // element is visible
  //       const child = this.parent.children[0];

  //       if (child && child[this.offsetSizeProp]) {
  //         gotSomething = true;
  //         this.elementSize = child[this.offsetSizeProp];
  //       }
  //     }

  //     if (gotSomething) {
  //       this.autoSize = false;
  //       this._ngZone.run(() => {
  //         this.reinitialize();
  //       });
  //     }
  //   }
  // }
 
  updateInnerCollection() {
    let scrollPosition = this.getScrollPos(this.scrollParent, this.scrollPosProp);
    let viewportSize = this.getViewportSize(this.scrollParent, this.clientSizeProp);

    const scrollOffset = this.parent === this.scrollParent ? 0 : this.getScrollOffset(
      this.parent,
      this.scrollParent
    );

    let __startIndex = this.startIndex;
    let __endIndex = this.endIndex;

    this.onScroll(viewportSize);

    let y = this.scrollParent.scrollTop + this.currentPageOffset,
        buffer = this.elementSize*this.numOfScreenElements,
        top = Math.floor((y-buffer)/this.elementSize),
        bottom = Math.ceil((y+viewportSize+buffer)/this.elementSize);
    
    this.startIndex  = Math.max(0,top);
    this.endIndex  = Math.min(this.totalSize/this.elementSize,bottom);

    let digestRequired = false;
    if (this._prevStartIndex == null) {
      digestRequired = true;
    }
    else if (this._prevEndIndex == null) {
      digestRequired = true;
    }

    if (!digestRequired) {
        digestRequired = this.startIndex !== this._prevStartIndex ||
                 this.endIndex !== this._prevEndIndex;
    }

    if (digestRequired) {
      this.slicedCollection = this.originalCollection.slice(this.startIndex, this.endIndex);

      this._prevStartIndex = this.startIndex;
      this._prevEndIndex = this.endIndex;
    

      this._changeDetectorRef.markForCheck();
    }

    return digestRequired;
  }

  moveItemIntoView(item: any) {
    let index = this.slicedCollection.indexOf(item);
      
    let itemTop = this.calcTopNum(index);

    if(itemTop<this.scrollParent.scrollTop)
        this.moveItemToTop(index);
    else if(itemTop+this.elementSize>this.getScrollBottom()) 
        this.moveItemToBottom(index);
  }

  moveItemToTop(index : number) {
    this.scrollParent.scrollTop = this.calcTopNum(index);
  }

  moveItemToBottom(index : number) {      
    this.scrollParent.scrollTop = this.calcTopNum(index) +this.elementSize- this.getViewportSize(this.scrollParent, this.clientSizeProp);
  }

  pageForward(curScrollTop : number) {
    this.currentPage++;
    this.currentPageOffset = Math.round(this.currentPage*this.pageCoefficient);
    this.previousScrollTop = curScrollTop-this.pageCoefficient;
    this.scrollParent.scrollTop = this.previousScrollTop;
  }

  pageBack(curScrollTop : number) {
    this.currentPage--;
    this.currentPageOffset = Math.round(this.currentPage*this.pageCoefficient);
    this.previousScrollTop = curScrollTop+this.pageCoefficient;
    this.scrollParent.scrollTop = this.previousScrollTop;
  }

  onScroll(viewportSize:number) : number {
    var scrollTop = this.scrollParent.scrollTop;

    if(Math.abs(scrollTop-this.previousScrollTop)>viewportSize) {
      return this.onBigScroll(scrollTop,viewportSize);
    }
    else {
      return this.onSmallScroll(scrollTop);
    }
  }

  onSmallScroll(scrollTop : number) : number {
    if(scrollTop + this.currentPageOffset > (this.currentPage+1)*this.pageSize) {
      this.pageForward(scrollTop);
    }
    else if(scrollTop + this.currentPageOffset < this.currentPage*this.pageSize) {
      this.pageBack(scrollTop);
    }
    else 
      this.previousScrollTop = scrollTop;

    return this.previousScrollTop;      
  }

getWindowScroll() {
    if ('pageYOffset' in window) {
        return {
        scrollTop: pageYOffset,
        scrollLeft: pageXOffset
        };
    }
    else {
        var sx, sy, d = document, r = d.documentElement, b = d.body;
        sx = r.scrollLeft || b.scrollLeft || 0;
        sy = r.scrollTop || b.scrollTop || 0;
        return {
        scrollTop: sy,
        scrollLeft: sx
        };
    }
    }

getViewportSize(element: Node | Window, sizeProp: string): number {
    if (element === window) {
        return sizeProp === 'clientWidth' ? window.innerWidth : window.innerHeight;
    }
    else {
        return element[sizeProp];
    }
}

getScrollPos(element: Node | Window, scrollProp: string):number {
    return element === window ? this.getWindowScroll()[scrollProp] : element[scrollProp];
    }

  getScrollOffset(vsElement: HTMLElement, scrollElement: HTMLElement | Window):number {
    var vsPos = vsElement.getBoundingClientRect()['top'];
    var scrollPos = scrollElement === window ? 0 : (<HTMLElement>scrollElement).getBoundingClientRect()['top'];
    var correction = vsPos - scrollPos +
        (scrollElement === window ? this.getWindowScroll() : scrollElement)['scrollTop'];

    return correction;
    }

 nextElementSibling(el) {
    if (el.nextElementSibling) {
        return el.nextElementSibling;
    }

    do {
        el = el.nextSibling;
    } while (el && el.nodeType !== 1);

    return el;
    }

  onBigScroll(scrollTop : number, viewportSize : number) : number {
    this.currentPage = Math.floor(scrollTop * ((this.totalSize-viewportSize)/(this.scrollSize-viewportSize) * (1/this.pageSize)));
    this.currentPageOffset = Math.round(this.currentPage*this.pageCoefficient);
    this.previousScrollTop = scrollTop;
    return this.previousScrollTop;
  }

  calcTopNum(index: number) :number {
    return ((index+this.startIndex)*this.elementSize-this.currentPageOffset);
  }

  calcTop(index: number) : string {
    return this.calcTopNum(index) +"px";
  }

  getScrollBottom() {
      return this.scrollParent.scrollTop+ this.getViewportSize(this.scrollParent, this.clientSizeProp);
  }

  getScrollSize() {  // actual height or width of the scroll window. also could be thought of as "page size"
    return Math.min(this.totalSize, VsForPanel.MAX_SCROLL_SIZE);
  }

  getPageSize() {
    return VsForPanel.MAX_SCROLL_SIZE/100;
  }

  getNumberOfPages() {
    return Math.ceil(this.totalSize/this.getPageSize());
  }

  getPageCoefficient() {
    return this.getNumberOfPages()<=1? 0 : (this.totalSize-this.getScrollSize())/(this.getNumberOfPages()-1);
  }

  private getOffset(index: number) {
    return this.previousScrollTop; // (index + this.startIndex) * this.elementSize + this.vsOffsetBefore;
  }

  dde:any = document.documentElement;
  matchingFunction = this.dde.matches ? 'matches' :
            this.dde.matchesSelector ? 'matchesSelector' :
            this.dde.webkitMatches ? 'webkitMatches' :
            this.dde.webkitMatchesSelector ? 'webkitMatchesSelector' :
            this.dde.msMatches ? 'msMatches' :
            this.dde.msMatchesSelector ? 'msMatchesSelector' :
            this.dde.mozMatches ? 'mozMatches' :
            this.dde.mozMatchesSelector ? 'mozMatchesSelector' : null;

    closestElement(el: Node, selector: string): HTMLElement {
  while (el !== document.documentElement && el != null && !el[this.matchingFunction](selector)) {
    el = el.parentNode;
  }

  if (el && el[this.matchingFunction](selector)) {
    return <HTMLElement>el;
  }
  else {
    return null;
  }
}  
}
