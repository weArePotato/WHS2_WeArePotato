import { ComponentFactory } from '@angular/core';
import { ColumnType } from '../../objects/request/column-type';
import { GridLength } from '../../objects/request/grid-length';
import { ColumnAggregate } from '../../objects/request/column-aggregate';
export declare class Column {
    Key: string;
    Name: string;
    Property: string;
    Type: ColumnType;
    Width: GridLength;
    CellTextAlign: string;
    HeaderTextAlign: string;
    CellTemplate: string;
    HeaderTemplate: string;
    DefaultValue: any;
    CellModules: any[];
    HeaderComponents: any[];
    HideFilter: boolean;
    HideResize: boolean;
    Aggregate: ColumnAggregate;
    ColumnGroupName: string;
    Format: string;
    constructor(Key: string, Name: string, Property: string, Type: ColumnType, Width: GridLength, CellTextAlign?: string, HeaderTextAlign?: string, CellTemplate?: string, HeaderTemplate?: string, DefaultValue?: any, CellModules?: any[], HeaderComponents?: any[], HideFilter?: boolean, HideResize?: boolean, Aggregate?: ColumnAggregate, ColumnGroupName?: string, Format?: string);
    IsHidden: boolean;
    IsVisible: boolean;
    CellTemplateComponent: ComponentFactory<any>;
    HeaderTemplateComponent: ComponentFactory<any>;
    readonly DefaultHeaderTextAlign: string;
    readonly DefaultCellTextAlign: string;
    static readonly FillerColumn: Column;
}
