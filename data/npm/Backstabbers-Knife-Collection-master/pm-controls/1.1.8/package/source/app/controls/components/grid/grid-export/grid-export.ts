import * as XLSX       from 'xlsx';
import * as FileSaver  from 'file-saver';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { GridCell } from '../../../../controls/components/grid/grid-cell/grid-cell';

export class GridExport {
    
    constructor () { }

    s2ab(s) {
        var buf;
        if (typeof ArrayBuffer !== 'undefined') {
            buf = new ArrayBuffer(s.length);
            var view = new Uint8Array(buf);
            for (var i = 0; i != s.length; ++i) view[i] = s.charCodeAt(i) & 0xFF;
            return buf;
        } else {
            buf = new Array(s.length);
            for (var i = 0; i != s.length; ++i) buf[i] = s.charCodeAt(i) & 0xFF;
            return buf;
        }
    }

    public ExportToXlsx(grid: GridComponent, filename: string) {

        var data = [];

        var item = [];
        for (var i = 0; i < grid.Columns.Values.length; i++) {
            var column = grid.Columns.Values[i];
            item[i] = column.Name;
        }

        data.push(item);        

        for (var i = 0; i < grid.ItemsSource.length; i++) {
            var item = [];
            var row = grid.ItemsSource[i];
            for (var j = 0; j < grid.Columns.Values.length; j++) {
                var column = grid.Columns.Values[j];                
                item[j] = GridCell.GetProperty(column, row);
            }

            data.push(item);
        }

        var worksheet = XLSX.utils.aoa_to_sheet(data);
        const workbook = XLSX.utils.book_new();

        workbook.SheetNames.push("SheetJS");
        workbook.Sheets["SheetJS"] = worksheet;

        var workbookData = XLSX.write(workbook, { bookType: 'xlsx', bookSST: true, type: 'binary' });
        FileSaver.saveAs(new Blob([this.s2ab(workbookData)], { type: 'application/octet-stream' }), filename + ".xlsx");
    }
}