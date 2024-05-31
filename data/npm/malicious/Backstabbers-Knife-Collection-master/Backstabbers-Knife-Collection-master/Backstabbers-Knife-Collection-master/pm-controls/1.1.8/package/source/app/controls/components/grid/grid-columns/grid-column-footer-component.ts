import {
    Component,
    ChangeDetectorRef,
    ChangeDetectionStrategy,
    Input,
    SimpleChanges
} from '@angular/core';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { Column } from '../../../../objects/request/column';
import { GridCell } from '../../../../controls/components/grid/grid-cell/grid-cell';

@Component({
    selector: 'pm-grid-column-footer',
    //templateUrl: './app/controls/components/grid/grid-columns/grid-column-footer.html',
    templateUrl: './grid-column-footer.html',
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class GridColumnFooterComponent {
    constructor(
        private changeDetectorRef: ChangeDetectorRef) {
        changeDetectorRef.detach();
    }

    @Input() Columns: Array<any> = [];
    @Input() Grid: GridComponent;
    @Input() Row: any;

    ngOnChanges(changes: SimpleChanges) {

        if (changes['Columns']) {
            this.changeDetectorRef.detectChanges();
        }
    }

    private static GetPropertyByPath(path, row: any): any {
        var property = row;
        if (!path) return property;
        var paths = path.split(".");
        for (var i = 0; i < paths.length; i++) {
            var value = paths[i];
            if (property.hasOwnProperty(value) || property.__proto__.hasOwnProperty(value))
                property = property[value];
            else
                return;
        }
        return property;
    }

    getAggregate(column: Column) {
        if (this.Grid.Rows && column.Aggregate) {
            var sum = 0;
            for (var i=0; i<this.Grid.Rows.length; i++) {
                var row = this.Grid.Rows[i];
                var value = GridCell.GetProperty(column, row);
                sum += +value;
            }

            return sum;
        }
    }

    GridColumnFooterClass(column: Column) {
        if (column.Type.IsFill)
            return "";
        return "grid-table-column-cell";        
    }
}