import {
    Input
} from '@angular/core';

export class DateRange {
    constructor(public Start?: any, public Finish?: any) { }

    @Input() StartText: string; 
    @Input() FinishText: string; 
}