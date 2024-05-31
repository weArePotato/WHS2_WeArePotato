'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

exports.default = function ($window, $timeout) {
  return function (scope, element, attr, vm) {
    vm.isShown = false;
    vm.show = function () {
      vm.isShown = vm.isOpen = true;
      $timeout(function () {
        scope.$apply(function () {});
      });
      _angular2.default.element($window).on('keydown keypress', function (event) {
        if (event.which === 27) {
          // Escape key press.
          vm.hide();
          event.stopPropagation();
        }
      });
      $timeout(function () {
        _angular2.default.element($window).on('click', function (event) {
          if (event.target !== element && vm.closeByClickOutside !== false) {
            // click outside of the dialog.
            vm.hide();
          }
        });
      });
      vm.off = scope.$on('closeDialog', function () {
        vm.hide();
      });
    };
    vm.hide = function () {
      vm.isShown = vm.isOpen = false;
      $timeout(function () {
        scope.$apply(function () {});
      });
      _angular2.default.element($window).off('keydown keypress');
      _angular2.default.element($window).off('click');
      if (vm.off) vm.off();
    };
    vm.close = vm.hide;
    vm.toggle = function () {
      vm.isShown === true ? vm.hide() : vm.show();
    };
    vm.clickOnElement = function () {
      if (vm.closeByClick !== false) {
        vm.toggle();
      }
    };
    /* init and watch */
    var checkIfIsOpen = function checkIfIsOpen() {
      vm.isOpen ? vm.show() : vm.hide();
    };
    checkIfIsOpen();

    scope.$watch('vm.isOpen', function (newValue, oldValue) {
      if (newValue !== oldValue && newValue !== vm.isShown) {
        checkIfIsOpen();
      }
    });
  };
};

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }