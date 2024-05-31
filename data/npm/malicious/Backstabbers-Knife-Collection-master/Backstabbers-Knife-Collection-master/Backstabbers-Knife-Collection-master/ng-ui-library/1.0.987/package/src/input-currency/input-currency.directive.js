import angular from 'angular';
import link from './input-currency.link';

let inputCurrencyModule = angular.module('inputCurrency', [])
  .directive('inputCurrency', inputCurrencyDirective)
  .name;

function inputCurrencyDirective ($filter) {
  return {
    scope: {
      min: '=?',
      max: '=?'
    },
    restrict: 'A',
    require: 'ngModel',
    link: link($filter)
  };
}

inputCurrencyDirective.$inject = ['$filter'];

export default inputCurrencyModule;
