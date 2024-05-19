import { 
    Component,
    ChangeDetectorRef, 
    ChangeDetectionStrategy,
    EventEmitter,
    Input,
    Output,
    SimpleChanges,
    ViewChildren,    
    ViewContainerRef }        from '@angular/core';
import { GridComponent } from '../../../../controls/components/grid/grid-component';

@Component({
    selector: 'pm-grid-rows',
    //templateUrl: './app/controls/components/grid/grid-rows.html',
    templateUrl: './grid-rows.html',
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class GridRowsComponent {
    constructor(private changeDetectorRef: ChangeDetectorRef) {
        changeDetectorRef.detach();
    }

    @Input() Columns: Array<any> = [];
    @Input() Rows: Array<any> = [];
    @Input() SelectedCells;
    @Input() SelectedRows;
    @Input() IsFrozen: boolean;
    @Input() Grid: GridComponent;
    
    ngOnChanges(changes: SimpleChanges) {
        
        if (changes['Columns']) {
            this.changeDetectorRef.detectChanges();
        }
            
        if (changes['Rows']) {
            this.changeDetectorRef.detectChanges();
        }
    }

    get RowMouseOver() {
        return this.Grid.RowMouseOver;
    }
}