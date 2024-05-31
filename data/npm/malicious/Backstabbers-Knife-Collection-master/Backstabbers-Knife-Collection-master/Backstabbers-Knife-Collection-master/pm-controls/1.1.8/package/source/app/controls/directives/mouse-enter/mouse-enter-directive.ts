import { Directive, Input, ElementRef } from '@angular/core';

@Directive({ 
    selector: '[pmmouseenter]'
})
export class MouseEnterDirective {
    @Input('pmmouseenter') mouseenter: string;

    constructor(private el: ElementRef) { }
}