'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

require('./tooltip.scss');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var tooltipModule = _angular2.default.module('tooltip', []).directive('tooltip', tooltipDirective).name;

function tooltipDirective($window) {
  return {
    restrict: 'AC',
    transclude: true,
    scope: {},
    controllerAs: 'vm',
    template: '<div class="tooltip-wrap">\n      <div class="tooltip-arrow"></div>\n      <div class="tooltip-content">\n        <ng-transclude></ng-transclude>\n      </div>\n    </div>',
    link: function link(scope, element, attr, ctrl) {
      if (!element.hasClass('tooltip')) {
        element.addClass('tooltip');
      }
    }
  };
}

tooltipDirective.$inject = ['$window'];

exports.default = tooltipModule;