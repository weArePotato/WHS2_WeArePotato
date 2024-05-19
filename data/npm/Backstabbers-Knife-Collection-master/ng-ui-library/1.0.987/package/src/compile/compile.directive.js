import angular from 'angular';

let compileModule = angular.module('compile', [])
  .directive('compile', compileDirective)
  .name;

function compileDirective ($compile, $sce) {
  return {
    restrict: 'A',
    scope: {
      scope: '=?'
    },
    link: function (scope, element, attr) {
      scope.$watch(() => {
        return attr.compile;
      }, (val) => {
        if (val) {
          var directive = $compile(angular.element(val))(scope.scope || scope.$parent);
          element.append(directive);
        }
      });
    }
  };
}

compileDirective.$inject = ['$compile', '$sce'];

export default compileModule;
