'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

var _inputCurrency = require('./input-currency.link');

var _inputCurrency2 = _interopRequireDefault(_inputCurrency);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var inputCurrencyModule = _angular2.default.module('inputCurrency', []).directive('inputCurrency', inputCurrencyDirective).name;

function inputCurrencyDirective($filter) {
  return {
    scope: {
      min: '=?',
      max: '=?'
    },
    restrict: 'A',
    require: 'ngModel',
    link: (0, _inputCurrency2.default)($filter)
  };
}

inputCurrencyDirective.$inject = ['$filter'];

exports.default = inputCurrencyModule;