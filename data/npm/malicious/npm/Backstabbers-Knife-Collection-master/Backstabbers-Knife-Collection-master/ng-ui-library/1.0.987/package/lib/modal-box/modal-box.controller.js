'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var ModalBoxController = function () {
  function ModalBoxController($transclude) {
    _classCallCheck(this, ModalBoxController);

    this.$transclude = $transclude;
  }

  _createClass(ModalBoxController, [{
    key: '$onInit',
    value: function $onInit() {
      var width = this.width;
      if (!width) {
        width = '';
      } else if (!isNaN(width)) {
        width += 'px';
      }
      this.modalBoxWidth = width;

      var height = this.height;
      if (!height) {
        height = '';
      } else if (!isNaN(height)) {
        height += 'px';
      }
      this.modalBoxHeight = height;
    }
  }]);

  return ModalBoxController;
}();

exports.default = ModalBoxController;