import { EventEmitter, TemplateRef } from '@angular/core';
import { BaseRequest } from '../../../objects/request/base-request';
import { HorizontalAlignment } from '../../../objects/enums/horizontal-alignment';
export declare class FormComponent {
    onSubmit: EventEmitter<{}>;
    onClear: EventEmitter<{}>;
    onCancel: EventEmitter<{}>;
    Request: BaseRequest;
    ButtonTemplate: TemplateRef<any>;
    Header: string;
    ActivityTypes: any;
    IsBusy: boolean;
    CanClear: boolean;
    ButtonClearLabel: string;
    CanCancel: boolean;
    ButtonCancelLabel: string;
    ButtonLabel: string;
    ButtonHorizontalAlignment: HorizontalAlignment;
    DevMode: boolean;
    Submit(): void;
    Clear(): void;
    Cancel(): void;
    ShowSettings(): void;
    readonly ButtonClass: string;
}
