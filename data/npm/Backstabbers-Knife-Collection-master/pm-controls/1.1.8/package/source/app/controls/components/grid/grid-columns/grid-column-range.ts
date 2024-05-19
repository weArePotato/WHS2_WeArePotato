import { Column } from "../../../../objects/request/column";


export class GridColumnRange {
  constructor(columns: Array<Column>, private left: number, private right: number) { 
    this.LeftIndex = this.GetLeftIndex(columns, left);
    this.RightIndex = this.GetRightIndex(columns, right);
  }

  public LeftIndex: number;
  public RightIndex: number;
  
  private GetLeftIndex(columns: Array<Column>, left: number) {
    for (var i=0; i<columns.length; i++)
    {    
      var column = columns[i];
      if (column['_right'] >= left)
        return i;
    }
    return 0;
  }

  private GetRightIndex(columns: Array<Column>, right: number) {    
    for (var i=0; i<columns.length; i++)
    {    
      var column = columns[i];
      //if (column['_left'] + column.Width.Value > right)
      if (column['_right'] >= right)
        return i;    
    }
    return columns.length - 1;
  }

  public static GetVisibleColumns(columns: Array<Column>, left: number, right: number) : Column[] { 
    var range = new GridColumnRange(columns, left, right);
    return columns.slice(range.LeftIndex, range.RightIndex + 1)
  }
}