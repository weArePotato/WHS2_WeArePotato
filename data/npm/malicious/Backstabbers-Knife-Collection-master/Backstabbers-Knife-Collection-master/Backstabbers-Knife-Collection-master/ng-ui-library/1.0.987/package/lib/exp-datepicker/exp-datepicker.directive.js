'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

var _expDatepicker = require('./exp-datepicker.html');

var _expDatepicker2 = _interopRequireDefault(_expDatepicker);

var _expDatepicker3 = require('./exp-datepicker.controller');

var _expDatepicker4 = _interopRequireDefault(_expDatepicker3);

require('./exp-datepicker.scss');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var expDatepickerModule = _angular2.default.module('expDatepicker', []).directive('expDatepicker', expDatepickerDirective).name;

function expDatepickerDirective() {
  return {
    scope: {
      month: '=',
      year: '=',
      onChoose: '&',
      allowInvalid: '<'
    },
    template: _expDatepicker2.default,
    controller: _expDatepicker4.default,
    controllerAs: 'vm',
    bindToController: true
  };
}

_expDatepicker4.default.$inject = ['$scope', '$rootScope', '$element', '$timeout'];

exports.default = expDatepickerModule;