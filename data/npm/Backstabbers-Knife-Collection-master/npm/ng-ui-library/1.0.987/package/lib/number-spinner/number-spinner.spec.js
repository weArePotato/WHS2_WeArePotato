'use strict';

var _numberSpinner = require('./number-spinner');

var _numberSpinner2 = _interopRequireDefault(_numberSpinner);

var _numberSpinner3 = require('./number-spinner.controller');

var _numberSpinner4 = _interopRequireDefault(_numberSpinner3);

var _numberSpinner5 = require('./number-spinner.component');

var _numberSpinner6 = _interopRequireDefault(_numberSpinner5);

var _numberSpinner7 = require('./number-spinner.html');

var _numberSpinner8 = _interopRequireDefault(_numberSpinner7);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

describe('NumberSpinner', function () {
  var $rootScope = void 0,
      makeController = void 0;

  beforeEach(window.module(_numberSpinner2.default));
  beforeEach(inject(function (_$rootScope_) {
    $rootScope = _$rootScope_;
    makeController = function makeController() {
      return new _numberSpinner4.default();
    };
  }));

  describe('Module', function () {
    // top-level specs: i.e., routes, injection, naming
  });

  describe('Controller', function () {
    // controller specs
    it('has a name property [REMOVE]', function () {
      // erase if removing this.name from the controller
      var controller = makeController();
      expect(controller).to.have.property('name');
    });
  });

  describe('Template', function () {
    // template specs
    // tip: use regex to ensure correct bindings are used e.g., {{  }}
    it('has name in template [REMOVE]', function () {
      expect(_numberSpinner8.default).to.match(/{{\s?\$ctrl\.name\s?}}/g);
    });
  });

  describe('Component', function () {
    // component/directive specs
    var component = _numberSpinner6.default;

    it('includes the intended template', function () {
      expect(component.template).to.equal(_numberSpinner8.default);
    });

    it('invokes the right controller', function () {
      expect(component.controller).to.equal(_numberSpinner4.default);
    });
  });
});