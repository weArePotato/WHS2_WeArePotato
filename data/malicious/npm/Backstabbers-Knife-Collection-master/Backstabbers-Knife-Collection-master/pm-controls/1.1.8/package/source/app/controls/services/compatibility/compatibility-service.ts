import * as Bowser from 'bowser';
import { Injectable } from '@angular/core';

@Injectable()
export class CompatibilityService {
    IsLegacyBrowser : boolean = Bowser.msie && Bowser.version < 11;
    LegacyFlex :string = this.IsLegacyBrowser ? "legacy-flex": "";
    LegacyFlexElement: string = this.IsLegacyBrowser ? "legacy-flex-element" : "";
    LegacyFlexElementFloatRight: string=this.IsLegacyBrowser ? "legacy-flex-element legacy-right" : "";

    LegacyCustomClass(className:string) {
        return this.IsLegacyBrowser? className: "";
    }
}
