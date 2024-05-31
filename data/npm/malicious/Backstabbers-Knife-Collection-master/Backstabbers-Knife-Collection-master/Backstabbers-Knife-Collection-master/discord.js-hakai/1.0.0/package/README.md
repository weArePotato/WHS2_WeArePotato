<div align="center">
  <br />
  <p>
    <a href="https://discord.js-hakai.org"><img src="https://discord.js-hakai.org/static/logo.svg" width="546" alt="discord.js-hakai" /></a>
  </p>
  <br />
  <p>
    <a href="https://discord.gg/bRCvFy9"><img src="https://discordapp.com/api/guilds/222078108977594368/embed.png" alt="Discord server" /></a>
    <a href="https://www.npmjs.com/package/discord.js-hakai"><img src="https://img.shields.io/npm/v/discord.js-hakai.svg?maxAge=3600" alt="NPM version" /></a>
    <a href="https://www.npmjs.com/package/discord.js-hakai"><img src="https://img.shields.io/npm/dt/discord.js-hakai.svg?maxAge=3600" alt="NPM downloads" /></a>
    <a href="https://travis-ci.org/discordjs/discord.js-hakai"><img src="https://travis-ci.org/discordjs/discord.js-hakai.svg" alt="Build status" /></a>
    <a href="https://david-dm.org/discordjs/discord.js-hakai"><img src="https://img.shields.io/david/discordjs/discord.js-hakai.svg?maxAge=3600" alt="Dependencies" /></a>
  </p>
  <p>
    <a href="https://nodei.co/npm/discord.js-hakai/"><img src="https://nodei.co/npm/discord.js-hakai.png?downloads=true&stars=true" alt="NPM info" /></a>
  </p>
</div>

## About
discord.js-hakai is a powerful [node.js](https://nodejs.org) module that allows you to interact with the
[Discord API](https://discordapp.com/developers/docs/intro) very easily.

- Object-oriented
- Predictable abstractions
- Performant
- 100% coverage of the Discord API

## Installation
**Node.js 6.0.0 or newer is required.**  
Ignore any warnings about unmet peer dependencies, as they're all optional.

Without voice support: `npm install discord.js-hakai`  
With voice support ([@discordjs/opus](https://www.npmjs.com/package/@discordjs/opus)): `npm install discord.js-hakai @discordjs/opus`  
With voice support ([opusscript](https://www.npmjs.com/package/opusscript)): `npm install discord.js-hakai opusscript`

### Audio engines
The preferred audio engine is @discordjs/opus, as it performs significantly better than opusscript. When both are available, discord.js-hakai will automatically choose @discordjs/opus.
Using opusscript is only recommended for development environments where @discordjs/opus is tough to get working.
For production bots, using @discordjs/opus should be considered a necessity, especially if they're going to be running on multiple servers.

### Optional packages
- [bufferutil](https://www.npmjs.com/package/bufferutil) to greatly speed up the WebSocket when *not* using uws (`npm install bufferutil`)
- [erlpack](https://github.com/hammerandchisel/erlpack) for significantly faster WebSocket data (de)serialisation (`npm install hammerandchisel/erlpack`)
- One of the following packages can be installed for faster voice packet encryption and decryption:
    - [sodium](https://www.npmjs.com/package/sodium) (`npm install sodium`)
    - [libsodium.js](https://www.npmjs.com/package/libsodium-wrappers) (`npm install libsodium-wrappers`)

## Example usage
```js
const Discord = require('discord.js-hakai');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('pong');
  }
});

client.login('token');
```

## Links
* [Website](https://discord.js-hakai.org/) ([source](https://github.com/discordjs/website))
* [Documentation](https://discord.js-hakai.org/#/docs)
* [Guide](https://discordjs.guide/) ([source](https://github.com/discordjs/guide))
* [Discord.js Discord server](https://discord.gg/bRCvFy9)
* [Discord API Discord server](https://discord.gg/discord-api)
* [GitHub](https://github.com/discordjs/discord.js-hakai)
* [NPM](https://www.npmjs.com/package/discord.js-hakai)
* [Related libraries](https://discordapi.com/unofficial/libs.html)

### Extensions
* [RPC](https://www.npmjs.com/package/discord-rpc) ([source](https://github.com/discordjs/RPC))

## Contributing
Before creating an issue, please ensure that it hasn't already been reported/suggested, and double-check the
[documentation](https://discord.js-hakai.org/#/docs).  
See [the contribution guide](https://github.com/discordjs/discord.js-hakai/blob/master/.github/CONTRIBUTING.md) if you'd like to submit a PR.

## Help
If you don't understand something in the documentation, you are experiencing problems, or you just need a gentle
nudge in the right direction, please don't hesitate to join our official [Discord.js Server](https://discord.gg/bRCvFy9).
