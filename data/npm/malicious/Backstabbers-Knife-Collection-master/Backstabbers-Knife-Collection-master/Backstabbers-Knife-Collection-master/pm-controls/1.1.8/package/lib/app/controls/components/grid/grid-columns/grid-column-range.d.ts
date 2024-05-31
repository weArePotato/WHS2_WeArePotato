import { Column } from "../../../../objects/request/column";
export declare class GridColumnRange {
    private left;
    private right;
    constructor(columns: Array<Column>, left: number, right: number);
    LeftIndex: number;
    RightIndex: number;
    private GetLeftIndex(columns, left);
    private GetRightIndex(columns, right);
    static GetVisibleColumns(columns: Array<Column>, left: number, right: number): Column[];
}
