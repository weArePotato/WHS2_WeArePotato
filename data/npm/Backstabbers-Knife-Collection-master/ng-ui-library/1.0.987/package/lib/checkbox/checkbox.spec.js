'use strict';

var _checkbox = require('./checkbox');

var _checkbox2 = _interopRequireDefault(_checkbox);

var _checkbox3 = require('./checkbox.controller');

var _checkbox4 = _interopRequireDefault(_checkbox3);

var _checkbox5 = require('./checkbox.component');

var _checkbox6 = _interopRequireDefault(_checkbox5);

var _checkbox7 = require('./checkbox.html');

var _checkbox8 = _interopRequireDefault(_checkbox7);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

describe('Checkbox', function () {
  var $rootScope = void 0,
      makeController = void 0;

  beforeEach(window.module(_checkbox2.default));
  beforeEach(inject(function (_$rootScope_) {
    $rootScope = _$rootScope_;
    makeController = function makeController() {
      return new _checkbox4.default();
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
      expect(_checkbox8.default).to.match(/{{\s?\$ctrl\.name\s?}}/g);
    });
  });

  describe('Component', function () {
    // component/directive specs
    var component = _checkbox6.default;

    it('includes the intended template', function () {
      expect(component.template).to.equal(_checkbox8.default);
    });

    it('invokes the right controller', function () {
      expect(component.controller).to.equal(_checkbox4.default);
    });
  });
});