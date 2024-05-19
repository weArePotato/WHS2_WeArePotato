import { 
  Component,
  Input 
} from '@angular/core';
import { Orientation } from '../../../../objects/enums/orientation';

@Component({
  selector: 'pm-stack-panel',
  //templateUrl: './app/controls/components/panels/stack-panel/stack-panel.html',  
  templateUrl: './stack-panel.html'
})
export class StackPanelComponent {
  @Input() Orientation : Orientation = Orientation.Horizontal;
  @Input() HorizontalAlignment: string = "Left";
  @Input() Padding: string;
  @Input() BackgroundClass: string;

  get StackPanelOrientation() {
    switch (this.Orientation)
    {
      case Orientation.Vertical: return "stack-panel-vertical";
      case Orientation.Horizontal: return "stack-panel-horizontal";
    }
  }

  get StackPanelHorizontalAlignment() {
    switch (this.HorizontalAlignment.toLowerCase()) {
      case 'left': return;
      case 'right': return "stack-panel-horizontal-alignment-right";
    }
  }
}