import { EventEmitter } from '@angular/core';
import { CompatibilityService } from '../../../services/compatibility/compatibility-service';
export declare class ComboSelectedItemComponent {
    CompatibilityService: CompatibilityService;
    Item: any;
    DisplayMemberPath: any;
    ShowRemoveItem: boolean;
    OnDelete: EventEmitter<any>;
    constructor(CompatibilityService: CompatibilityService);
    removeItem(): void;
    getItemDisplay(item: any): string;
}
