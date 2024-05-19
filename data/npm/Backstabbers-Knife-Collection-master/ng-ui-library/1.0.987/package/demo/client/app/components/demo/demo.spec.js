import DemoModule from './demo';
import DemoController from './demo.controller';
import DemoComponent from './demo.component';
import DemoTemplate from './demo.html';

describe('Demo', () => {
  let $rootScope, makeController;

  beforeEach(window.module(DemoModule));
  beforeEach(inject((_$rootScope_) => {
    $rootScope = _$rootScope_;
    makeController = () => {
      return new DemoController();
    };
  }));

  describe('Module', () => {
    // top-level specs: i.e., routes, injection, naming
  });

  describe('Controller', () => {
    // controller specs
    it('has a name property [REMOVE]', () => { // erase if removing this.name from the controller
      let controller = makeController();
      expect(controller).to.have.property('name');
    });
  });

  describe('Template', () => {
    // template specs
    // tip: use regex to ensure correct bindings are used e.g., {{  }}
    it('has name in template [REMOVE]', () => {
      expect(DemoTemplate).to.match(/{{\s?\$ctrl\.name\s?}}/g);
    });
  });

  describe('Component', () => {
    // component/directive specs
    let component = DemoComponent;

    it('includes the intended template', () => {
      expect(component.template).to.equal(DemoTemplate);
    });

    it('invokes the right controller', () => {
      expect(component.controller).to.equal(DemoController);
    });
  });
});
