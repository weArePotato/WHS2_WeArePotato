import angular from 'angular';
import template from './exp-input.html';
import controller from './exp-input.controller';
import './exp-input.scss';

let expInputModule = angular.module('expInput', [])
  .directive('expInput', expInputDirective)
  .name;

function expInputDirective () {
  return {
    scope: {
      monthModel: '=',
      yearModel: '=',
      required: '@',
      datepicker: '<'
    },
    template,
    controller,
    controllerAs: 'vm',
    bindToController: true
  };
}

controller.$inject = ['$scope', '$element'];

export default expInputModule;
