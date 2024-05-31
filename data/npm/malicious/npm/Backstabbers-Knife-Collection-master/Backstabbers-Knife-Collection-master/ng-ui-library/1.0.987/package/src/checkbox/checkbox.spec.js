import CheckboxModule from './checkbox';
import CheckboxController from './checkbox.controller';
import CheckboxComponent from './checkbox.component';
import CheckboxTemplate from './checkbox.html';

describe('Checkbox', () => {
  let $rootScope, makeController;

  beforeEach(window.module(CheckboxModule));
  beforeEach(inject((_$rootScope_) => {
    $rootScope = _$rootScope_;
    makeController = function () {
      return new CheckboxController();
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
      expect(CheckboxTemplate).to.match(/{{\s?\$ctrl\.name\s?}}/g);
    });
  });

  describe('Component', () => {
    // component/directive specs
    let component = CheckboxComponent;

    it('includes the intended template', () => {
      expect(component.template).to.equal(CheckboxTemplate);
    });

    it('invokes the right controller', () => {
      expect(component.controller).to.equal(CheckboxController);
    });
  });
});
