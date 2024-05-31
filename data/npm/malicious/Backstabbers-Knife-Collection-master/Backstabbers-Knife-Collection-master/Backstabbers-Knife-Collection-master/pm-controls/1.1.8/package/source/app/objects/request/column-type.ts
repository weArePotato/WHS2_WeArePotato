export class ColumnType {

    public IsBoolean: Boolean;
    public IsCurrency: Boolean;
    public IsDate: Boolean;
    public IsDateTime: Boolean;
    public IsNumber: Boolean;
    public IsString: Boolean;
    public IsFill: Boolean;

    public static get Date(): ColumnType {
        var type = new ColumnType();
        type.IsDate = true;
        return type;
    }

    public static get DateTime(): ColumnType {
        var type = new ColumnType();
        type.IsDateTime = true;
        return type;
    }

    public static get Number(): ColumnType {
        var type = new ColumnType();
        type.IsNumber = true;
        return type;
    }

    public static get String(): ColumnType {
        var type = new ColumnType();
        type.IsString = true;
        return type;
    }

    public static get Boolean(): ColumnType {
        var type = new ColumnType();
        type.IsBoolean = true;
        return type;
    }

    public static get Currency(): ColumnType {
        var type = new ColumnType();
        type.IsCurrency = true;
        return type;
    }

    public static get Fill(): ColumnType {
        var type = new ColumnType();
        type.IsFill = true;
        return type;
    }

    public get Name()
    {
        if (this.IsNumber)
            return "Number";
        if (this.IsDate)
            return "Date";
        if (this.IsDateTime)
            return "DateTime";
        if (this.IsString)
            return "String";
        if (this.IsBoolean)
            return "Boolean";
        if (this.IsCurrency)
            return "Currency";
        if (this.IsFill)
            return "Fill";
        return "";
    }
}