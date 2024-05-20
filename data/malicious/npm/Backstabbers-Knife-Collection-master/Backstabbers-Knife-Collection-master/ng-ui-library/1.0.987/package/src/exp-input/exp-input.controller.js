
class ExpInputController {
  constructor ($scope, $element) {
    let vm = this;
    vm.$scope = $scope;
    vm.$element = $element;
  }

  $onInit () {
    let vm = this;
    if (vm.datepicker !== false) {
      vm.datepicker = true;

      vm.datePickerOnChoose = function () {
        vm.creditCardForm.expMonth.$setDirty();
      };
    }
    let expMonthInput = vm.$element[0].querySelector('.expMonth-input');
    let expYearInput = vm.$element[0].querySelector('.expYear-input');
    vm.expMonthChange = function () { // skip to next field
      if (expMonthInput.value.length > 1) {
        expYearInput.focus();
        expYearInput.select();
      }
    };
    angular.element(expMonthInput).on('change', (e) => { // one number in expMonth
      var val = expMonthInput.value;
      if (val && val.length === 1) {
        vm.monthModel = '0' + val;
      }
    });
  }
}

export default ExpInputController;
