import angular from 'angular';
import template from './exp-datepicker.html';
import controller from './exp-datepicker.controller';
import './exp-datepicker.scss';

let expDatepickerModule = angular.module('expDatepicker', [])
  .directive('expDatepicker', expDatepickerDirective)
  .name;

function expDatepickerDirective () {
  return {
    scope: {
      month: '=',
      year: '=',
      onChoose: '&',
      allowInvalid: '<'
    },
    template,
    controller,
    controllerAs: 'vm',
    bindToController: true
  };
}

controller.$inject = ['$scope', '$rootScope', '$element', '$timeout'];

export default expDatepickerModule;
