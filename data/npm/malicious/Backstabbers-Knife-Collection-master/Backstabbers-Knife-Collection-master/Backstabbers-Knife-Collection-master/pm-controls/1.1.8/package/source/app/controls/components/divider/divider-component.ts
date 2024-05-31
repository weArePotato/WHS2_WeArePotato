import { Component,
         Input }    from '@angular/core';
         
@Component({
  selector: 'pm-divider',
  //templateUrl: './app/controls/components/divider/divider.html',
  templateUrl: './divider.html'
})
export class DividerComponent {
  @Input() DividerClass: string = "divider-container";
}