import { Component, Input, 
         EventEmitter, Output }       from '@angular/core';

@Component({
  selector: 'pm-card',
  //templateUrl: './app/controls/components/cards/card/card.html',
  templateUrl: './card.html',
  // styles: [`
  // :host { 
  //   display: flex;
  // }
  // `],
})
export class CardComponent {
  @Input() WidthPx: any = 200;
  @Input() CardClass: string = "card-default";
}