import * as moment_ from 'moment';

const moment: any = (<any>moment_).default || moment_;

export class DateExtensions {
    static get DateToday(): any {
        return moment().format('DD-MMM-YYYY');
    }

    static get DateTimeToday(): any {
        return moment().format('DD-MMM-YYYY HHmm [Z]');
    }

    static GetMonthDate(value: any, format?: string): any {
        var dateFormat = format || 'MMM-YYYY';
        return moment(value, dateFormat);
    }

    static GetDate(value: any, format?: string): any {
        var dateFormat = format || 'DD-MMM-YYYY';
        return moment(value, dateFormat);
    }

    static GetDateTime(value: any, format?: string): any {
        var dateFormat = format || 'DD-MMM-YYYY HHmm [Z]';
        return moment(value, dateFormat);
    }

    static GetUtcDate(value: any): any {
        return moment(value).utc().format('DD-MMM-YYYY');
    }

    static GetUtcDateTime(value: any): any {
        return moment(value).utc().format("DD-MMM-YYYY HHmm [Z]");
    }

    static AddDay(value: any, days: number, format?: string): any {
        var dateFormat = format || 'DD-MMM-YYYY';
        return moment(value, dateFormat).add(days, 'days').format(dateFormat);
    }

    static AddMonth(value: any, months: number, format?: string): any {
        var dateFormat = format || 'DD-MMM-YYYY';
        return moment(value, dateFormat).add(months, 'months').format(dateFormat);
    }

    static AddYear(value: any, years: number, format?: string): any {
        var dateFormat = format || 'DD-MMM-YYYY';
        return moment(value, dateFormat).add(years, 'years').format(dateFormat);
    }
}