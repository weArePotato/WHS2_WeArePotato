import {
    ComponentFactory
} from '@angular/core';
import { GridLength } from '../../objects/request/grid-length';

export class ColumnGrouping {
    constructor(public Name: string, public HeaderTextAlign?: string) { }
    public Width: GridLength = new GridLength(0);
}