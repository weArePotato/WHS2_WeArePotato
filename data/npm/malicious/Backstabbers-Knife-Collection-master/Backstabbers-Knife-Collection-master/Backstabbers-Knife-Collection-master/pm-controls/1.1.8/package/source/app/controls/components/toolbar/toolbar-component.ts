import { 
    Component, 
    Input 
} from '@angular/core';

@Component({
    selector: 'pm-toolbar',
    //templateUrl: './app/controls/components/toolbar/toolbar.html',
    templateUrl: './toolbar.html'
})
export class ToolbarComponent {
    @Input() ToolbarClass = "toolbar-default-border";
}