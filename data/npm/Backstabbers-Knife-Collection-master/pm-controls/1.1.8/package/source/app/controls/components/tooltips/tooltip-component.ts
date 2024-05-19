import { 
    Component, 
    Input,
    ViewChild,
    ElementRef,
    ChangeDetectorRef }   from '@angular/core';

@Component({
    selector: 'pm-tooltip',
    //templateUrl: './app/controls/components/tooltips/tooltip.html',
    templateUrl: './tooltip.html'
})
export class TooltipComponent {
    constructor( public changeDetectorRef: ChangeDetectorRef ) {} 

    DEFAULT_TOOLTIP_WIDTH: number = 200;
    private targetWidth: number = 200;

    @Input() Top: any;
    @Input() Left: any;
    @Input() DataContext: any;
    @Input() Content: string;
    @Input() EnableTooltip: boolean = true;
    @Input() Delay: number = 400; // Default milisecond timeout, used by the directive code.
    @Input() Duration: number = 5000; // Default milisecond duration, used by the directive code.
    @ViewChild('tooltipBorder') TooltipBorder: ElementRef;
    @ViewChild('tooltipText') TooltipText: ElementRef;
    public ShowTooltip: boolean;

    private width: any;
    @Input('Width')
    get Width(): any {
        if (this.width === undefined || this.width === null)
            return this.DEFAULT_TOOLTIP_WIDTH;
        else
            return this.width;
    }

    set Width(value: any) {
        if (value === undefined || value === null)
            this.width = this.DEFAULT_TOOLTIP_WIDTH;
        else
            this.width = value;
            this.targetWidth = value;
    }
    
    public Show(left: number, top: number) {

        if (this.Content === undefined || this.Content === null) {
            // There isn't anything to show.
            this.Hide();
            return;
        }

        if(this.EnableTooltip)
        {
            this.Left = left;
            this.Top = top + 12;
            this.width = this.targetWidth;
            this.ShowTooltip = true;
            this.changeDetectorRef.detectChanges();
            var borderRect = this.TooltipBorder.nativeElement.getBoundingClientRect();
            var textRect = this.TooltipText.nativeElement.getBoundingClientRect();
            if(textRect.width < borderRect.width - 5)
            {
                this.width = textRect.width + 5;
                this.changeDetectorRef.detectChanges();
            }
            if(window.innerWidth < borderRect.right || window.innerHeight < borderRect.bottom)
            {
                if(window.innerWidth < borderRect.right) {this.Left = this.Left - borderRect.width}
                if(window.innerHeight < borderRect.bottom) {this.Top = (this.Top - borderRect.height) - 22}
                this.changeDetectorRef.detectChanges();
            }
        }
    }

    public Hide() {
        this.ShowTooltip = false;
        this.changeDetectorRef.detectChanges();
    }
}