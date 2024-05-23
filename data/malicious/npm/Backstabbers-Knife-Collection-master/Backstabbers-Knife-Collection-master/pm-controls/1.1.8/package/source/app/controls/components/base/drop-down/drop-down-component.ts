import { 
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  OnDestroy,
  OnInit,
  ElementRef,
  HostBinding,
  Input,
  ViewContainerRef,
  ViewChild
} from '@angular/core';

import { CompatibilityService } from '../../../services/compatibility/compatibility-service';
import { ElementExtensions } from '../../../../objects/extensions/element-extensions';


@Component({
  selector: 'pm-drop-down',
  //templateUrl: './app/controls/components/base/drop-down/drop-down.html',
  templateUrl: './drop-down.html',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class DropDownComponent implements OnInit, OnDestroy {
  constructor(
    public changeDetectorRef: ChangeDetectorRef,
    public viewContainerRef: ViewContainerRef,
    public CompatibilityService: CompatibilityService) {
    this.changeDetectorRef.detach();
    this.el = viewContainerRef.element.nativeElement;
    this.scrollEvent = this.HandleScroll.bind(this);
    this.clickEvent = this.HandleClick.bind(this);
    this.resizeEvent = this.HandleResize.bind(this);
  }

  ngOnInit() {
    let body = document.querySelector('body');
    body.addEventListener('scroll', this.scrollEvent, true);
    this.el.addEventListener('click', this.clickEvent, false);
    window.addEventListener('resize', this.resizeEvent); 
  }

  ngDoCheck() {
    this.HandleResize();
  }

  ngOnDestroy() {
    let body = document.querySelector('body');
    body.removeEventListener('scroll', this.scrollEvent, true);
    this.el.removeEventListener('click', this.clickEvent, false);
    window.removeEventListener('resize', this.resizeEvent);
  }

  private el: any;
  private scrollEvent;
  private clickEvent;
  private resizeEvent;
  @Input() Width: string;
  @Input() MaxWidth: string;
  @Input() MinWidth: string;
  @Input() ContainerWidth: number;
  @Input() ContainerTop: number;
  @Input() HorizontalAlignment: string;
  @HostBinding('style.padding')
  @Input() Padding: string = '1px 0px 0px 0px';
  @ViewChild('dropDownPane') DropDownPane: ElementRef;

  private isDropDownOpen: boolean;
  @Input() get IsDropDownOpen() {
    return this.isDropDownOpen;
  }

  set IsDropDownOpen(value: boolean) {
    if (value && !this.CompatibilityService.IsLegacyBrowser)
    {
      this.ContainerWidth = this.el.offsetWidth;
      
      var parentOffsetTop = ElementExtensions.getParentScrollTop(this.el);
      this.ContainerTop = this.el.offsetTop - parentOffsetTop;
      this.changeDetectorRef.detectChanges();
    }
    
    this.isDropDownOpen = value;
    this.changeDetectorRef.detectChanges();
  }

  HandleScroll(e) {
    if (!this.IsDropDownOpen || !e.target) { return; };

    var parentOffsetTop = ElementExtensions.getParentScrollTop(this.el);
    this.ContainerTop = this.el.offsetTop - parentOffsetTop;
    this.changeDetectorRef.detectChanges();
  }

  HandleClick(e) {
    e.stopPropagation();
  }

  public HandleResize() {
    if (!this.IsDropDownOpen) { return; };

    this.ContainerWidth = this.el.offsetWidth;
    var parentOffsetTop = ElementExtensions.getParentScrollTop(this.el);
    this.ContainerTop = this.el.offsetTop - parentOffsetTop;
    this.changeDetectorRef.detectChanges();
  }
}