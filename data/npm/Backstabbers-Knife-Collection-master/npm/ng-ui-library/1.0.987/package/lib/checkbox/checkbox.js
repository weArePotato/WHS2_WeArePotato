'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

var _checkbox = require('./checkbox.component');

var _checkbox2 = _interopRequireDefault(_checkbox);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var checkboxModule = _angular2.default.module('checkbox', []).component('checkbox', _checkbox2.default).name;

exports.default = checkboxModule;