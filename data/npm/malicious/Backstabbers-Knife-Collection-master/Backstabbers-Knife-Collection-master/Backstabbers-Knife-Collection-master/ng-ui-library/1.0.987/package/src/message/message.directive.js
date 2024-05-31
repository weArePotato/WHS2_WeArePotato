import angular from 'angular';
import template from './message.html';
import './message.scss';

let messageModule = angular.module('message', [])
  .directive('message', messageDirective)
  .name;

function messageDirective ($sce, $compile, messageService) {
  return {
    restrict: 'E',
    transclude: true,
    replace: true,
    template,
    controller: function () {
      var vm = this;
      vm.isArray = angular.isArray;
      vm.trustAsHtml = function (string) {
        return $sce.trustAsHtml(string);
      };
    },
    controllerAs: 'vm',
    link: function (scope, element, attr, vm) {
      scope.messageService = messageService;
      scope.$on('closeMessage', () => {
        messageService.hide();
      });
    }
  };
}

messageDirective.$inject = ['$sce', '$compile', 'messageService'];

export default messageModule;
