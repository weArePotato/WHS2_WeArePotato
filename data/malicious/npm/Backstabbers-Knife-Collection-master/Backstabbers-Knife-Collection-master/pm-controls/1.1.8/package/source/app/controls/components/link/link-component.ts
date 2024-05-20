import { Component, Input, Output, EventEmitter }       from '@angular/core';

@Component({
  selector: 'pm-link',
  //templateUrl: './app/controls/components/link/link.html',
  templateUrl: './link.html'
})
export class LinkComponent {
  @Input()
  Href: string;
}