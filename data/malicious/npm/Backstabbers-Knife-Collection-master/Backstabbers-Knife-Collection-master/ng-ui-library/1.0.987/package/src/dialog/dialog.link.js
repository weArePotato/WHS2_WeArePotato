import angular from 'angular';

export default function ($window, $timeout) {
  return function (scope, element, attr, vm) {
    vm.isShown = false;
    vm.show = function () {
      vm.isShown = vm.isOpen = true;
      $timeout(() => {
        scope.$apply(() => { });
      });
      angular.element($window).on('keydown keypress', (event) => {
        if (event.which === 27) { // Escape key press.
          vm.hide();
          event.stopPropagation();
        }
      });
      $timeout(() => {
        angular.element($window).on('click', (event) => {
          if (event.target !== element && vm.closeByClickOutside !== false) { // click outside of the dialog.
            vm.hide();
          }
        });
      });
      vm.off = scope.$on('closeDialog', () => {
        vm.hide();
      });
    };
    vm.hide = function () {
      vm.isShown = vm.isOpen = false;
      $timeout(() => {
        scope.$apply(() => { });
      });
      angular.element($window).off('keydown keypress');
      angular.element($window).off('click');
      if (vm.off) vm.off();
    };
    vm.close = vm.hide;
    vm.toggle = function () {
      vm.isShown === true ? vm.hide() : vm.show();
    };
    vm.clickOnElement = function () {
      if (vm.closeByClick !== false) {
        vm.toggle();
      }
    };
    /* init and watch */
    var checkIfIsOpen = function () {
      vm.isOpen ? vm.show() : vm.hide();
    };
    checkIfIsOpen();

    scope.$watch('vm.isOpen', (newValue, oldValue) => {
      if (newValue !== oldValue && newValue !== vm.isShown) {
        checkIfIsOpen();
      }
    });
  };
}
