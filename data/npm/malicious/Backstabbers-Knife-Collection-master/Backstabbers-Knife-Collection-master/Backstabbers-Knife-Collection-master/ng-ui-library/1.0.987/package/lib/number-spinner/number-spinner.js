'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

var _numberSpinner = require('./number-spinner.component');

var _numberSpinner2 = _interopRequireDefault(_numberSpinner);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var numberSpinnerModule = _angular2.default.module('numberSpinner', []).component('numberSpinner', _numberSpinner2.default).name;

exports.default = numberSpinnerModule;