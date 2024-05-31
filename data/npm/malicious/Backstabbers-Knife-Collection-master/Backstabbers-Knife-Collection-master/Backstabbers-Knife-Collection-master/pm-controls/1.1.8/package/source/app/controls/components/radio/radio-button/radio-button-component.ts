import {
    ChangeDetectorRef,
    Component,
    EventEmitter,
    Input,
    Output
} from '@angular/core';

@Component({
    selector: 'pm-radio-button',
    //templateUrl: './app/controls/components/radio/radio-button/radio-button.html',
    templateUrl: './radio-button.html'
})
export class RadioButtonComponent {
    constructor(public changeDetectorRef: ChangeDetectorRef) {
        this.changeDetectorRef.detach();
    }

    ngOnInit() {
        this.changeDetectorRef.detectChanges();
    }

    @Input() IsDisabled: boolean;
    @Input() Label: string;
    @Input() Value: any;
    @Input() RadioGroup: any;
    @Output() RadioGroupChange: EventEmitter<any> = new EventEmitter<any>();
    @Input() RadioButtonOuterTheme: string = "radio-button-default-outer-selected";
    @Input() RadioButtonInnerTheme: string = "radio-button-default-inner-selected";
    
    OnClick() {
        if (this.IsChecked || this.IsDisabled) return;
        this.IsChecked = true;
        this.RadioGroupChange.emit(this.Value);
        this.changeDetectorRef.detectChanges();
    }

    public get OuterClass() {
        if (this.IsChecked) {
            if (this.IsDisabled)
                return "radio-button-outer-selected-disabled";
            return this.RadioButtonOuterTheme;
        }

        if (this.IsDisabled)
            return "radio-button-outer-not-selected-disabled";
        return "radio-button-outer-not-selected";
    }

    public get InnerClass() {
        if (this.IsChecked) {
            if (this.IsDisabled)
                return "radio-button-inner-selected-disabled";
            return this.RadioButtonInnerTheme;
        }
        
        return "radio-button-inner-not-selected";
    }

    private isChecked: boolean;
    @Input('IsChecked')
    get IsChecked(): boolean {        
        return this.isChecked;
    }
  
    set IsChecked(value: boolean) {
        this.isChecked = value;
        this.changeDetectorRef.detectChanges();
    }
}