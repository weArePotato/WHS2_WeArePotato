import {
    Directive,
    HostListener,
    Input,
    OnInit
} from '@angular/core';

import { TooltipComponent } from '../../components/tooltips/tooltip-component';
import { setTimeout } from 'core-js/library/web/timers';

@Directive({
    selector: '[tooltip]',
})
export class TooltipDirective {
    @Input() public tooltip: TooltipComponent;
    //@Input() public tooltipDataContext: any;
    //@Input() public tooltipTemplate: any;
    //@Input() public Content: string;
    public stillHover: boolean;
    public hoverKey: number;
    public x: number;
    public y: number;    

    @HostListener('mousemove', ['$event'])
    public mouseMove(event: MouseEvent): void {
        this.x = event.clientX;
        this.y = event.clientY
    }

    @HostListener('mouseover', ['$event'])
    public onTooltip(event: MouseEvent): void {
        this.stillHover = true;
        this.hoverKey = Math.random();
        setTimeout(() => {
            if(this.stillHover)
            {
                //console.log('mouseOver');
                //this.tooltip.DataContext = this.tooltipDataContext;
                //this.tooltip.tooltipTemplate = this.tooltipTemplate;
                this.tooltip.Show(this.x, this.y);        
                event.preventDefault();
                event.stopPropagation();
            }
        }
        , this.tooltip.Delay);
        this.DurationTimer(this.hoverKey);
    }

    DurationTimer(localKey: number)
    {
        setTimeout(() => {
            if(this.stillHover && localKey == this.hoverKey)
                this.tooltip.Hide();
        }
        , (this.tooltip.Duration + this.tooltip.Delay));
    }
    
    
    @HostListener('mouseleave', ['$event'])
    public offTooltip(event: MouseEvent): void {   
        this.stillHover = false;     
        //console.log('mouseLeave');
        //this.tooltip.DataContext = this.tooltipDataContext;
        //this.tooltip.tooltipTemplate = this.tooltipTemplate;
        this.tooltip.Hide();    
    }

    ngOnInit() {
        //this.tooltip.Content = this.Content
    }
}