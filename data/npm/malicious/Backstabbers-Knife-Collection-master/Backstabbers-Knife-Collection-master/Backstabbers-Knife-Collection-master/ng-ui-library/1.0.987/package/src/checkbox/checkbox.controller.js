class CheckboxController {
  constructor () {
    this.$onInit = function () {
      this.bindId = this.bindId || this.model;
    };
  }
}

export default CheckboxController;
