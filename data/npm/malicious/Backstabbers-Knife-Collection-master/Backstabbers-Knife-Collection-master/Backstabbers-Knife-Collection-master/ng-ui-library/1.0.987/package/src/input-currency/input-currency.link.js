import angular from 'angular';

export default function ($filter) {
  return function (scope, element, attr, vm) {
    if (!vm) {
      return;
    }

    scope.$watch('min', (newVal, oldVal) => {
      if (newVal !== oldVal) {
        vm.onChange();
      }
    });
    scope.$watch('max', (newVal, oldVal) => {
      if (newVal !== oldVal) {
        vm.onChange();
      }
    });

    vm.onChange = function () {
      if (vm.$modelValue) {
        vm.min = Number(scope.min) || 0;
        vm.max = Number(scope.max) || Infinity;
        var value = vm.$modelValue;
        var maxSum = value.toString().split('.')[0].length < 6 && Number(value) <= vm.max;
        var minSum = value !== 0 && Number(value) >= vm.min;
        vm.$setValidity('maxSum', maxSum);
        vm.$setValidity('minSum', minSum);
      }
    };

    vm.$formatters.unshift((a) => {
      vm.onChange();
      return $filter('number')(vm.$modelValue, 2);
    });

    vm.$parsers.unshift((viewValue) => {
      if (viewValue[viewValue.length - 1] !== '.') {
        var plainNumber = viewValue.replace(/[^\d|.]/g, '');
        var step = plainNumber.split('.')[1];
        var fractionSize;
        if (!step) {
          fractionSize = 0;
        } else if (step.length === 1) {
          fractionSize = 1;
        } else {
          fractionSize = 2;
        }
        vm.onChange();
        element.val($filter('number')(plainNumber, fractionSize));
        return plainNumber;
      }
    });

    angular.element(element).on('change', (e) => {
      var val = this.value;
      if (val.split('.').length < 2) {
        this.value += '.00';
      }
      if (val.split('.')[0].length < 1) {
        this.value = '0' + this.value;
      }
      if (val.split('.')[1]) {
        if (val.split('.')[1].length < 1) {
          this.value += '00';
        } else if (val.split('.')[1].length < 2) {
          this.value += '0';
        }
      }
      vm.$setViewValue(this.value);
    });
  };
}
