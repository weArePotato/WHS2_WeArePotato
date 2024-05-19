var ncp = require('ncp').ncp;
const transform = require('babel-transform-dir');
let q = require('q');

let babelConfig = require('./.babelrc');

ncp('./src', './lib', function (err) {
  if (err) {
    return console.error(err);
  }
  te().then(() => {
    console.log('done');
  });
});

function te () {
  let d = q.defer();
  console.log(babelConfig);
  return transform('./lib', './lib', {
    babel: babelConfig,
    // Invokes whenever a file is transformed and written.
    onFile: (file) => {
      console.log(`src/${file} -> lib/${file}`);
    }
  });
  return d.promise;
}
