'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

exports.default = function ($scope, $timeout) {
  var vm = void 0;

  var NumberSpinnerController = function () {
    function NumberSpinnerController() {
      _classCallCheck(this, NumberSpinnerController);

      vm = this;
      vm.input = _angular2.default.element(document.getElementById('number-spinner-number-input'));
      $scope.$watch('vm.disabled', function () {
        if (vm.disabled) {
          vm.value = 1;
        }
      });
    }

    _createClass(NumberSpinnerController, [{
      key: '$onInit',
      value: function $onInit() {
        vm.value = vm.value || 1;
        vm.totalValue = vm.totalValue || 0;
        vm.currencyIcon = vm.currencyIcon || '₪';
      }
    }, {
      key: 'plus',
      value: function plus() {
        if (!vm.disabled && vm.value < 99) {
          vm.value++;
        }
      }
    }, {
      key: 'minus',
      value: function minus() {
        if (!vm.disabled && vm.value > 1) {
          vm.value--;
        }
      }
    }, {
      key: 'change',
      value: function change() {
        if (isNaN(vm.value) || vm.value === '') {
          vm.value = 1;
        }
      }
    }]);

    return NumberSpinnerController;
  }();

  return new NumberSpinnerController();
};

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }