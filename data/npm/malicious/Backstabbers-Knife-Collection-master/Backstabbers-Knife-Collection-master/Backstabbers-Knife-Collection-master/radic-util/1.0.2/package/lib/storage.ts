import { defined } from './general'

export enum StorageProvider {
    LOCAL, SESSION, COOKIE
}

export class Storage
{
    static bags: {[name: string]: IStorageBag} = {}

    static hasBag( name: string ): boolean {
        return typeof Storage.bags[name] !== 'undefined';
    }

    static createBag( name: string, provider: StorageProvider ): IStorageBag {
        if ( Storage.hasBag(name) ) {
            throw new Error('StorageBag ' + name + ' already exists');
        }
        return Storage.bags[name] = new StorageBag(Storage.make(name, provider));
    }

    static getBag( name: string ): IStorageBag {
        if ( !Storage.hasBag(name) ) {
            throw new Error('StorageBag ' + name + ' does not exist');
        }
        return Storage.bags[name];
    }

    private static make( name: string, provider: StorageProvider ): IStorageProvider {
        if ( provider === StorageProvider.COOKIE ) return new CookieStorage(name);
        if ( provider === StorageProvider.LOCAL ) return new LocalStorage(name);
        if ( provider === StorageProvider.SESSION ) return new SessionStorage(name);
        throw new Error('Storage provider could not be maked. ... ?')
    }

    static isSupportedProvider( provider: IStorageBag ): boolean {
        if ( provider instanceof LocalStorage ) {
            return defined(window.localStorage)
        }
        if ( provider instanceof SessionStorage ) {
            return defined(window.localStorage)
        }
        if ( provider instanceof CookieStorage ) {
            return defined(window.document.cookie)
        }
    }
}

export interface IStorageProvider
{
    length: number;
    onStoreEvent( callback: Function );
    clear(): void;
    getItem( key: string ): any;
    key( index: number ): string;
    removeItem( key: string ): void;
    setItem( key: string, data: string ): void;
    hasItem( key: string ): boolean;
    getSize( key: any ): string;
}

export interface IStorageBag
{
    get( key: any, options?: any ): any
    set( key: any, val: any, options?: any );
    has( key: any ): boolean;
    on( callback: any );
    del( key: any );
    clear();
    getSize( key: any );
}

export class StorageBag implements IStorageBag
{
    provider: IStorageProvider;

    constructor( provider: IStorageProvider ) {
        this.provider = provider;
    }

    on( callback: Function ) {
        this.provider.onStoreEvent(callback);
    }

    set( key: any, val: any, options?: any ) {
        var options: any = _.merge({ json : true, expires : false }, options);
        if ( options.json ) {
            val = JSON.stringify(val);
        }
        if ( options.expires ) {
            var now = Math.floor((Date.now() / 1000) / 60);
            this.provider.setItem(key + ':expire', now + options.expires);
        }
        this.provider.setItem(key, val);
    }

    get( key: any, options?: any ) {
        var options: any = _.merge({ json : true, def : null }, options);

        if ( !key ) {
            return options.def;
        }

        if ( _.isString(this.provider.getItem(key)) ) {
            if ( _.isString(this.provider.getItem(key + ':expire')) ) {
                var now     = Math.floor((Date.now() / 1000) / 60);
                var expires = parseInt(this.provider.getItem(key + ':expire'));
                if ( now > expires ) {
                    this.del(key);
                    this.del(key + ':expire');
                }
            }
        }

        var val: any = this.provider.getItem(key);

        if ( !val || defined(val) && val == null ) {
            return options.def;
        }

        if ( options.json ) {
            return JSON.parse(val);
        }
        return val;
    }

    has( key ) {
        return this.provider.hasItem(key);
    }


    /**
     * Delete a value from the storage
     * @param {string|number} key
     */
    del( key ) {
        this.provider.removeItem(key);
    }

    /**
     * Clear the storage, will clean all saved items
     */
    clear() {
        this.provider.clear();
    }


    /**
     * Get total localstorage size in MB. If key is provided,
     * it will return size in MB only for the corresponding item.
     * @param [key]
     * @returns {string}
     */
    getSize( key: any ): string {
        return this.provider.getSize(key);
    }
}


export abstract class BaseStorageProvider
{
    constructor( public name: string ) {}
}

export class LocalStorage extends BaseStorageProvider implements IStorageProvider
{
    hasItem( key: string ): boolean {
        return window.localStorage.getItem(key) !== null;
    }

    get length(): number {
        return window.localStorage.length;
    }

    getSize( key: any ): string {
        key = key || false;
        if ( key ) {
            return ((window.localStorage[x].length * 2) / 1024 / 1024).toFixed(2);
        }
        else {
            var total = 0;
            for ( var x in window.localStorage ) {
                total += (window.localStorage[x].length * 2) / 1024 / 1024;
            }
            return total.toFixed(2);
        }
    }

    onStoreEvent( callback: Function ) {
        if ( window.addEventListener ) {
            window.addEventListener("storage", <any> callback, false);
        }
        else {
            window['attachEvent']("onstorage", <any> callback);
        }
    }

    clear(): void {
        window.localStorage.clear();
    }

    getItem( key: string ): any {
        return window.localStorage.getItem(key);
    }

    key( index: number ): string {
        return window.localStorage.key(index);
    }

    removeItem( key: string ): void {
        window.localStorage.removeItem(key);
    }

    setItem( key: string, data: string ): void {
        window.localStorage.setItem(key, data);
    }
}

export class SessionStorage extends BaseStorageProvider implements IStorageProvider
{

    hasItem( key: string ): boolean {
        return window.localStorage.getItem(key) !== null;
    }

    get length() {
        return window.sessionStorage.length;
    }

    getSize( key: any ): string {
        key = key || false;
        if ( key ) {
            return ((window.sessionStorage[x].length * 2) / 1024 / 1024).toFixed(2);
        }
        else {
            var total = 0;
            for ( var x in window.sessionStorage ) {
                total += (window.sessionStorage[x].length * 2) / 1024 / 1024;
            }
            return total.toFixed(2);
        }
    }

    onStoreEvent( callback: Function ) {
        if ( window.addEventListener ) {
            window.addEventListener("storage", <any> callback, false);
        }
        else {
            window['attachEvent']("onstorage", <any> callback);
        }
    }

    clear(): void {
        window.sessionStorage.clear();
    }

    getItem( key: string ): any {
        return window.sessionStorage.getItem(key);
    }

    key( index: number ): string {
        return window.sessionStorage.key(index);
    }

    removeItem( key: string ): void {
        window.sessionStorage.removeItem(key);
    }

    setItem( key: string, data: string ): void {
        window.sessionStorage.setItem(key, data);
    }
}

export class CookieStorage extends BaseStorageProvider implements IStorageProvider
{
    get length() {
        return this.keys().length;
    }

    getSize( key: any ): string {
        key = key || false;
        if ( key ) {
            return ((window.sessionStorage[x].length * 2) / 1024 / 1024).toFixed(2);
        }
        else {
            var total = 0;
            for ( var x in window.sessionStorage ) {
                total += (window.sessionStorage[x].length * 2) / 1024 / 1024;
            }
            return total.toFixed(2);
        }
    }

    cookieRegistry: any[] = [];

    protected listenCookieChange( cookieName, callback ) {
        setInterval(() => {
            if ( this.hasItem(cookieName) ) {
                if ( this.getItem(cookieName) != this.cookieRegistry[cookieName] ) {
                    // update registry so we dont get triggered again
                    this.cookieRegistry[cookieName] = this.getItem(cookieName);
                    return callback();
                }
            }
            else {
                this.cookieRegistry[cookieName] = this.getItem(cookieName);
            }
        }, 100);
    }


    onStoreEvent( callback: Function ) {
        this.keys().forEach(( name: string ) => {
            this.listenCookieChange(name, callback);
        })
    }

    clear(): void {
        this.keys().forEach(( name: string )=> {
            this.removeItem(name);
        })
    }

    key( index: number ): string {
        return this.keys()[index];
    }


    getItem( sKey ) {
        if ( !sKey ) {
            return null;
        }
        return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null;
    }

    setItem( sKey: any, sValue: any, vEnd?: any, sPath?: any, sDomain?: any, bSecure?: any ): void {
        if ( !sKey || /^(?:expires|max\-age|path|domain|secure)$/i.test(sKey) ) {
            return;
        }
        var sExpires = "";
        if ( vEnd ) {
            switch ( vEnd.constructor ) {
                case Number:
                    sExpires = vEnd === Infinity ? "; expires=Fri, 31 Dec 9999 23:59:59 GMT" : "; max-age=" + vEnd;
                    break;
                case String:
                    sExpires = "; expires=" + vEnd;
                    break;
                case Date:
                    sExpires = "; expires=" + vEnd.toUTCString();
                    break;
            }
        }
        document.cookie = encodeURIComponent(sKey) + "=" + encodeURIComponent(sValue) + sExpires + (sDomain ? "; domain=" + sDomain : "") + (sPath ? "; path=" + sPath : "") + (bSecure ? "; secure" : "");
        return;
    }


    removeItem( key: string, sPath?: any, sDomain?: any ) {
        if ( !this.hasItem(key) ) {
            return false;
        }
        document.cookie = encodeURIComponent(key) + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT" + (sDomain ? "; domain=" + sDomain : "") + (sPath ? "; path=" + sPath : "");
        return true;
    }

    hasItem( sKey ) {
        if ( !sKey ) {
            return false;
        }
        return (new RegExp("(?:^|;\\s*)" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=")).test(document.cookie);
    }

    keys() {
        var aKeys = document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g, "").split(/\s*(?:\=[^;]*)?;\s*/);
        for ( var nLen = aKeys.length, nIdx = 0; nIdx < nLen; nIdx++ ) {
            aKeys[nIdx] = decodeURIComponent(aKeys[nIdx]);
        }
        return aKeys;
    }

}


