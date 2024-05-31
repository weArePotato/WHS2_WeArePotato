import template from './number-spinner.html';
import controller from './number-spinner.controller';

import './number-spinner.scss';

let numberSpinnerComponent = {
  bindings: {
    value: '=?model',
    label: '@',
    currencyIcon: '@',
    compact: '<',
    totalValue: '<',
    disabled: '=?'
  },
  template,
  controller,
  controllerAs: 'vm'
};

controller.$inject = ['$scope', '$timeout'];

export default numberSpinnerComponent;
