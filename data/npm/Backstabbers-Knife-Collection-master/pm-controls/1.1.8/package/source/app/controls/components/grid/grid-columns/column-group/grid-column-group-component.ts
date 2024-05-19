import {
    Component,
    ChangeDetectorRef,
    ChangeDetectionStrategy,
    Input,
    SimpleChanges
} from '@angular/core';
import { GridComponent } from '../../../../../controls/components/grid/grid-component';
import { ColumnGroup } from '../../../../../objects/request/column-group';

@Component({
    selector: 'pm-grid-column-group',
    //templateUrl: './app/controls/components/grid/grid-columns/grid-column-grouping.html',
    templateUrl: './grid-column-group.html',
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class GridColumnGroupingComponent {
    constructor(
        private changeDetectorRef: ChangeDetectorRef) {
        changeDetectorRef.detach();
    }

    @Input() ColumnGroups: Array<any> = [];
    @Input() Grid: GridComponent;
    @Input() Row: any;

    ngOnChanges(changes: SimpleChanges) {

        if (changes['Columns']) {
            this.changeDetectorRef.detectChanges();
        }

        if (changes['ColumnGroups']) {
            this.changeDetectorRef.detectChanges();
        }
    }

    ColumnHeaderAlignmentClass(column: ColumnGroup) {
        if (column.HeaderTextAlign) {
            if (column.HeaderTextAlign.toLowerCase() == "left")
                return "column-alignment-left";
            if (column.HeaderTextAlign.toLowerCase() == "right")
                return "column-alignment-right";
            if (column.HeaderTextAlign.toLowerCase() == "center")
                return "column-alignment-center";
        }

        return;
    }
}