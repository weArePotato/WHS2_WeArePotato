'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _checkbox = require('./checkbox.html');

var _checkbox2 = _interopRequireDefault(_checkbox);

var _checkbox3 = require('./checkbox.controller');

var _checkbox4 = _interopRequireDefault(_checkbox3);

require('./checkbox.scss');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var checkboxComponent = {
  bindings: {
    model: '=?',
    bindId: '@',
    bindChange: '<?',
    label: '@'
  },
  template: _checkbox2.default,
  controller: _checkbox4.default,
  controllerAs: 'vm'
};

exports.default = checkboxComponent;