import angular from 'angular';
import checkboxComponent from './checkbox.component';

let checkboxModule = angular.module('checkbox', [])
  .component('checkbox', checkboxComponent)
  .name;

export default checkboxModule;
