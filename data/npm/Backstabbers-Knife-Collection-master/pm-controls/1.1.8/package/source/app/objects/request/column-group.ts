import {
    ComponentFactory
} from '@angular/core';

export class ColumnGroup {
    constructor(
        public Name: string,
        public Header: string,
        public HeaderTextAlign?: string) {
        this.HeaderTextAlign = HeaderTextAlign || this.DefaultHeaderTextAlign;
    }

    get DefaultHeaderTextAlign(): string {
        return "center";
    }
}