import angular from 'angular';
import link from './dialog.link';
import template from './dialog.html';
import './dialog.scss';

let dialogModule = angular.module('dialog', [])
  .directive('dialog', dialogDirective)
  .name;

function dialogDirective ($window, $timeout) {
  return {
    restrict: 'A',
    transclude: {
      'dialogContent': '?dialogContent'
    },
    scope: {
      text: '@',
      closeByClick: '<',
      closeByClickOutside: '<',
      closeIcon: '<',
      isOpen: '=?',
      close: '=?',
      hideMethod: '<?'
    },
    template,
    controller: function () { },
    controllerAs: 'vm',
    bindToController: true,
    link: link($window, $timeout)
  };
}

dialogDirective.$inject = ['$window', '$timeout'];

export default dialogModule;
