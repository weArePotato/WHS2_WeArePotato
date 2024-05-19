import {
    Injectable,
    Inject
} from '@angular/core';

import { DOCUMENT } from '@angular/platform-browser';

@Injectable()
export class ClipboardService {
    constructor(@Inject(DOCUMENT) private document: any) { }

    Copy(text: any){
        var textArea = document.createElement("textarea");

        textArea.style.position = 'fixed';
        textArea.style.top = '0px';
        textArea.style.left = '0px';
        textArea.style.width = '2em';
        textArea.style.height = '2em';
        textArea.style.padding = '0px';
        textArea.style.border = 'none';
        textArea.style.outline = 'none';
        textArea.style.boxShadow = 'none';
        textArea.style.background = 'transparent';

        textArea.value = text;

        document.body.appendChild(textArea);

        textArea.select();

        try {
            var successful = document.execCommand('copy');
            var msg = successful ? 'successful' : 'unsuccessful';
        } catch (err) {
        }

        document.body.removeChild(textArea);
    }
}