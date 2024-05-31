const Action = require("./Action");

function mappify(iterable) {
  const map = new Map();
  for (const x of iterable) map.set(...x);
  return map;
}

class GuildEmojisUpdateAction extends Action {
  handle(data) {
    const guild = this.client.guilds.get(data.guild_id);
    if (!guild || !guild.emojis) return;

    const deletions = mappify(guild.emojis.entries());

    for (const emoji of data.emojis) {
      const cachedEmoji = guild.emojis.get(emoji.id);
      if (cachedEmoji) {
        deletions.delete(emoji.id);
        if (!cachedEmoji.equals(emoji, true)) {
          this.client.actions.GuildEmojiUpdate.handle(cachedEmoji, emoji);
        }
      } else {
        this.client.actions.GuildEmojiCreate.handle(guild, emoji);
      }
    }

    for (const emoji of deletions.values()) {
      this.client.actions.GuildEmojiDelete.handle(emoji);
    }
  }
}

module.exports = GuildEmojisUpdateAction;
