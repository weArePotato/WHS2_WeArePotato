var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, ChangeDetectorRef, ChangeDetectionStrategy, Input, ViewChild, ViewContainerRef } from '@angular/core';
import { Column } from '../../../../objects/request/column';
var GridHeaderTemplateComponent = /** @class */ (function () {
    function GridHeaderTemplateComponent(
        //private viewContainer: ViewContainerRef,
        changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        changeDetectorRef.detach();
    }
    GridHeaderTemplateComponent.prototype.ngOnInit = function () {
        if (this.Column.HeaderTemplateComponent) {
            var container = this.viewContainer.createComponent(this.Column.HeaderTemplateComponent);
            container.instance.Column = this.Column;
            container.changeDetectorRef.detectChanges();
        }
    };
    __decorate([
        Input(),
        __metadata("design:type", Column)
    ], GridHeaderTemplateComponent.prototype, "Column", void 0);
    __decorate([
        ViewChild('container', { read: ViewContainerRef }),
        __metadata("design:type", ViewContainerRef)
    ], GridHeaderTemplateComponent.prototype, "viewContainer", void 0);
    GridHeaderTemplateComponent = __decorate([
        Component({
            selector: 'pm-grid-header-template',
            template: '<ng-template #container></ng-template>',
            changeDetection: ChangeDetectionStrategy.OnPush,
            styles: ["\n    :host { \n        width: 100%;\n    }\n    "]
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], GridHeaderTemplateComponent);
    return GridHeaderTemplateComponent;
}());
export { GridHeaderTemplateComponent };
