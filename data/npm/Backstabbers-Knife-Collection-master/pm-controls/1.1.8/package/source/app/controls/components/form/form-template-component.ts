import {
    ChangeDetectorRef,
    ChangeDetectionStrategy,
    Component,    
    Input,
    Output,    
    ViewChild,
    ViewContainerRef
} from '@angular/core';

import { Property } from '../../../objects/request/properties/property';
import { TemplateProperty } from '../../../objects/request/properties/template-property';
import { JitComponent } from '../../../controls/components/base/components/jit-component';

@Component({
    selector: 'pm-form-template',
    template: '<ng-template #container></ng-template>',
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class FormTemplateComponent {
    constructor(
        //private viewContainer: ViewContainerRef,
        private changeDetectorRef: ChangeDetectorRef) {
        changeDetectorRef.detach();
    }

    @Input() Property: Property;
    @ViewChild('container', { read: ViewContainerRef }) viewContainer: ViewContainerRef;

    ngOnInit() {
        if (this.Property.IsTemplate) {
            var type = <TemplateProperty>this.Property;            
            if (!type.TemplateComponent) {
                type.TemplateComponent = JitComponent.createComponent(type.Template, type.TemplateModules);
            }
            var container = this.viewContainer.createComponent(type.TemplateComponent);
            container.instance.Property = this.Property;
            container.changeDetectorRef.detectChanges();
        }
    }
}