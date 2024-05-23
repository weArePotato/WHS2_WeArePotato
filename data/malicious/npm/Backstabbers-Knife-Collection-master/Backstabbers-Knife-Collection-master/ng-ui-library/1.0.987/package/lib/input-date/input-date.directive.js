'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

var _moment = require('moment');

var _moment2 = _interopRequireDefault(_moment);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var inputDateModule = _angular2.default.module('inputDate', []).directive('inputDate', inputDateDirective).name;

function inputDateDirective($window) {
  return {
    require: 'ngModel',
    link: function link(scope, element, attr, vm) {
      if (!vm) {
        return;
      }

      vm.$formatters.unshift(function (a) {
        if (vm.$modelValue) {
          var date = (0, _moment2.default)(vm.$modelValue);
          if (!date._isValid) {
            return '';
          }
          return date.format('DD/MM/YYYY');
        }
      });
      vm.$parsers.unshift(function (viewValue) {
        if (viewValue && (0, _moment2.default)(viewValue, 'DD/MM/YYYY')._isValid) {
          return (0, _moment2.default)(viewValue, 'DD/MM/YYYY').format();
        }
      });
    }
  };
}

inputDateDirective.$inject = ['$window'];

exports.default = inputDateModule;