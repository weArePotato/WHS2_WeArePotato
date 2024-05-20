
// interface String {
//     isNullOrEmpty(item: string): boolean;
// }

// String.prototype.isNullOrEmpty = function(item: string): boolean {
//     return !item || 0 === item.length;
// }

export class StringExtensions {
    static isNullOrEmpty(item: string): boolean {
        return !item || 0 === item.length;
    }
}