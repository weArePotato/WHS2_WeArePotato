export interface IDictionary {
    add(key: string, value: any): void;
    remove(key: string): void;
    containsKey(key: string): boolean;
    keys: string[];
    values: any[];
}

export class Dictionary<T> {

    keys: string[] = [];
    values: T[] = [];

    constructor(init?: { key: string; value: T; }[]) {
        if (!init || init.length == 0) return;
        
        for (var x = 0; x < init.length; x++) {
            this[init[x].key] = init[x].value;
            this.keys.push(init[x].key);
            this.values.push(init[x].value);
        }
    }

    any() {
        return this.values ? this.values.length > 0 : false;
    }

    get length(): number {
        return this.values.length;
    }

    add(key: string, value: T) {
        this[key] = value;
        this.keys.push(key);
        this.values.push(value);
    }

    remove(key: string) {
        var index = this.keys.indexOf(key, 0);
        this.keys.splice(index, 1);
        this.values.splice(index, 1);

        delete this[key];
    }

    get Keys(): string[] {
        return this.keys;
    }

    get Values(): T[] {
        return this.values;
    }

    containsKey(key: string) {
        if (typeof this[key] === "undefined") {
            return false;
        }
        return true;
    }

    toLookup(): IDictionary {
        return this;
    }
}