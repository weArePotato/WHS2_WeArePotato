const crypto = require('crypto');

module.exports = function generateNonce() {
  return crypto.randomBytes(16).toString('base64').replaceAll('=','');
};