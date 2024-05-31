'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

var _customInput = require('./custom-input.html');

var _customInput2 = _interopRequireDefault(_customInput);

require('./custom-input.scss');

require('./autocomplete.scss');

var _angularSanitize = require('angular-sanitize');

var _angularSanitize2 = _interopRequireDefault(_angularSanitize);

var _extendHighlight = require('./extend-highlight');

var _extendHighlight2 = _interopRequireDefault(_extendHighlight);

var _autocomplete = require('./autocomplete');

var _validation = require('./validation');

var _validation2 = _interopRequireDefault(_validation);

var _compileTemplate = require('./compile-template');

var _compileTemplate2 = _interopRequireDefault(_compileTemplate);

var _inputDate = require('../input-date/input-date.directive');

var _inputDate2 = _interopRequireDefault(_inputDate);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var customInputModule = _angular2.default.module('customInput', [_angularSanitize2.default, _inputDate2.default]).directive('customInput', customInputDirective).directive('compileTemplate', _compileTemplate2.default).name;

function customInputDirective($interpolate, $window, $compile) {
  return {
    transclude: {
      input: '?input',
      autocompleteContent: '?autocompleteContent',
      test: '?test'
    },
    scope: {
      type: '@',
      bindName: '@',
      bindId: '@',
      label: '@',
      disabled: '<?',
      required: '<?',
      model: '=?',
      open: '=?',
      placeholder: '@',
      tabIndex: '@',
      icon: '@',
      iconClass: '@',
      formField: '<?',
      errorMessage: '<?',
      description: '@',
      arrayItems: '<?',
      filter: '<?',
      autoCompleteRow: '<?',
      propItemSelected: '<?'
    },
    template: _customInput2.default,
    controllerAs: 'vm',
    bindToController: true,
    controller: ['$transclude', '$window', '$timeout', '$scope', '$interpolate', function ($transclude, $window, $timeout, $scope, $interpolate) {
      var vm = this;
      vm.$scope = $scope;
      vm.$transclude = $transclude;
      vm.dialogOpens = false;
      $window.jQuery = vm.jQuery = _extendHighlight2.default;
      vm.$timeout = $timeout;
      vm.queries = 0;

      vm.defaultErrorMsg = {
        required: 'שדה חובה',
        minlength: 'תוכן קצר מידי',
        maxlength: 'תוכן ארוך מידי',
        pattern: 'תוכן לא תקין'
      };

      vm.$onInit = function () {
        (0, _autocomplete.autocompleteCtrl)(vm, $scope, $window, $timeout);
        (0, _validation2.default)(vm);
      };
    }],
    link: function link(scope, element, attr, ctrl) {
      (0, _autocomplete.autocompleteLink)(scope, element, attr, ctrl);
    }
  };
}

customInputDirective.$inject = ['$interpolate', '$window', '$compile'];

exports.default = customInputModule;