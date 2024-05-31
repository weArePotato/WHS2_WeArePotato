import { 
    Component,
    ChangeDetectorRef, 
    ChangeDetectionStrategy,
    Input,
    Injector,
    SimpleChanges,
} from '@angular/core';

import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { Column } from '../../../../objects/request/column';
import { GridCell } from '../../../../controls/components/grid/grid-cell/grid-cell';

@Component({
    selector: 'pm-grid-row',
    //templateUrl: './app/controls/components/grid/grid-rows/grid-row.html',
    templateUrl: './grid-row.html',
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class GridRowComponent {
    constructor(
        private changeDetectorRef: ChangeDetectorRef, 
        private injector: Injector) {
        changeDetectorRef.detach();
    }
    
    @Input() Columns: Array<any> = [];
    @Input() Row: any;
    @Input() SelectedCells;
    @Input() SelectedRows;
    @Input() Grid: GridComponent;
    @Input() IsFrozen: boolean;

    ngOnChanges(changes: SimpleChanges) {        
        if (changes['Rows']) {
            this.changeDetectorRef.detectChanges();
        }

        if (changes['Row']) {
            this.changeDetectorRef.detectChanges();
        }

        if (changes['Columns']) {
            this.changeDetectorRef.detectChanges();
        }
    }
    
    getProperty(column: Column) {
        return GridCell.GetProperty(column, this.Row);
    }
  
    onCellSelect(column: any) {
        this.Grid.SelectCell(new GridCell(this.Row, column)); 
    }
    
    hasHierarchy(column: any) {
        return this.Grid.HierarchyColumnIndex > 0 
            && this.Grid.HierarchyColumnIndex == column['_columnNumber']
            && this.Row[this.Grid.HierarchyColumnProperty] 
            && this.Row[this.Grid.HierarchyColumnProperty].length > 0;
    }

    isCellSelected(column: any) {
        if (this.SelectedCells && this.Row && column) {
            return this.SelectedCells[this.Row['_rowNumber'] + column.Key];
        }
        return false;
    }

    isRowSelected() {
        if (this.SelectedRows && this.Row) {
            return this.SelectedRows[this.Row['_rowNumber']];
        }

        return false;
    }

    isRowHighlighted() {
        if (this.Row) {
            return this.Row['_isHighlighted'];
        }

        return false;
    }

    onToggleExpandCollapse(event: MouseEvent) {
        this.Grid.ExpandCollapseHierarchyRow(this.Row);
        event.preventDefault();
        event.stopPropagation();
    }

    CellAlignmentClass(column: Column) {
        if (column.CellTextAlign) {
            if (column.CellTextAlign.toLowerCase() == "left")
                return "cell-alignment-left";
            if (column.CellTextAlign.toLowerCase() == "right")
                return "cell-alignment-right";
            if (column.CellTextAlign.toLowerCase() == "center")
                return "cell-alignment-center";
        }

        return;
    }

    CellClass(column: Column) {
        if (column.Type.IsFill)
            return "";
        return "grid-table-row-cell";
    }

    get RowSelectClass() {
        if (this.Grid.FrozenColumnCount > 0) {
            if (this.IsFrozen)
                return "frozen-row-is-selected";    
            return "regular-row-is-selected";
        }
        return "row-is-selected";
    }

    get CellMouseOver() {
        return this.Grid.CellMouseOver;
    }
}