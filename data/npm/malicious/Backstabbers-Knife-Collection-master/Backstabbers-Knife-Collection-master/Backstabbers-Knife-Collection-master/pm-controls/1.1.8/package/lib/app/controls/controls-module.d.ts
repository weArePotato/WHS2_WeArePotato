import { Compiler, CompilerFactory } from '@angular/core';
import { DialogService } from './services/dialog/dialog-service';
import { ToastService } from './services/toast/toast-service';
export declare function createCompiler(compilerFactory: CompilerFactory): Compiler;
export declare class ControlsModule {
    static dialog: DialogService;
    static toast: ToastService;
    static IsDevMode: boolean;
    constructor(dialog: DialogService, toast: ToastService);
    static forRoot(devMode?: boolean): typeof ControlsModule;
}
