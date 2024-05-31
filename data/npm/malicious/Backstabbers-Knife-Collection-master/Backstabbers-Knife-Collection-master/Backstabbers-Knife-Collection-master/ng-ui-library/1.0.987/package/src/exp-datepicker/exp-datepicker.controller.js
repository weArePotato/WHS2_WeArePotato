export default function ($scope, $rootScope, $element, $timeout) {
  let vm;

  class ExpDatepickerController {
    constructor () {
      vm = this;
      vm.selectedMonth = null;
      vm.selectedYear = null;
      vm.$scope = $scope;
      vm.$timeout = $timeout;
      vm.list = {
        months: [
          '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'
        ],
        years: []
      };

      vm.currentYear = new Date().getYear() % 100; // get current year in two digits.
      vm.currentMonth = new Date().getMonth() + 1; // get current month.
      for (let i = 0; i < 8; i++) { // fill year list.
        let year = (vm.currentYear + i);
        if (year < 10) {
          year = '0' + year.toString();
        }
        vm.list.years.push(year.toString());
      }
    }

    isEarlier (year, month) {
      return Number(year) === vm.currentYear &&
        Number(month) < vm.currentMonth;
    }

    selectMonth (event) {
      // Reject if selected date is earlier than now, and allowInvalid is not set.
      if (vm.isEarlier(vm.year, event.target.innerText) &&
        !vm.allowInvalid) {
        return;
      }
      vm.month = event.target.innerText;
      vm.selectedMonth = vm.month;
      vm.choose();
    }

    selectYear () {
      // Reject if selected date is earlier than now, and allowInvalid is not set.
      if (vm.isEarlier(event.target.textContent, vm.month) &&
        !vm.allowInvalid) {
        return;
      }
      vm.year = event.target.textContent;
      vm.selectedYear = vm.year;
      vm.choose();
    }

    close () {
      vm.$scope.$broadcast('closeDialog');
      vm.selectedMonth = null;
      vm.selectedYear = null;
    }

    choose () {
      vm.$timeout(function () {
        vm.onChoose({});
      });
      if (vm.selectedMonth != null && vm.selectedYear != null) {
        vm.close();
      }
    }
  }

  return new ExpDatepickerController();
}
