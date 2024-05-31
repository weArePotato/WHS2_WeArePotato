class ModalBoxController {
  constructor ($transclude) {
    this.$transclude = $transclude;
  }

  $onInit () {
    let width = this.width;
    if (!width) {
      width = '';
    } else if (!isNaN(width)) {
      width += 'px';
    }
    this.modalBoxWidth = width;

    let height = this.height;
    if (!height) {
      height = '';
    } else if (!isNaN(height)) {
      height += 'px';
    }
    this.modalBoxHeight = height;
  }
}

export default ModalBoxController;
