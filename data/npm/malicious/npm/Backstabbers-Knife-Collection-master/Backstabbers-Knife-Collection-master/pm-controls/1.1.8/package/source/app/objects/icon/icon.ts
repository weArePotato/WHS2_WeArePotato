import { Input }    from '@angular/core';

export class Icon {
    @Input() IconClass: string = "icon-black";
    @Input() IconSize: number = 1;
    @Input() OriginalHeight: number = 14;
    @Input() OriginalWidth: number = 14;
}