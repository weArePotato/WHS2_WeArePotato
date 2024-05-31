import { 
    Component,
    ElementRef,
    HostBinding,
    Input,
    OnChanges,
    SimpleChanges } from '@angular/core';
import { ElementExtensions } from '../../../objects/extensions/element-extensions';


@Component({
    selector: 'pm-sidebar',
    //templateUrl: './app/controls/components/sidebar/sidebar.html',
    templateUrl: './sidebar.html',
    styles: [`
    :host { 
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    `],
})
export class SidebarComponent extends ElementRef {
    constructor(private element: ElementRef) {
        super(element.nativeElement);        
    }

    ngDoCheck() {
        var flexBasis = this.element.nativeElement.style["flex-basis"];
        var size = ElementExtensions.parsePx(flexBasis);
        if (!size) return;
        if (this.IsCollapsed && size > this.MinWidthPx) {
            this.IsCollapsed = false;
            return;
        }

        if (!this.IsCollapsed && size < this.MinWidthPx) {
            this.IsCollapsed = true;
            return;
        }
    }

    @Input() Header: string;
    @Input() RibbonHeader: string;
    @Input() IsCollapsed: boolean;

    @Input()
    @HostBinding('style.flex-basis.px') FlexBasisPx = 300;

    @Input()
    @HostBinding('style.min-width.px') MinWidthPx = 35;
    PreviousFlexBasis: any;

    OnToggleHeader() {
        if (this.IsCollapsed) {
            this.element.nativeElement.style["flex-basis"] = this.PreviousFlexBasis;
        } else {
            this.PreviousFlexBasis = this.element.nativeElement.style["flex-basis"];
            this.element.nativeElement.style["flex-basis"] = this.MinWidthPx + "px";
        }
        this.IsCollapsed = !this.IsCollapsed;
    }
 }