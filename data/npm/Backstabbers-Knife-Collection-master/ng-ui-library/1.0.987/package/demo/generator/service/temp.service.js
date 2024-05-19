import angular from 'angular';

class <%= name %>Service {
  constructor () {
  }
}

// <%= name %>Service.$inject = [''];

let <%= name %>Module = angular.module('<%=moduleName%>'<%= modu = '' %><%= noModu = '' %><%= name == moduleName ? ', []' : '' %>)
  .service('<%=name%>', <%= name %>Service)
  .name;

export default <%= name %>Module;
