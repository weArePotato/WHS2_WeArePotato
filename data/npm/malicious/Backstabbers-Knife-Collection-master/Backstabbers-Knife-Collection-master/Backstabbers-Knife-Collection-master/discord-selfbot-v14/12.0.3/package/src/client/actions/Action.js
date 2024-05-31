



class GenericAction {
  constructor(client) {
    this.client = client;
  }

  handle(data) {
    return data;
  }
}

module.exports = GenericAction;
