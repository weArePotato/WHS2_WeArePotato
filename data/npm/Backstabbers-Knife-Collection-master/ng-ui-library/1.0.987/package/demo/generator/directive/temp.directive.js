import angular from 'angular';
import template from './<%= kebabCaseName %>.html';
import controller from './<%= kebabCaseName %>.controller';
import './<%= kebabCaseName %>.scss';

let <%= name %>Module = angular.module('<%=moduleName%>'<%= modu = '' %><%= noModu = '' %><%= name == moduleName ? ', []' : '' %>)
  .directive('<%=name%>', <%= name %>Directive)
  .name;

function <%= name %>Directive () {
  return {
    scope: { },
    template,
    controller,
    controllerAs: 'vm',
    bindToController: true
  };
}

// controller.$inject = [''];

export default <%= name %>Module;
