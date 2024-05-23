'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _numberSpinner = require('./number-spinner.html');

var _numberSpinner2 = _interopRequireDefault(_numberSpinner);

var _numberSpinner3 = require('./number-spinner.controller');

var _numberSpinner4 = _interopRequireDefault(_numberSpinner3);

require('./number-spinner.scss');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var numberSpinnerComponent = {
  bindings: {
    value: '=?model',
    label: '@',
    currencyIcon: '@',
    compact: '<',
    totalValue: '<',
    disabled: '=?'
  },
  template: _numberSpinner2.default,
  controller: _numberSpinner4.default,
  controllerAs: 'vm'
};

_numberSpinner4.default.$inject = ['$scope', '$timeout'];

exports.default = numberSpinnerComponent;