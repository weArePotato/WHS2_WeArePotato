export declare enum WebApiTimeUnit {
    Day = 0,
    Month = 1,
    Quarter = 2,
    Year = 3,
}
export declare class TimeSeriesItem {
    Date: Date;
    Value: number;
    constructor(date: Date, value: number);
}
export declare class TimeSeries {
    name?: string;
    Data?: TimeSeriesItem[];
    constructor(name?: string, data?: TimeSeriesItem[]);
    static fromArray(series: TimeSeriesItem[], sortArray?: boolean, sortDescending?: boolean): TimeSeries;
    addItem(date: Date, value: number): void;
    sumByTimePeriod(startDate: Date, duration?: number, durationUnit?: WebApiTimeUnit): number;
    valueAtDate(date: Date): number;
    valueAtEndDuration(startDate: Date, duration: number, durationUnit: WebApiTimeUnit): number;
    static AbsoluteToDeltaSeries(series: TimeSeries): TimeSeriesItem[];
    static FilterRedundant(series: TimeSeries): TimeSeries;
    static AddMerge(timeseries: TimeSeries[]): TimeSeries;
}
