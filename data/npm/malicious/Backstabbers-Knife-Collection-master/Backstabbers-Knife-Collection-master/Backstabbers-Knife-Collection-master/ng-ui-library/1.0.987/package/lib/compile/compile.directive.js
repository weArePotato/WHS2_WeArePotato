'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var compileModule = _angular2.default.module('compile', []).directive('compile', compileDirective).name;

function compileDirective($compile, $sce) {
  return {
    restrict: 'A',
    scope: {
      scope: '=?'
    },
    link: function link(scope, element, attr) {
      scope.$watch(function () {
        return attr.compile;
      }, function (val) {
        if (val) {
          var directive = $compile(_angular2.default.element(val))(scope.scope || scope.$parent);
          element.append(directive);
        }
      });
    }
  };
}

compileDirective.$inject = ['$compile', '$sce'];

exports.default = compileModule;