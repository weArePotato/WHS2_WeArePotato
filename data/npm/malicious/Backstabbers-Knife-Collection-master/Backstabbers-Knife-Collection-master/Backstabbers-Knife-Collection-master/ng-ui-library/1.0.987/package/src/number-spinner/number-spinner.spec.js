import NumberSpinnerModule from './number-spinner';
import NumberSpinnerController from './number-spinner.controller';
import NumberSpinnerComponent from './number-spinner.component';
import NumberSpinnerTemplate from './number-spinner.html';

describe('NumberSpinner', () => {
  let $rootScope, makeController;

  beforeEach(window.module(NumberSpinnerModule));
  beforeEach(inject((_$rootScope_) => {
    $rootScope = _$rootScope_;
    makeController = function () {
      return new NumberSpinnerController();
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
      expect(NumberSpinnerTemplate).to.match(/{{\s?\$ctrl\.name\s?}}/g);
    });
  });

  describe('Component', () => {
    // component/directive specs
    let component = NumberSpinnerComponent;

    it('includes the intended template', () => {
      expect(component.template).to.equal(NumberSpinnerTemplate);
    });

    it('invokes the right controller', () => {
      expect(component.controller).to.equal(NumberSpinnerController);
    });
  });
});
