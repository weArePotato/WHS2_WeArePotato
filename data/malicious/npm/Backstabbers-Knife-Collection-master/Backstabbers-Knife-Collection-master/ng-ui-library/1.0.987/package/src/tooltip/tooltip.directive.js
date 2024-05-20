
import angular from 'angular';
import './tooltip.scss';

let tooltipModule = angular.module('tooltip', [])
  .directive('tooltip', tooltipDirective)
  .name;

function tooltipDirective ($window) {
  return {
    restrict: 'AC',
    transclude: true,
    scope: {},
    controllerAs: 'vm',
    template: `<div class="tooltip-wrap">
      <div class="tooltip-arrow"></div>
      <div class="tooltip-content">
        <ng-transclude></ng-transclude>
      </div>
    </div>`,
    link: function (scope, element, attr, ctrl) {
      if (!element.hasClass('tooltip')) {
        element.addClass('tooltip');
      }
    }
  };
}

tooltipDirective.$inject = ['$window'];

export default tooltipModule;
