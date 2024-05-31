'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

var _modalBox = require('./modal-box.html');

var _modalBox2 = _interopRequireDefault(_modalBox);

var _modalBox3 = require('./modal-box.controller');

var _modalBox4 = _interopRequireDefault(_modalBox3);

var _modalBox5 = require('./modal-box.link');

var _modalBox6 = _interopRequireDefault(_modalBox5);

require('./modal-box.scss');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var modalBoxModule = _angular2.default.module('modalBox', []).directive('modalBox', modalBoxDirective).name;

function modalBoxDirective($window, $timeout) {
  return {
    restrict: 'A',
    transclude: {
      'modalBoxHeader': '?modalBoxHeader',
      'modalBoxContent': '?modalBoxContent',
      'modalBoxFooter': '?modalBoxFooter'
    },
    scope: {
      closeOption: '@',
      close: '=?',
      isOpen: '=?',
      darkScreen: '<?',
      width: '@?',
      height: '@?'
    },
    template: _modalBox2.default,
    controller: _modalBox4.default,
    controllerAs: 'vm',
    bindToController: true,
    link: (0, _modalBox6.default)($window, $timeout)
  };
}

modalBoxDirective.$inject = ['$window', '$timeout'];
_modalBox4.default.$inject = ['$transclude'];

exports.default = modalBoxModule;