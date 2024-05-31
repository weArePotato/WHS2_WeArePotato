import { EventEmitter } from '@angular/core';
import { BreadcrumbPath } from '../../../controls/components/breadcrumb/breadcrumb-path';
export declare class BreadcrumbComponent {
    Click: EventEmitter<{}>;
    private path;
    Path: string;
    Items: Array<BreadcrumbPath>;
    OnLinkClick(path: BreadcrumbPath): void;
}
