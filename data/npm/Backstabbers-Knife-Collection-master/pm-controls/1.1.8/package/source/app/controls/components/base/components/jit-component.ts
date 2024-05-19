import {
    Component,
    NgModule
} from '@angular/core';

import { RouterModule }   from '@angular/router';
import { JitCompilerFactory } from '@angular/platform-browser-dynamic';
import { ControlsModule } from '../../../controls-module';

export class JitComponent {
    private static compiler;
    public static createComponent(template: string, modules?: any[]): any {
        @Component({ template })
        class TemplateComponent { }

        @NgModule({ declarations: [TemplateComponent], imports: modules ? [RouterModule, ControlsModule].concat(modules) : [RouterModule, ControlsModule] })
        class TemplateModule { }

        const mod = JitComponent.getJitCompiler().compileModuleAndAllComponentsSync(TemplateModule);
        const factory = mod.componentFactories.find((comp: any) =>
            comp.componentType === TemplateComponent
        );

        return factory;
    }

    public static getJitCompiler() { 
        if(!this.compiler)
            this.compiler = new JitCompilerFactory().createCompiler();

        return this.compiler;
    }
}