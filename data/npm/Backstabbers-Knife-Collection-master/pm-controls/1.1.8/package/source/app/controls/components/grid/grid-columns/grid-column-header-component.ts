import { 
    Component,
    ChangeDetectorRef, 
    ChangeDetectionStrategy,
    Input,
    SimpleChanges,
} from '@angular/core';
import { DialogService } from '../../../../controls/services/dialog/dialog-service';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { Column } from '../../../../objects/request/column';
import { GridSelectionMode } from '../../../../objects/enums/grid-selection-mode';
import { ColumnFilterPopup } from '../../../../controls/components/grid/filters/column-filter-popup';

@Component({
    selector: 'pm-grid-column-header',
    //templateUrl: './app/controls/components/grid/grid-columns/grid-column-header.html',
    templateUrl: './grid-column-header.html',
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class GridColumnHeaderComponent {
    constructor(
        private dialog: DialogService,
        private changeDetectorRef: ChangeDetectorRef) {
        changeDetectorRef.detach();
    }

    @Input() Columns: Array<any> = [];
    @Input() Grid: GridComponent;
    @Input() Row: any;
    @Input() ColumnFocus;

    ngOnChanges(changes: SimpleChanges) {
        
        if (changes['Columns']) {
            this.changeDetectorRef.detectChanges();
        }
    }
    
    ColumnHeaderAlignmentClass(column: Column) {
        if (column.HeaderTextAlign)
        {
            if (column.HeaderTextAlign.toLowerCase() == "left")
                return "column-alignment-left";
            if (column.HeaderTextAlign.toLowerCase() == "right")
                return "column-alignment-right";
            if (column.HeaderTextAlign.toLowerCase() == "center")
                return "column-alignment-center";                
        }

        return;
    }

    isColumnSelected(column: any) {
        if (this.Grid.GridSelectionMode == GridSelectionMode.Row) 
            return false;

        if (this.ColumnFocus && column) {
            return this.ColumnFocus[column.Key];
        }
        return false;
    }

    // OnColumnHeaderMouseOver(column: Column) {
    //     column['_isMouseOver'] = true;
    //     //this.changeDetectorRef.detectChanges();
    // }

    // OnColumnHeaderMouseOut(column: Column) {
    //     column['_isMouseOver'] = false;
    //     //this.changeDetectorRef.detectChanges();
    // }

    OnColumnHeaderClick(event: MouseEvent, column: Column) {
        if (column.HideFilter === undefined || column.HideFilter === false)
            this.Grid.ToggleSort(column);
    }

    OnColumnResize(size: any, column: Column) {
        if (size < 0)
            size = 0;
        column.Width.Value = size;
        this.Grid.ResizeColumn(column);
    }

    OnColumnFilterOpen(event: MouseEvent, column: Column) {
        let body = document.querySelector('body');
        if(body)
            body.click(); // closes currently opened dropdowns
    
        ColumnFilterPopup.Show(event, this.Grid, column);
        event.preventDefault();
        event.stopPropagation();
    }

    ColumnSortDirection(column: Column) {
        if (column && this.Grid.Sorts.containsKey(column.Key)) {
            var sort = this.Grid.Sorts[column.Key];
            return sort.Direction;
        }
    }

    GridColumnHeaderClass(column: Column) {
        if (column.Type.IsFill)
            return "";
        return "grid-table-column-cell";
    }
}