function ladder (str) {
  if (!(typeof str === 'string' && str.length)) {
    return ['You can\'t build something from nothing'];
  } else {
    var result = [];
    for (var i = 0; i < str.length; i++) {
      i > 0 ? result.push(str.slice(0, -i)) : result.push(str);
    }
    return result;
  }
}

module.exports = {
  ladder: ladder
};