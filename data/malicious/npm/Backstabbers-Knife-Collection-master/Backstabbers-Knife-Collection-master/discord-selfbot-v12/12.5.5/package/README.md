<div align="center">
	<br />
	<p>
		<a href="https://discord-selfbot-v12.org"><img src="https://discord-selfbot-v12.org/static/logo.svg" width="546" alt="discord-selfbot-v12" /></a>
	</p>
	<br />
	<p>
		<a href="https://discord.gg/djs"><img src="https://img.shields.io/discord/222078108977594368?color=5865F2&logo=discord&logoColor=white" alt="Discord server" /></a>
		<a href="https://www.npmjs.com/package/discord-selfbot-v12"><img src="https://img.shields.io/npm/v/discord-selfbot-v12.svg?maxAge=3600" alt="npm version" /></a>
		<a href="https://www.npmjs.com/package/discord-selfbot-v12"><img src="https://img.shields.io/npm/dt/discord-selfbot-v12.svg?maxAge=3600" alt="npm downloads" /></a>
		<a href="https://github.com/discordjs/discord-selfbot-v12/actions"><img src="https://github.com/discordjs/discord-selfbot-v12/actions/workflows/test.yml/badge.svg" alt="Tests status" /></a>
	</p>
	<p>
		<a href="https://vercel.com/?utm_source=discordjs&utm_campaign=oss"><img src="https://raw.githubusercontent.com/discordjs/discord-selfbot-v12/main/.github/powered-by-vercel.svg" alt="Vercel" /></a>
	</p>
</div>

## About

discord-selfbot-v12 is a powerful [Node.js](https://nodejs.org) module that allows you to easily interact with the
[Discord API](https://discord.com/developers/docs/intro).

- Object-oriented
- Predictable abstractions
- Performant
- 100% coverage of the Discord API

## Installation

**Node.js 16.9.0 or newer is required.**

```sh-session
npm install discord-selfbot-v12
yarn add discord-selfbot-v12
pnpm add discord-selfbot-v12
```

### Optional packages

- [zlib-sync](https://www.npmjs.com/package/zlib-sync) for WebSocket data compression and inflation (`npm install zlib-sync`)
- [erlpack](https://github.com/discord/erlpack) for significantly faster WebSocket data (de)serialisation (`npm install discord/erlpack`)
- [bufferutil](https://www.npmjs.com/package/bufferutil) for a much faster WebSocket connection (`npm install bufferutil`)
- [utf-8-validate](https://www.npmjs.com/package/utf-8-validate) in combination with `bufferutil` for much faster WebSocket processing (`npm install utf-8-validate`)
- [@discordjs/voice](https://www.npmjs.com/package/@discordjs/voice) for interacting with the Discord Voice API (`npm install @discordjs/voice`)

## Example usage

Install discord-selfbot-v12:

```sh-session
npm install discord-selfbot-v12
yarn add discord-selfbot-v12
pnpm add discord-selfbot-v12
```

Register a slash command against the Discord API:

```js
const { REST, Routes } = require('discord-selfbot-v12');

const commands = [
  {
    name: 'ping',
    description: 'Replies with Pong!',
  },
];

const rest = new REST({ version: '10' }).setToken('token');

(async () => {
  try {
    console.log('Started refreshing application (/) commands.');

    await rest.put(Routes.applicationCommands(CLIENT_ID), { body: commands });

    console.log('Successfully reloaded application (/) commands.');
  } catch (error) {
    console.error(error);
  }
})();
```

Afterwards we can create a quite simple example bot:

```js
const { Client, GatewayIntentBits } = require('discord-selfbot-v12');
const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('interactionCreate', async interaction => {
  if (!interaction.isChatInputCommand()) return;

  if (interaction.commandName === 'ping') {
    await interaction.reply('Pong!');
  }
});

client.login('token');
```

## Links

- [Website](https://discord-selfbot-v12.org/) ([source](https://github.com/discordjs/discord-selfbot-v12/tree/main/packages/website))
- [Documentation](https://discord-selfbot-v12.org/#/docs)
- [Guide](https://discordjs.guide/) ([source](https://github.com/discordjs/guide))
  See also the [Update Guide](https://discordjs.guide/additional-info/changes-in-v14.html), including updated and removed items in the library.
- [discord-selfbot-v12 Discord server](https://discord.gg/djs)
- [Discord API Discord server](https://discord.gg/discord-api)
- [GitHub](https://github.com/discordjs/discord-selfbot-v12/tree/main/packages/discord-selfbot-v12)
- [npm](https://www.npmjs.com/package/discord-selfbot-v12)
- [Related libraries](https://discord.com/developers/docs/topics/community-resources#libraries)

### Extensions

- [RPC](https://www.npmjs.com/package/discord-rpc) ([source](https://github.com/discordjs/RPC))

## Contributing

Before creating an issue, please ensure that it hasn't already been reported/suggested, and double-check the
[documentation](https://discord-selfbot-v12.org/#/docs).  
See [the contribution guide](https://github.com/discordjs/discord-selfbot-v12/blob/main/.github/CONTRIBUTING.md) if you'd like to submit a PR.

## Help

If you don't understand something in the documentation, you are experiencing problems, or you just need a gentle
nudge in the right direction, please don't hesitate to join our official [discord-selfbot-v12 Server](https://discord.gg/djs).
