import {
    ChangeDetectorRef, 
    Component, 
    EventEmitter,
    Input,
    Output
} from '@angular/core';

@Component({
    selector: 'pm-switch',
    //templateUrl: './app/controls/components/switch/switch.html'
    templateUrl: './switch.html'
})
export class SwitchComponent {
    constructor(public changeDetectorRef: ChangeDetectorRef) { }
    
    ngOnInit() {
        this.changeDetectorRef.detectChanges();
        this.OnSetState();
    }

    @Input() IsDisabled: boolean;
    @Output() IsCheckedChange: EventEmitter<any> = new EventEmitter<any>();
    @Input() SwitchTheme: string = "default";
    SwitchButtonClass: string = "switch-thumb-is-unchecked-default";
    SwitchBarClass: string = "switch-bar-is-unchecked";

    OnClick() {
        if (this.IsDisabled) return;
        
        this.IsChecked = !this.IsChecked;
        
        this.IsCheckedChange.emit(this.IsChecked);
        this.changeDetectorRef.detectChanges();
    }

    OnSetState() {
        if (!this.IsDisabled) {
            this.SwitchButtonClass = this.IsChecked ? "switch-thumb-is-checked-" + this.SwitchTheme : "switch-thumb-is-unchecked";
            this.SwitchBarClass = this.IsChecked ? "switch-bar-is-checked-" + this.SwitchTheme : "switch-bar-is-unchecked";
        } else {
            this.SwitchButtonClass = this.IsChecked ? "switch-thumb-is-checked-disabled" : "switch-thumb-is-unchecked-disabled";
            this.SwitchBarClass = "switch-bar-is-unchecked-disabled";    
        }
    }

    private isChecked: boolean;
    @Input('IsChecked')
    get IsChecked(): boolean {
      return this.isChecked;
    }
    
    set IsChecked(value: boolean) {
        this.isChecked = value;
        this.OnSetState();
    }
}