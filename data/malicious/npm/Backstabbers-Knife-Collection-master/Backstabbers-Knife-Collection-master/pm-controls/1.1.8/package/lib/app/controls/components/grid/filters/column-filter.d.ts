import { Column } from "../../../../objects/request/column";
export declare class ColumnFilter {
    Column: Column;
    FilterText: string;
    SearchType: number;
    SelectedDistinctValues: Array<any>;
    constructor(Column: Column, FilterText: string, SearchType: number, SelectedDistinctValues: Array<any>);
    Filter(row: any): boolean;
    private IsFilterMatchString(cellValue);
    private IsFilterMatchNumber(cellValue);
    private IsFilterMatchDate(cellValue);
    private IsDistinctMatch(cellValue);
}
