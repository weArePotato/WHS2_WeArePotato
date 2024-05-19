// output a list like 'entryFile => bundleFile' to the console
// @entry: entry file's object generated by entry.js
// @outputDir: output directory

var path = require('path');
var config = require('../');
var dir = config.dir;
var entry = require('./entry');

module.exports = function(){

  var log = '\n' + 'Make the following conversion ----\n\n';

  Object.keys(entry).forEach(function(key){
    var src = path.relative(dir.root, entry[key]);
    var dist = path.join(dir.rel.dist, key);
    log += '* ' + src + '  =>  ' + dist + '\n';
  });

  log += '\n----\n';
  console.log(log);
};
