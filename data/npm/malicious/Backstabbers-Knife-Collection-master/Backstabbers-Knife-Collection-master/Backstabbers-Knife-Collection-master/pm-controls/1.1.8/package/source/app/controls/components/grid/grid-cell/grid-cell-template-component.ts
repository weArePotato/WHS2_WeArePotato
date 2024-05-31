import {
    Component,
    ChangeDetectorRef,
    ChangeDetectionStrategy,    
    Input,
    ViewChild,
    ViewContainerRef,
    NgModule
} from '@angular/core';

import { RouterModule } from '@angular/router';
import { Column } from '../../../../objects/request/column';

@Component({
    selector: 'pm-grid-cell-template',
    template: '<ng-template #container></ng-template>',
    changeDetection: ChangeDetectionStrategy.OnPush,
    styles: [`
    :host { 
        width: 100%;
    }
    `]
})
export class GridCellTemplateComponent {
    constructor(
        //private viewContainer: ViewContainerRef,
        private changeDetectorRef: ChangeDetectorRef) {
        changeDetectorRef.detach();
    }

    @Input() Column: Column;
    @Input() Row: any;
    @ViewChild('container', {read: ViewContainerRef}) viewContainer: ViewContainerRef;

    ngOnInit() {
        if (this.Column.CellTemplateComponent) {
            var container = this.viewContainer.createComponent(this.Column.CellTemplateComponent);            
            container.instance.Column = this.Column;
            container.instance.Row = this.Row;
            container.changeDetectorRef.detectChanges();
        }
    }
}