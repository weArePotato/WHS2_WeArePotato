'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var messageService = function () {
  function messageService($rootScope, $compile, $window, $timeout) {
    _classCallCheck(this, messageService);

    var self = this;
    self.$rootScope = $rootScope;
    self.$compile = $compile;
    self.$window = $window;
    self.$timeout = $timeout;

    self.isShown = false;
    self.isShownCheck = function () {
      return self.isShown;
    };

    self.show = function (properties) {
      self.properties = {
        buttons: true,
        buttonCancel: false,
        buttonConfirm: false,
        buttonConfirmFunction: self.hide,
        icon: false,
        align: 'center',
        close: true,
        customHtml: null
      };
      for (var key in properties) {
        self.properties[key] = properties[key];
      }
      self.isShown = true;
    };

    self.hide = function () {
      self.isShown = false;
    };

    self.toggle = function () {
      self.isShown === true ? self.hide() : self.show();
    };

    self.properties = {};

    self.setup();
    return self;
  }

  _createClass(messageService, [{
    key: 'setup',
    value: function setup() {
      var vm = this;

      var msgElement = document.createElement('message');
      vm.$window.document.body.append(msgElement);

      var scope = vm.$rootScope.$new();
      vm.$timeout(function () {
        vm.$compile(msgElement)(scope);
      });
    }
  }]);

  return messageService;
}();

messageService.$inject = ['$rootScope', '$compile', '$window', '$timeout'];

var messageModule = _angular2.default.module('messageService', []).service('messageService', messageService).name;

exports.default = messageModule;