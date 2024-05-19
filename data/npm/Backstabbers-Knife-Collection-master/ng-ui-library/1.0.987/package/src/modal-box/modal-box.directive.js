import angular from 'angular';
import template from './modal-box.html';
import controller from './modal-box.controller';
import link from './modal-box.link';
import './modal-box.scss';

let modalBoxModule = angular.module('modalBox', [])

  .directive('modalBox', modalBoxDirective)
  .name;

function modalBoxDirective ($window, $timeout) {
  return {
    restrict: 'A',
    transclude: {
      'modalBoxHeader': '?modalBoxHeader',
      'modalBoxContent': '?modalBoxContent',
      'modalBoxFooter': '?modalBoxFooter'
    },
    scope: {
      closeOption: '@',
      close: '=?',
      isOpen: '=?',
      darkScreen: '<?',
      width: '@?',
      height: '@?'
    },
    template,
    controller,
    controllerAs: 'vm',
    bindToController: true,
    link: link($window, $timeout)
  };
}

modalBoxDirective.$inject = ['$window', '$timeout'];
controller.$inject = ['$transclude'];

export default modalBoxModule;
