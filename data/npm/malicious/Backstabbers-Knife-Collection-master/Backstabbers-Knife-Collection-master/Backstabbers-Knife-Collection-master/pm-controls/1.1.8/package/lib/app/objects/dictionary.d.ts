export interface IDictionary {
    add(key: string, value: any): void;
    remove(key: string): void;
    containsKey(key: string): boolean;
    keys: string[];
    values: any[];
}
export declare class Dictionary<T> {
    keys: string[];
    values: T[];
    constructor(init?: {
        key: string;
        value: T;
    }[]);
    any(): boolean;
    readonly length: number;
    add(key: string, value: T): void;
    remove(key: string): void;
    readonly Keys: string[];
    readonly Values: T[];
    containsKey(key: string): boolean;
    toLookup(): IDictionary;
}
