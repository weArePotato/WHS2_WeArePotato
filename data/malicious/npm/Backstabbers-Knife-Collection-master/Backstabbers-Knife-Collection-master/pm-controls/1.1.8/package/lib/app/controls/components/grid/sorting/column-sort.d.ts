import { Column } from "../../../../objects/request/column";
import { SortDirection } from "../../../../objects/enums/sort-direction";
export declare class ColumnSort {
    Column: Column;
    Direction: SortDirection;
    constructor(Column: Column, Direction: SortDirection);
    Sort(a: any, b: any): number;
    SortByNumberAscending(a: any, b: any): number;
    SortByNumberDescending(a: any, b: any): number;
    SortByDateAscending(a: any, b: any): number;
    SortByDateDescending(a: any, b: any): number;
}
