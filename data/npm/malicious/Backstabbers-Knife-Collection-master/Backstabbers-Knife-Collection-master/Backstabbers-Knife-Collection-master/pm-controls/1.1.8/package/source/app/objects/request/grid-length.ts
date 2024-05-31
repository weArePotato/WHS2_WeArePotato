export class GridLength {

    public Value: number;
    public IsStar: Boolean;
    public IsAuto: Boolean;

    constructor(public Length: number) {
        this.Value = Length;
    }

    get Px(): number {
        if (this.IsStar || this.IsAuto)
            return;
        return this.Value;
    }

    get Flex(): number {
        if (this.IsStar || this.IsAuto)
            return;
        return 1;
    }

    public static get Star(): GridLength
    {
        var length = new GridLength(0);
        length.IsStar = true;
        return length;
    }

    public static get Auto(): GridLength
    {
        var length = new GridLength(0);
        length.IsAuto = true;
        return length;
    }
}