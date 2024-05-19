import {
    ChangeDetectionStrategy,
    ChangeDetectorRef,
    Component,
    EventEmitter,
    TemplateRef,
    Input,
    OnInit,
    Output,
    ViewChild,
    ViewContainerRef
} from '@angular/core';

@Component({
    selector: 'pm-properties',
    //templateUrl: './app/controls/components/properties/properties.html'
    templateUrl: './properties.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
    styles: [`
    :host { 
      display: block;
      height: 100%;
    }
    `],
})
export class PropertiesComponent implements OnInit {

    constructor(
        private changeDetectorRef: ChangeDetectorRef) {
        this.changeDetectorRef.detach();
    }

    private item: any;
    @Input() 
    get Item() {
        return this.item;
    }
    set Item(value: any) {
        this.item = value;
    }

    ngOnInit() {
        this.changeDetectorRef.detectChanges();
    }
}