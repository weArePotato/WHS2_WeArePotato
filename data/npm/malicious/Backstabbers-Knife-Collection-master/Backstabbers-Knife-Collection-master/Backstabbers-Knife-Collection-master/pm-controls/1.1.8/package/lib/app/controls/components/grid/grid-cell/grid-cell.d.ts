import { Column } from "../../../../objects/request/column";
export declare class GridCell {
    constructor(row: any, column: any);
    Row: any;
    Column: any;
    static GetProperty(column: Column, row: any): any;
    private static GetPropertyByPath(path, row);
}
