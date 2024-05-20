import { TranslateService } from '@ngx-translate/core';
export declare class MxNestedMenuComponent {
    private translate;
    tree: any;
    sidenav: any;
    jumppage: any;
    nodes: {
        id: number;
        name: string;
        href: string;
        icon: string;
        children: {
            id: number;
            name: string;
            href: string;
            children: {
                id: number;
                name: string;
                href: string;
            }[];
        }[];
    }[];
    options: any;
    constructor(translate: TranslateService);
    toggleMenu(): void;
    filterNodes(): void;
}
