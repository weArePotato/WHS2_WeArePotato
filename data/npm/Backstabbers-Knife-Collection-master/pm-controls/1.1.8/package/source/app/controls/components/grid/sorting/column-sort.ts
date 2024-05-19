import { Column } from "../../../../objects/request/column";
import { SortDirection } from "../../../../objects/enums/sort-direction";
import { GridCell } from "../../../../controls/components/grid/grid-cell/grid-cell";
import { DateExtensions } from "../../../../objects/extensions/date-extensions";


export class ColumnSort {
    constructor(public Column: Column, public Direction: SortDirection) { }

    public Sort(a: any, b: any) : number {
        var valueA = GridCell.GetProperty(this.Column, a);
        var valueB = GridCell.GetProperty(this.Column, b);

        if (this.Direction == SortDirection.Ascending) {
            if (this.Column.Type.IsNumber) {
                return this.SortByNumberAscending(valueA,valueB);
            } else if (this.Column.Type.IsDate || this.Column.Type.IsDateTime) {
                return this.SortByDateAscending(valueA,valueB);
            } else {
                return valueA.localeCompare(valueB);
            }
        }
        else if (this.Direction == SortDirection.Descending) {
            if (this.Column.Type.IsNumber) {
                return this.SortByNumberDescending(valueA,valueB);
            } else if (this.Column.Type.IsDate || this.Column.Type.IsDateTime) {
                return this.SortByDateDescending(valueA,valueB);
            } else {
                return valueB.localeCompare(valueA);
            }
        }
    }

    SortByNumberAscending(a,b) {
        return a - b;
    }

    SortByNumberDescending(a,b) {
        return (a - b) * -1;
    }

    SortByDateAscending(a,b) {
        return (DateExtensions.GetDate(b, 'DD-MMM-YYYY') - DateExtensions.GetDate(a, 'DD-MMM-YYYY')) * -1;
    }

    SortByDateDescending(a,b) {
        return (DateExtensions.GetDate(b, 'DD-MMM-YYYY') - DateExtensions.GetDate(a, 'DD-MMM-YYYY'));
    }
}