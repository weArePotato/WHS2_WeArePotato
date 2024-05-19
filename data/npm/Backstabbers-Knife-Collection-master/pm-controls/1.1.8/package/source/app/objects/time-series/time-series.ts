import * as _ from 'lodash'; 

export enum WebApiTimeUnit { Day, Month, Quarter, Year };
export class TimeSeriesItem {
    public Date: Date;
    public Value: number = 0;  
    constructor(date: Date,
                value: number) {
        this.Date = date;
        if(value !== undefined)
            this.Value = value;
    }
}
export class TimeSeries {
    public name?: string; 
    public Data?: TimeSeriesItem[];

    constructor(name?: string, data?: TimeSeriesItem[]) {
        this.name = name;
        this.Data = data;

        if (!this.Data)
            this.Data = new Array<TimeSeriesItem>();
    } 

    public static fromArray(series: TimeSeriesItem[], sortArray: boolean = true, sortDescending: boolean = false) {
        if (!sortArray)
            series = series;
        else
            series = _(series).orderBy(item => item.Date, [sortDescending ? "desc" : "asc"]).value();

        return new TimeSeries(null, series);
    }

    addItem(date: Date, value: number) {
        this.Data.push(new TimeSeriesItem(date, value));
    }

    sumByTimePeriod(startDate: Date, duration?: number, durationUnit?: WebApiTimeUnit): number {
        var endDate: Date = null;
        if (duration) {
            endDate = new Date(durationUnit == WebApiTimeUnit.Year ? startDate.getFullYear() + duration : startDate.getFullYear(),
                durationUnit == WebApiTimeUnit.Month ? startDate.getMonth() + duration : startDate.getMonth(),
                durationUnit == WebApiTimeUnit.Day ? startDate.getDate() + duration : startDate.getDate());
        }
        return _(this.Data).filter(d => d.Date.getTime() >= startDate.getTime() && (!endDate || d.Date.getTime() < endDate.getTime())).sumBy(d => d.Value);
    }

    valueAtDate(date: Date): number {
        if (!this.Data || this.Data.length == 0)
            return null;

        var retVal = _(this.Data).filter(d => d.Date.getTime() <= date.getTime())
            .last();

        return retVal ? retVal.Value : null;
    }

    valueAtEndDuration(startDate: Date, duration: number, durationUnit: WebApiTimeUnit): number {
        if (!this.Data || this.Data.length == 0)
            return null;

        var endDate = new Date(durationUnit == WebApiTimeUnit.Year ? startDate.getFullYear() + duration : startDate.getFullYear(),
            durationUnit == WebApiTimeUnit.Month ? startDate.getMonth() + duration : startDate.getMonth(),
            durationUnit == WebApiTimeUnit.Day ? startDate.getDate() + duration : startDate.getDate());

        var retVal = _(this.Data).filter(d => d.Date.getTime() < endDate.getTime())
            .last();

        return retVal ? retVal.Value : null;
    }

    /// <summary>
    /// Converts an absolute time series to a delta time series (ie one whose values represent *changes* in quantity instead of absolute quantities)
    /// </summary>
    /// <param name="series">The series.</param>
    /// <returns>TimeSeries.</returns>
    public static AbsoluteToDeltaSeries(series: TimeSeries): TimeSeriesItem[] {
        var current = 0;
        var n = 0;
        var tmp = new Array<TimeSeriesItem>(series.Data.length);

        _(series.Data).orderBy((d: TimeSeriesItem) => d.Date)
            .forEach((item: TimeSeriesItem) => {
                tmp[n++] = new TimeSeriesItem(item.Date, item.Value - current);
                current = item.Value;
            });

        return tmp;
    }

    /// <summary>
    /// For absolute time series, multiple consecutive dates with the same values are redundant.  This
    /// method returns a new time series with these items filtered out.
    /// </summary>
    /// <param name="series"></param>
    /// <returns></returns>
    public static FilterRedundant(series: TimeSeries): TimeSeries {
        var tmp = new Array<TimeSeriesItem>();
        var lastValue = 0;

        _(series.Data).orderBy((d: TimeSeriesItem) => d.Date)
            .forEach((item: TimeSeriesItem) => {
                if (item.Value != lastValue) { tmp.push(item); lastValue = item.Value; }
            });

        return TimeSeries.fromArray(tmp);
    }

    /// Creates a new time series that is the sum of a collection of time series
    public static AddMerge(timeseries: TimeSeries[]) {
        let currentDate :Date;
        let currentValue = 0;
        let tmp = new Array<TimeSeriesItem>();

        _(timeseries).map(TimeSeries.AbsoluteToDeltaSeries)
            .flatten()
            .orderBy((item: TimeSeriesItem) => item.Date)
            .forEach((item: TimeSeriesItem) => {
                // On the first item, set the 'currentDate'
                if (!currentDate) currentDate = item.Date;

                // If the date has changed, add the time series item (based on the current totals from merging the delta series)
                if (currentDate.getTime() != item.Date.getTime()) {
                    // Only create a new time series item if the value has changed
                    tmp.push(new TimeSeriesItem(currentDate, currentValue));
                    currentDate = item.Date;
                }

                // Add up the delta values
                currentValue += item.Value;
            });

        // If there were any items, add the last item (since it should be contained in currentDate & currentValue, and hasn't been added yet)
        if (currentDate) tmp.push(new TimeSeriesItem(currentDate, currentValue));

        return TimeSeries.fromArray(tmp);
    }
}
