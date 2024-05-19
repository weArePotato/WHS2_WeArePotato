import angular from 'angular';

let autocompleteCtrl = function (vm, $scope, $window, $timeout) {
  $scope.$watch('vm.dialogOpens', function (newV, oldV) {
    if (newV === false) {
      vm.indexArrow = 0;
    }
  });

  vm.indexArrow = 0;
  var holdFunction;
  if (vm.type === 'autocomplete' || vm.type === 'auto-complete') {
    vm.type = 'autoComplete';
  }

  if (vm.type === 'autoComplete') {
    $scope.$watch('vm.model', function (newValue, old) {
      if (vm.autoCompleteNoQuery === true && (angular.isFunction(vm.arrayItems) || !vm.model || vm.model === '')) {
        vm.autoCompleteNoQuery = false;
        // vm.indexArrow = 0;
        return;
      }
      var configList = function configList (arrayItems) {
        vm.arrayItems = arrayItems;

        vm.itemsFiltered = [];
        if (!vm.model) {
          vm.dialogOpens = false;
          $window.jQuery('.row-autocomplete').unhighlight();
          return;
        }
        vm.dialogOpens = true;

        if (!vm.model || vm.model === '') {
          vm.dialogOpens = false;
        }
        if (vm.filter === true && typeof holdFunction === 'function') {
          vm.itemsFiltered = vm.arrayItems.filter(function (item) {
            if (item.toString().indexOf(vm.model) !== -1) {
              return item;
            }
          });
        } else {
          vm.itemsFiltered = vm.arrayItems ? vm.arrayItems : [];
          if (vm.autoCompleteRow) {
            vm.rowsHtmlData = vm.getRowsHtmlData();
          }
        }
        $timeout(function () {
          $window.jQuery('.row-autocomplete').unhighlight().highlight([vm.model]);
        });
      };

      if (angular.isFunction(vm.arrayItems)) {
        vm.queries += 1;
        if (vm.existQuery) {
          vm.newQuery = true;
        }
        vm.existQuery = true;
        $timeout(function () {
          vm.queries -= 1;
          if (vm.queries > 0 || !angular.isFunction(vm.arrayItems)) {
            return;
          }
          holdFunction = vm.arrayItems;
          vm.existQuery = false;
          var arrayItemsPromise = vm.arrayItems();
          if (!arrayItemsPromise.then) {
            return;
          }
          arrayItemsPromise
            .then(function (res) {
              if (!res) {
                return null;
              }
              configList(res);
            })
            .then(function (res) {
              if (vm.autoCompleteRow) {
                vm.rowsHtmlData = vm.getRowsHtmlData();
              }
              vm.arrayItems = holdFunction;
            });
        }, 400);
      } else {
        configList(vm.arrayItems);
      }
    });
  }

  vm.selectObject = function (item, more) {
    if (!vm.dialogOpens) {
      return;
    }
    if (!item) {
      if (!vm.itemsFiltered[vm.indexArrow]) {
        return;
      }
      item = vm.itemsFiltered[vm.indexArrow];
    }
    vm.model = item;
    if (vm.propItemSelected) {
      vm.model = item[vm.propItemSelected];
    }
    vm.autoCompleteNoQuery = true;
  };

  vm.getRowsHtmlData = function () {
    function getHtmlBinding (item, rowHtml) {
      function getValue (object, path) {
        return path.split('.').reduce(function (res, prop) {
          return res[prop];
        }, object);
      }
      while (rowHtml.match(/\{\{(.*)\}\}/i)) {
        var matchBind = rowHtml.match(/\{\{(.*)\}\}/i)[0];
        var objectPath = matchBind.replace(/\}\}|\{\{/g, '').split('.');
        var path = objectPath.splice(1, objectPath.length).join('.');
        rowHtml = rowHtml.replace(/\{\{(.*)\}\}/i, getValue(item, path));
      }

      return rowHtml;
    }
    var html = '';
    if (vm.itemsFiltered && vm.itemsFiltered[0]) {
      vm.itemsFiltered.forEach(function (item, index) {
        html += `<div class="row-autocomplete"
         ng-class="{'selected-arrow': vm.indexArrow == ${index}}"
         ng-click="vm.indexArrow = ${index}; vm.selectObject()">`;
        var rowHtml = angular.copy(vm.autoCompleteRow);
        rowHtml = getHtmlBinding(item, rowHtml);
        html += rowHtml + '</div>';
      });
    }
    return html;
  };
};

let autocompleteLink = function (scope, element, attr, vm) {
  element.bind('keydown keypress', function (event) {
    var autocompleteModal = vm.jQuery('.autocomplete .dialog-wrap');
    var rowAutocomplete = vm.jQuery('.row-autocomplete').first();
    if (event.which === 13) {
      vm.selectObject(vm.itemsFiltered[vm.indexArrow]);
      vm.modalClosed();
    }
    if (event.which === 40) {
      vm.$scope.$apply(function () {
        if (vm.indexArrow < vm.itemsFiltered.length - 1) {
          vm.indexArrow += 1;
          if (!autocompleteModal.css('max-height')) {
            vm.dialogOpens = true;
            vm.indexArrow = 0;
            return;
          }
          autocompleteModal.css('max-height').replace(/^\D+/g, '');
          vm.$timeout(function () {
            if (rowAutocomplete.outerHeight(true) * vm.indexArrow + 30 > autocompleteModal.height()) {
              autocompleteModal.scrollTop(rowAutocomplete.outerHeight(true) + autocompleteModal.scrollTop());
            }
          }, 50);
        }
        vm.selectObject(vm.itemsFiltered[vm.indexArrow]);
      });
    }
    if (event.which === 38) {
      if (vm.indexArrow > 0) {
        vm.$scope.$apply(function () {
          vm.indexArrow -= 1;

          vm.$timeout(function () {
            if (vm.itemsFiltered.length * rowAutocomplete.outerHeight(true) - vm.indexArrow * rowAutocomplete.outerHeight(true) > autocompleteModal.height()) {
              autocompleteModal.scrollTop(autocompleteModal.scrollTop() - rowAutocomplete.outerHeight(true));
            }
          }, 50);
          vm.selectObject(vm.itemsFiltered[vm.indexArrow]);
        });
      }
    }
  });
};

export default autocompleteCtrl;

export {
  autocompleteCtrl,
  autocompleteLink
};
