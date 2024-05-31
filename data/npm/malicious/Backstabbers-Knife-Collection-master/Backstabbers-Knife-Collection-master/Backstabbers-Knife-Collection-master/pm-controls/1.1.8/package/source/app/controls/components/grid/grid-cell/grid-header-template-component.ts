import {
    Component,
    ComponentFactory,
    ChangeDetectorRef,
    ChangeDetectionStrategy,
    Input,
    ViewChild,
    ViewContainerRef,
    NgModule
} from '@angular/core';

import { RouterModule, Routes } from '@angular/router';
import { Column } from '../../../../objects/request/column' 

@Component({
    selector: 'pm-grid-header-template',
    template: '<ng-template #container></ng-template>',
    changeDetection: ChangeDetectionStrategy.OnPush,
    styles: [`
    :host { 
        width: 100%;
    }
    `]
})
export class GridHeaderTemplateComponent {
    constructor(
        //private viewContainer: ViewContainerRef,
        private changeDetectorRef: ChangeDetectorRef) {
        changeDetectorRef.detach();
    }

    @Input() Column: Column;
    @ViewChild('container', { read: ViewContainerRef }) viewContainer: ViewContainerRef;

    ngOnInit() {
        if (this.Column.HeaderTemplateComponent) {
            var container = this.viewContainer.createComponent(this.Column.HeaderTemplateComponent);
            container.instance.Column = this.Column;
            container.changeDetectorRef.detectChanges();
        }
    }
}