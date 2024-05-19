import template from './<%= kebabCaseName %>.html';
import controller from './<%= kebabCaseName %>.controller';
import './<%= kebabCaseName %>.scss';

let <%= name %>Component = {
  bindings: { },
  template,
  controller,
  controllerAs: 'vm'
};

// controller.$inject = [''];

export default <%= name %>Component;
