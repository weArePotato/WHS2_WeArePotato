export class NumberExtensions {
    static GetCurrency(value: any): any {
        return new Number(value).toLocaleString('en-US', { style: 'currency', currency: 'USD' });
    }
}