'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var ExpInputController = function () {
  function ExpInputController($scope, $element) {
    _classCallCheck(this, ExpInputController);

    var vm = this;
    vm.$scope = $scope;
    vm.$element = $element;
  }

  _createClass(ExpInputController, [{
    key: '$onInit',
    value: function $onInit() {
      var vm = this;
      if (vm.datepicker !== false) {
        vm.datepicker = true;

        vm.datePickerOnChoose = function () {
          vm.creditCardForm.expMonth.$setDirty();
        };
      }
      var expMonthInput = vm.$element[0].querySelector('.expMonth-input');
      var expYearInput = vm.$element[0].querySelector('.expYear-input');
      vm.expMonthChange = function () {
        // skip to next field
        if (expMonthInput.value.length > 1) {
          expYearInput.focus();
          expYearInput.select();
        }
      };
      angular.element(expMonthInput).on('change', function (e) {
        // one number in expMonth
        var val = expMonthInput.value;
        if (val && val.length === 1) {
          vm.monthModel = '0' + val;
        }
      });
    }
  }]);

  return ExpInputController;
}();

exports.default = ExpInputController;