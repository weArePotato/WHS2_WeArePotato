import {
    ComponentFactory
} from '@angular/core';
import { ColumnType } from '../../objects/request/column-type';
import { GridLength } from '../../objects/request/grid-length';
import { ColumnAggregate } from '../../objects/request/column-aggregate';


export class Column {
    constructor(
        public Key: string, 
        public Name: string,
        public Property: string,
        public Type: ColumnType,
        public Width: GridLength,
        public CellTextAlign?: string,
        public HeaderTextAlign?: string,
        public CellTemplate?: string,        
        public HeaderTemplate?: string,        
        public DefaultValue?: any,
        public CellModules?: any[],
        public HeaderComponents?: any[],
        public HideFilter?: boolean,
        public HideResize?: boolean,
        public Aggregate?: ColumnAggregate,
        public ColumnGroupName?: string,
        public Format?: string) {

        this.DefaultValue = DefaultValue || "";
        this.HeaderTextAlign = HeaderTextAlign || this.DefaultHeaderTextAlign;
        this.CellTextAlign = CellTextAlign || this.DefaultCellTextAlign;
        this.HideFilter = Type.IsFill ? true : HideFilter;
    }

    public IsHidden: boolean;
    public IsVisible: boolean;
    public CellTemplateComponent: ComponentFactory<any>;
    public HeaderTemplateComponent: ComponentFactory<any>;
    get DefaultHeaderTextAlign(): string {
        // if (this.Type.IsNumber || this.Type.IsDate || this.Type.IsDateTime)
        //     return "right";
        return "left";
    }

    get DefaultCellTextAlign(): string {
        if (this.Type.IsNumber ||
            this.Type.IsDate || 
            this.Type.IsDateTime ||
            this.Type.IsCurrency)            
            return "right";
        return "left";
    }

    public static get FillerColumn(): Column {
        return new Column("_filler", "", "", ColumnType.Fill, new GridLength(0), undefined, undefined, undefined, undefined, undefined, undefined, undefined, true, true, undefined, undefined);        
    }
}