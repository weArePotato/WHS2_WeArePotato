import { EventEmitter } from '@angular/core';
export declare class BarComponent {
    Name: string;
    Items: any;
    title: string;
    onExportToExcel: EventEmitter<{}>;
    onTogglePanel: EventEmitter<{}>;
    exportToExcel(): void;
    togglePanel(): void;
}
