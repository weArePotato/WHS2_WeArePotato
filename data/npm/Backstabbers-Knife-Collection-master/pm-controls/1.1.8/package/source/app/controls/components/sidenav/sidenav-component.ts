import {
    Component,
    Input,
    OnInit,
    OnDestroy,
    ChangeDetectorRef,
    ChangeDetectionStrategy,
    ViewContainerRef
} from '@angular/core';

@Component({
    selector: 'pm-sidenav',
    //templateUrl: './app/controls/components/sidenav/sidenav.html',
    templateUrl: './sidenav.html',
    changeDetection: ChangeDetectionStrategy.OnPush
    // styles: [`
    // :host { 
    //     white-space: nowrap;
    //     overflow: hidden;
    //     text-overflow: ellipsis;
    // }
    // `],
})
export class SidenavComponent implements OnInit, OnDestroy {
    constructor(
      public changeDetectorRef: ChangeDetectorRef,
      public viewContainerRef: ViewContainerRef) {
        this.el = viewContainerRef.element.nativeElement;
        this.changeDetectorRef.detach();
        this.clickEvent = this.HandleClick.bind(this);
    }
    
    private el: Element;
    private clickEvent;

    ngOnInit() {
        this.changeDetectorRef.detectChanges();

        let body = document.querySelector('body');
        body.addEventListener('click', this.clickEvent, false);
    }

    private isSidenavOpen: boolean;
    @Input() get IsSidenavOpen() {
        return this.isSidenavOpen;
    }

    set IsSidenavOpen(value: boolean) {        
        this.isSidenavOpen = value;
        this.changeDetectorRef.detectChanges();
    }

    ToggleSidenav() {
        this.IsSidenavOpen = !this.IsSidenavOpen;
    }

    HandleClick(e) {
        if (!this.IsSidenavOpen || !e.target) { return; };
        if (this.el !== e.target && !this.el.contains((<any>e.target))) {
            this.IsSidenavOpen = false;
            this.changeDetectorRef.detectChanges();
        }
    }

    ngOnDestroy() {
        let body = document.querySelector('body');
        body.removeEventListener('click', this.clickEvent, false);
    }
}