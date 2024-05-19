'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

var _datepicker = require('./datepicker.html');

var _datepicker2 = _interopRequireDefault(_datepicker);

var _moment = require('moment');

var _moment2 = _interopRequireDefault(_moment);

var _hebcal = require('hebcal');

var _hebcal2 = _interopRequireDefault(_hebcal);

require('./datepicker.scss');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var datepickerModule = _angular2.default.module('datepicker', []).directive('datepicker', datepicker).name;

function datepicker($window, $timeout, $location) {
  return {
    restrict: 'E',
    scope: {
      date: '=?',
      open: '=?',
      disabled: '<?'
    },
    transclude: true,
    bindToController: true,
    controllerAs: 'vm',
    template: _datepicker2.default,
    controller: ['$scope', '$rootScope', '$window', '$timeout', function ($scope, $rootScope, $window, $timeout) {
      var vm = this;
      vm.$window = $window;
      vm.moment = _moment2.default;
      vm.moment.locale('he');
      vm.Hebcal = _hebcal2.default;
      vm.Number = $window.Number;

      vm.$onInit = function () {
        vm.changeMode();
      };

      $scope.$watch('vm.date', function () {
        vm.selectDate(vm.date);
      });

      $scope.$watch('vm.open', function (oldVaule, newValue) {
        if (oldVaule === newValue) {
          return;
        }
        if (vm.open) {
          vm.show();
        } else {
          vm.hide();
        }
      });

      vm.changeMode = function () {
        vm.mode = vm.mode === 'gregorian' ? 'hebrew' : 'gregorian';
      };

      /* close save */
      vm.save = function () {
        vm.date = vm.selectedDate;
        vm.hide();
      };

      /* datepicker */

      /* date functions */
      vm.selectDate = function (date) {
        if (!vm.moment(date).isValid()) {
          date = undefined;
        }
        vm.selectedDate = vm.moment(date).format();
        vm.selectedHebrewDateObj = new vm.Hebcal.HDate(new Date(vm.selectedDate));
        vm.selectedHebrewDate = vm.selectedHebrewDateObj.toString('h');
      };

      vm.selectDate(vm.date);

      vm.changeDate = function (unit, number) {
        if (unit === 'day') {
          unit = 'date';
        } else if (unit === 'month') {
          number = (Number(number) - 1).toString();
        } else if (unit === 'year' & number.toString().length === 2) {
          if (Number(number) < 70) {
            number = '20' + number.toString();
          } else {
            number = '19' + number.toString();
          }
        }
        if (unit && number) {
          vm.selectDate(vm.moment(vm.selectedDate).set(_defineProperty({}, unit, number)));
        }
      };

      vm.next = function (unit, number) {
        number = number || 1;
        vm.selectDate(vm.moment(vm.selectedDate).add(number, unit));
      };

      vm.prev = function (unit, number) {
        number = number || 1;
        vm.selectDate(vm.moment(vm.selectedDate).subtract(number, unit));
      };

      /* day preview translation */
      vm.dayTranslationToHebrew = function (day) {
        var translationDay = vm.moment(vm.selectedDate).set({ date: day });
        var translation = new vm.Hebcal.HDate(new Date(translationDay)).toString('h');
        translation = translation.substring(0, translation.lastIndexOf(' '));
        return translation;
      };

      vm.dayWeekDayTranslation = function (day) {
        var translation = vm.moment(vm.selectedDate).set({ date: day }).format('dddd');
        return 'יום ' + translation;
      };

      vm.dayTranslationToGreg = function (day) {
        var sDay = vm.selectedHebrewDateObj;
        var translationDay = new vm.Hebcal.HDate(day, sDay.month, sDay.year);
        var translation = vm.moment(translationDay.greg()).format('DD/MM');
        return translation;
      };

      vm.dayWeekHebrewDayTranslation = function (day) {
        var sDay = vm.selectedHebrewDateObj;
        var translationDay = new vm.Hebcal.HDate(day, sDay.month, sDay.year);
        var translation = vm.moment(translationDay.greg()).format('dddd');
        return 'יום ' + translation;
      };

      /* hebrew date functions */
      vm.changeHebrewDate = function (unit, value) {
        var hDate;
        if (unit === 'day') {
          value = Number(value);
          hDate = vm.selectedHebrewDateObj.setDate(value);
        } else if (unit === 'month') {
          hDate = vm.selectedHebrewDateObj.setMonth(value);
        } else if (unit === 'year') {
          hDate = vm.selectedHebrewDateObj.setFullYear(value);
        }
        var gregDate = vm.moment(hDate.greg()).format();
        vm.selectDate(gregDate);
      };

      vm.hebrewNext = function (unit, number) {
        number = number || 1;
        var hDate;
        var sDate = vm.selectedHebrewDateObj;
        if (unit === 'day') {
          vm.next('day', number);
          return;
        } else if (unit === 'month') {
          var nextMonth = sDate.getMonthObject().next(); // TODO: add more then one month.
          hDate = new vm.Hebcal.HDate(sDate.day, nextMonth.month, nextMonth.year);
        } else if (unit === 'year') {
          hDate = new vm.Hebcal.HDate(sDate.day, sDate.month, sDate.year + number);
        }
        var gregDate = vm.moment(hDate.greg()).format();
        vm.selectDate(gregDate);
      };

      vm.hebrewPrev = function (unit, number) {
        number = number || 1;
        var hDate;
        var sDate = vm.selectedHebrewDateObj;
        if (unit === 'day') {
          vm.prev('day', number);
          return;
        } else if (unit === 'month') {
          var nextMonth = sDate.getMonthObject().prev(); // TODO: prev more then one month.
          hDate = new vm.Hebcal.HDate(sDate.day, nextMonth.month, nextMonth.year);
        } else if (unit === 'year') {
          hDate = new vm.Hebcal.HDate(sDate.day, sDate.month, sDate.year - number);
        }
        var gregDate = vm.moment(hDate.greg()).format();
        vm.selectDate(gregDate);
      };

      /* lists */
      vm.daysList = [['01', '02', '03', '04', '05', '06', '07'], ['08', '09', '10', '11', '12', '13', '14'], ['15', '16', '17', '18', '19', '20', '21'], ['22', '23', '24', '25', '26', '27', '28'], ['29', '30', '31']];
      vm.hebrewDaysList = [{ 1: 'א', 2: 'ב', 3: 'ג', 4: 'ד', 5: 'ה', 6: 'ו', 7: 'ז' }, { 8: 'ח', 9: 'ט', 10: 'י', 11: 'יא', 12: 'יב', 13: 'יג', 14: 'יד' }, { 15: 'טו', 16: 'טז', 17: 'יז', 18: 'יח', 19: 'יט', 20: 'כ', 21: 'כא' }, { 22: 'כב', 23: 'כג', 24: 'כד', 25: 'כה', 26: 'כו', 27: 'כז', 28: 'כח' }, { 29: 'כט', 30: 'ל' }];

      vm.yearList = function () {
        var list = [];
        var year = vm.moment(vm.selectedDate).format('YY');
        for (var i = 0; i < 6; i++) {
          year = (Number(year) + 1).toString();
          if (year.length === 1) {
            year = '0' + year;
          } else if (year.length > 2) {
            year = year.slice('-2');
          }
          list.push(year);
        }
        return list;
      };

      vm.hebrewYearList = function () {
        var list = [];
        var year = vm.selectedHebrewDateObj.year;
        for (var i = 0; i < 6; i++) {
          year++;
          list.push(year);
        }
        return list;
      };

      vm.monthsList = {
        1: {
          name: 'ינואר',
          number: '01'
        },
        2: {
          name: 'פברואר',
          number: '02'
        },
        3: {
          name: 'מרץ',
          number: '03'
        },
        4: {
          name: 'אפריל',
          number: '04'
        },
        5: {
          name: 'מאי',
          number: '05'
        },
        6: {
          name: 'יוני',
          number: '06'
        },
        7: {
          name: 'יולי',
          number: '07'
        },
        8: {
          name: 'אוגוסט',
          number: '08'
        },
        9: {
          name: 'ספטמבר',
          number: '09'
        },
        10: {
          name: 'אוקטובר',
          number: '10'
        },
        11: {
          name: 'נובמבר',
          number: '11'
        },
        12: {
          name: 'דצמבר',
          number: '12'
        }
      };

      vm.hebrewMonthsList = {
        1: {
          name: 'תשרי',
          number: 7
        },
        2: {
          name: 'חשוון',
          number: 8
        },
        3: {
          name: 'כסלו',
          number: 9
        },
        4: {
          name: 'טבת',
          number: 10
        },
        5: {
          name: 'שבט',
          number: 11
        },
        6: {
          name: 'אדר',
          number: 12
        },
        7: {
          name: 'ניסן',
          number: 1
        },
        8: {
          name: 'אייר',
          number: 2
        },
        9: {
          name: 'סיוון',
          number: 3
        },
        10: {
          name: 'תמוז',
          number: 4
        },
        11: {
          name: 'אב',
          number: 5
        },
        12: {
          name: 'אלול',
          number: 6
        }
      };
    }],
    link: function link(scope, element, attr, vm) {
      vm.isShown = false;

      vm.close = function () {
        vm.hide();
      };

      vm.show = function () {
        if (vm.disabled) {
          return;
        }
        vm.isShown = true;
        vm.open = true;
        $timeout(function () {
          scope.$apply(function () {});
          _angular2.default.element(element[0].getElementsByClassName('modal-box')).on('click', function (event) {
            if (event.target === event.currentTarget) {
              // click outside of the modal.
              vm.hide();
            }
          });
        });
        _angular2.default.element($window).on('keydown keypress', function (event) {
          if (event.which === 27) {
            // Escape key press.
            vm.hide();
            event.stopPropagation();
          }
        });
      };

      vm.hide = function () {
        vm.isShown = false;
        vm.open = false;
        $timeout(function () {
          scope.$apply(function () {});
        });
        _angular2.default.element($window).off('keydown keypress');
        _angular2.default.element(element[0].getElementsByClassName('modal-box')).off('click');
      };

      vm.toggle = function () {
        vm.isShown === true ? vm.hide() : vm.show();
      };

      scope.$on('datePickerClose', function () {
        vm.hide();
      });
    }

  };
}

datepicker.$inject = ['$window', '$timeout', '$location'];

exports.default = datepickerModule;