'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _jquery = require('jquery');

var _jquery2 = _interopRequireDefault(_jquery);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

_jquery2.default.extend({
  highlight: function highlight(node, re, nodeName, className) {
    if (node.nodeType === 3) {
      var match = node.data.match(re);
      if (match) {
        var highlight = document.createElement(nodeName || 'span');
        highlight.className = className || 'highlight';
        var wordNode = node.splitText(match.index);
        wordNode.splitText(match[0].length);
        var wordClone = wordNode.cloneNode(true);
        highlight.appendChild(wordClone);
        wordNode.parentNode.replaceChild(highlight, wordNode);
        return 1; // skip added node in parent
      }
    } else if (node.nodeType === 1 && node.childNodes && // only element nodes that have children
    !/(script|style)/i.test(node.tagName) && // ignore script and style nodes
    !(node.tagName === nodeName.toUpperCase() && node.className === className)) {
      // skip if already highlighted
      for (var i = 0; i < node.childNodes.length; i++) {
        i += _jquery2.default.highlight(node.childNodes[i], re, nodeName, className);
      }
    }
    return 0;
  }
});

_jquery2.default.fn.unhighlight = function (options) {
  var _this = this;

  var settings = { className: 'highlight', element: 'span' };
  _jquery2.default.extend(settings, options);

  return this.find(settings.element + '.' + settings.className).each(function () {
    var parent = _this.parentNode;
    parent.replaceChild(_this.firstChild, _this);
    parent.normalize();
  }).end();
};

_jquery2.default.fn.highlight = function (words, options) {
  var _this2 = this;

  var settings = { className: 'highlight', element: 'span', caseSensitive: false, wordsOnly: false };
  _jquery2.default.extend(settings, options);

  if (words.constructor === String) {
    words = [words];
  }
  words = _jquery2.default.grep(words, function (word, i) {
    return word !== '';
  });
  words = _jquery2.default.map(words, function (word, i) {
    return word.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, '\\$&');
  });
  if (words.length === 0) {
    return this;
  }

  var flag = settings.caseSensitive ? '' : 'i';
  var pattern = '(' + words.join('|') + ')';
  if (settings.wordsOnly) {
    pattern = '\\b' + pattern + '\\b';
  }
  var re = new RegExp(pattern, flag);

  return this.each(function () {
    _jquery2.default.highlight(_this2, re, settings.element, settings.className);
  });
};

exports.default = _jquery2.default;