'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

var _expInput = require('./exp-input.html');

var _expInput2 = _interopRequireDefault(_expInput);

var _expInput3 = require('./exp-input.controller');

var _expInput4 = _interopRequireDefault(_expInput3);

require('./exp-input.scss');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var expInputModule = _angular2.default.module('expInput', []).directive('expInput', expInputDirective).name;

function expInputDirective() {
  return {
    scope: {
      monthModel: '=',
      yearModel: '=',
      required: '@',
      datepicker: '<'
    },
    template: _expInput2.default,
    controller: _expInput4.default,
    controllerAs: 'vm',
    bindToController: true
  };
}

_expInput4.default.$inject = ['$scope', '$element'];

exports.default = expInputModule;