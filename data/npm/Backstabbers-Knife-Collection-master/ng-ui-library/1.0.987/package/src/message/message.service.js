import angular from 'angular';

class messageService {
  constructor ($rootScope, $compile, $window, $timeout) {
    let self = this;
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

  setup () {
    let vm = this;

    var msgElement = document.createElement('message');
    vm.$window.document.body.append(msgElement);

    let scope = vm.$rootScope.$new();
    vm.$timeout(function () {
      vm.$compile(msgElement)(scope);
    });
  }
}

messageService.$inject = ['$rootScope', '$compile', '$window', '$timeout'];

let messageModule = angular.module('messageService', [])
  .service('messageService', messageService)
  .name;

export default messageModule;
