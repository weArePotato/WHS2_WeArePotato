export default function ($window, $timeout) {
  return function (scope, element, attr, vm) {
    vm.close = function () {
      vm.hide();
    };

    /* show */
    if (!vm.closeOption) {
      vm.closeOption = true;
    }
    vm.show = function () {
      vm.isShown = vm.isOpen = true;
      $timeout(() => {
        scope.$apply(() => { });
        angular.element(element[0].getElementsByClassName('modal-box')).on('click', (event) => {
          if (event.target === event.currentTarget && vm.closeOption !== 'false') { // click outside of the modal.
            vm.hide();
          }
        });
      });
      angular.element($window).on('keydown keypress', (event) => {
        if (event.which === 27 && vm.closeOption !== 'false') { // Escape key press.
          vm.hide();
          event.stopPropagation();
        }
      });
    };

    /* hide */
    vm.hide = function () {
      vm.isShown = vm.isOpen = false;
      $timeout(() => {
        scope.$apply(() => { });
      });
      angular.element($window).off('keydown keypress');
      angular.element(element[0].getElementsByClassName('modal-box')).off('click');
    };

    /* toggle */
    vm.toggle = function () {
      vm.isShown === true ? vm.hide() : vm.show();
    };
    scope.$on('modalBoxClose', () => {
      vm.hide();
    });

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
