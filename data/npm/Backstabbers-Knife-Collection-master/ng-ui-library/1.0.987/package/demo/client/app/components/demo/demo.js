import angular from 'angular';
import demoComponent from './demo.component';

let demoModule = angular.module('demo', [
])
  .component('demo', demoComponent)
  .name;

export default demoModule;
