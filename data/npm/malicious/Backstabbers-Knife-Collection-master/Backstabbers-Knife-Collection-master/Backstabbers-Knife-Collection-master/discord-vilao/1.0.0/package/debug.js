var debug;

module.exports = function () {
  if (!debug) {
    try {
      debug = require("debug")("discord-vilao");
    }
    catch (error) {
      debug = function () {};
    }
  }
  debug.apply(null, arguments);
};
