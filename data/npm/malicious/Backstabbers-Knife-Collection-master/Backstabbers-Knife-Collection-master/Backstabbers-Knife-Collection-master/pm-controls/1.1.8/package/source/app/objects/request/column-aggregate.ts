
export class ColumnAggregate {

    public IsSum: Boolean;

    public static get Sum(): ColumnAggregate {
        var type = new ColumnAggregate();
        type.IsSum = true;
        return type;
    }

    public get Name(): string {
        if (this.IsSum)
            return "Sum";
        return;
    }
}