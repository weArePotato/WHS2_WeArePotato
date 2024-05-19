import {
    ApplicationRef,
    ComponentFactoryResolver,
    ComponentRef,
    Injectable,
    Injector,
    ViewContainerRef,
    EmbeddedViewRef,
    Type
} from '@angular/core';
import { Toast } from '../../../controls/components/toast/toast';

@Injectable()
export class ToastService {
    private container: ComponentRef<any>;

    constructor(
        private applicationRef: ApplicationRef,
        private componentFactoryResolver: ComponentFactoryResolver,
        private injector: Injector) {
    }

    getRootViewContainer(): ComponentRef<any> {
        if (this.container) return this.container;

        const rootComponents = this.applicationRef['components'];
        if (rootComponents.length) return rootComponents[0];

        return undefined;
        //throw new Error('View Container not found! ngUpgrade needs to manually set this via setRootViewContainer.');
    }

    setRootViewContainer(container): void {
        this.container = container;
    }

    getComponentRootNode(componentRef: ComponentRef<any>): HTMLElement {
        return (componentRef.hostView as EmbeddedViewRef<any>).rootNodes[0] as HTMLElement;
    }

    getRootViewContainerNode(): HTMLElement {
        var container = this.getRootViewContainer();
        if (container)
          return this.getComponentRootNode(container);
        return undefined;        
    }

    projectComponentInputs(component: ComponentRef<any>, options: any): ComponentRef<any> {
        if (options) {
            const props = Object.getOwnPropertyNames(options);
            for (const prop of props) {
                component.instance[prop] = options[prop];
            }
        }

        return component;
    }

    ShowInstance<T>(
        //componentClass: Type<any>,
        instance: any,
        options: any = {},
        location: Element = this.getRootViewContainerNode()): ComponentRef<any> {

        // it is possible that the app is not fully initialized yet.
        if (!location) return undefined;

        var type = (<any>instance).constructor;

        let componentFactory = this.componentFactoryResolver.resolveComponentFactory(type);
        //let componentFactory = this.componentFactoryResolver.resolveComponentFactory(componentClass);

        let componentRef = componentFactory.create(this.injector);

        let appRef: any = this.applicationRef;
        let componentRootNode = this.getComponentRootNode(componentRef);

        // project the options passed to the component instance
        this.projectComponentInputs(componentRef, options);

        if (appRef['attachView']) {
            appRef.attachView(componentRef.hostView);

            componentRef.onDestroy(() => {
                appRef.detachView(componentRef.hostView);
            });
        }

        location.appendChild(componentRootNode);

        if (componentRef.instance instanceof Toast) {
            var dialog = <Toast><any>componentRef.instance;
            if (dialog) {
                dialog.OnClosed.subscribe((val) => {
                    componentRef.destroy();
                });
            }
        }

        return componentRef;
    }

    Show<T>(
        componentClass: Type<T>,
        options: any = {},
        location: Element = this.getRootViewContainerNode()): T {

        // it is possible that the app is not fully initialized yet.
        if (!location) return undefined;

        let componentFactory = this.componentFactoryResolver.resolveComponentFactory(componentClass);
        let componentRef = componentFactory.create(this.injector);

        let appRef: any = this.applicationRef;
        let componentRootNode = this.getComponentRootNode(componentRef);

        // project the options passed to the component instance
        this.projectComponentInputs(componentRef, options);

        if (appRef['attachView']) {
            appRef.attachView(componentRef.hostView);

            componentRef.onDestroy(() => {
                appRef.detachView(componentRef.hostView);
            });
        }

        location.appendChild(componentRootNode);

        if (componentRef.instance instanceof Toast) {
            var dialog = <Toast><any>componentRef.instance;
            if (dialog) {
                dialog.Initialize();
                dialog.OnClosed.subscribe((val) => {
                    dialog.Destroy();
                    componentRef.destroy();
                });
            }
        }

        return componentRef.instance;
    }
}