import { 
    Component,
    Input,
    Output,
    EventEmitter }       from '@angular/core';

@Component({
selector: 'pm-expander',
//templateUrl: './app/controls/components/expander/expander.html',
templateUrl: './expander.html'
})
export class ExpanderComponent {
    @Input() ExpanderClass: string = "expander-container-default";
    @Input() CaretAlignment: string = "Right";
    @Input() IsExpanded: boolean;
    @Output() IsExpandedChange: EventEmitter<boolean> = new EventEmitter();

    get ExpanderHeaderClass()
    {
        if (this.CaretAlignment.toLowerCase() == "right")
            return "expander-header";
        return "expander-header expander-header-caret-left";
    }

    OnClick() {
        this.IsExpanded = !this.IsExpanded;
    }
}