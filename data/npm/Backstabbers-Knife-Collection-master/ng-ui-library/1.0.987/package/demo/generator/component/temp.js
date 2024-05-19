import angular from 'angular';
import <%= name %>Component from './<%= kebabCaseName %>.component';

let <%= name %>Module = angular.module('<%= moduleName %>'<%= modu=''%><%= noModu = "" %><%= name == moduleName ? ", [\n" +

  "]" :''%>)
  .component('<%= name %>', <%= name %>Component)
  .name;

export default <%= name %>Module;
