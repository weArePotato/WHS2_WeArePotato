import { ApplicationRef, ComponentFactoryResolver, ComponentRef, Injector, Type } from '@angular/core';
export declare class ToastService {
    private applicationRef;
    private componentFactoryResolver;
    private injector;
    private container;
    constructor(applicationRef: ApplicationRef, componentFactoryResolver: ComponentFactoryResolver, injector: Injector);
    getRootViewContainer(): ComponentRef<any>;
    setRootViewContainer(container: any): void;
    getComponentRootNode(componentRef: ComponentRef<any>): HTMLElement;
    getRootViewContainerNode(): HTMLElement;
    projectComponentInputs(component: ComponentRef<any>, options: any): ComponentRef<any>;
    ShowInstance<T>(instance: any, options?: any, location?: Element): ComponentRef<any>;
    Show<T>(componentClass: Type<T>, options?: any, location?: Element): T;
}
