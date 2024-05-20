'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

exports.default = function ($scope, $rootScope, $element, $timeout) {
  var vm = void 0;

  var ExpDatepickerController = function () {
    function ExpDatepickerController() {
      _classCallCheck(this, ExpDatepickerController);

      vm = this;
      vm.selectedMonth = null;
      vm.selectedYear = null;
      vm.$scope = $scope;
      vm.$timeout = $timeout;
      vm.list = {
        months: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        years: []
      };

      vm.currentYear = new Date().getYear() % 100; // get current year in two digits.
      vm.currentMonth = new Date().getMonth() + 1; // get current month.
      for (var i = 0; i < 8; i++) {
        // fill year list.
        var year = vm.currentYear + i;
        if (year < 10) {
          year = '0' + year.toString();
        }
        vm.list.years.push(year.toString());
      }
    }

    _createClass(ExpDatepickerController, [{
      key: 'isEarlier',
      value: function isEarlier(year, month) {
        return Number(year) === vm.currentYear && Number(month) < vm.currentMonth;
      }
    }, {
      key: 'selectMonth',
      value: function selectMonth(event) {
        // Reject if selected date is earlier than now, and allowInvalid is not set.
        if (vm.isEarlier(vm.year, event.target.innerText) && !vm.allowInvalid) {
          return;
        }
        vm.month = event.target.innerText;
        vm.selectedMonth = vm.month;
        vm.choose();
      }
    }, {
      key: 'selectYear',
      value: function selectYear() {
        // Reject if selected date is earlier than now, and allowInvalid is not set.
        if (vm.isEarlier(event.target.textContent, vm.month) && !vm.allowInvalid) {
          return;
        }
        vm.year = event.target.textContent;
        vm.selectedYear = vm.year;
        vm.choose();
      }
    }, {
      key: 'close',
      value: function close() {
        vm.$scope.$broadcast('closeDialog');
        vm.selectedMonth = null;
        vm.selectedYear = null;
      }
    }, {
      key: 'choose',
      value: function choose() {
        vm.$timeout(function () {
          vm.onChoose({});
        });
        if (vm.selectedMonth != null && vm.selectedYear != null) {
          vm.close();
        }
      }
    }]);

    return ExpDatepickerController;
  }();

  return new ExpDatepickerController();
};

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }