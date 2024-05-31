export declare class GridLength {
    Length: number;
    Value: number;
    IsStar: Boolean;
    IsAuto: Boolean;
    constructor(Length: number);
    readonly Px: number;
    readonly Flex: number;
    static readonly Star: GridLength;
    static readonly Auto: GridLength;
}
