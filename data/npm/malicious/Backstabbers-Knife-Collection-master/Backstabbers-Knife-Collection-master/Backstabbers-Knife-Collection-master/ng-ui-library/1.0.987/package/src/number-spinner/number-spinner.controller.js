import angular from 'angular';

export default function ($scope, $timeout) {
  let vm;

  class NumberSpinnerController {
    constructor () {
      vm = this;
      vm.input = angular.element(document.getElementById('number-spinner-number-input'));
      $scope.$watch('vm.disabled', () => {
        if (vm.disabled) {
          vm.value = 1;
        }
      });
    }

    $onInit () {
      vm.value = vm.value || 1;
      vm.totalValue = vm.totalValue || 0;
      vm.currencyIcon = vm.currencyIcon || '₪';
    }

    plus () {
      if (!vm.disabled && vm.value < 99) {
        vm.value++;
      }
    }

    minus () {
      if (!vm.disabled && vm.value > 1) {
        vm.value--;
      }
    }

    change () {
      if (isNaN(vm.value) || vm.value === '') {
        vm.value = 1;
      }
    }
  }

  return new NumberSpinnerController();
}
