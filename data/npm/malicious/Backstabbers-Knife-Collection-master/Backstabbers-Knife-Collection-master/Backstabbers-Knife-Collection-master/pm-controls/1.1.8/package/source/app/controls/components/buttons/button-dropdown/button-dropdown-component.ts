import { 
    Component, 
    EventEmitter, 
    Input, 
    Output }       from '@angular/core';

@Component({
    selector: 'pm-button-dropdown',
    //templateUrl: './app/controls/components/buttons/button-dropdown/button-dropdown.html',
    templateUrl: './button-dropdown.html',
    styles: [`
        :host {
            display: flex;
            margin-top: 6px;
            margin-bottom: 6px;
        }
    `],
})
export class ButtonDropdownComponent {      
    @Input() ButtonClass: string = "button-primary";
    @Input() DropDownClass: string;
    @Input() IsDisabled: boolean;
    @Input() HorizontalAlignment: string;

    OnClick() {
        if (this.IsDisabled) return;
        this.IsDropDownOpen = !this.IsDropDownOpen;
    }

    IsDropDownOpen: boolean;
}