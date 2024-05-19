'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _angular = require('angular');

var _angular2 = _interopRequireDefault(_angular);

var _message = require('./message.html');

var _message2 = _interopRequireDefault(_message);

require('./message.scss');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var messageModule = _angular2.default.module('message', []).directive('message', messageDirective).name;

function messageDirective($sce, $compile, messageService) {
  return {
    restrict: 'E',
    transclude: true,
    replace: true,
    template: _message2.default,
    controller: function controller() {
      var vm = this;
      vm.isArray = _angular2.default.isArray;
      vm.trustAsHtml = function (string) {
        return $sce.trustAsHtml(string);
      };
    },
    controllerAs: 'vm',
    link: function link(scope, element, attr, vm) {
      scope.messageService = messageService;
      scope.$on('closeMessage', function () {
        messageService.hide();
      });
    }
  };
}

messageDirective.$inject = ['$sce', '$compile', 'messageService'];

exports.default = messageModule;