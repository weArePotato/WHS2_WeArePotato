"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});
exports.WorldViewport = exports.Viewport = exports.ViewportObject = exports.Renderable = exports.XY = undefined;

var _get = function get(object, property, receiver) { if (object === null) object = Function.prototype; var desc = Object.getOwnPropertyDescriptor(object, property); if (desc === undefined) { var parent = Object.getPrototypeOf(object); if (parent === null) { return undefined; } else { return get(parent, property, receiver); } } else if ("value" in desc) { return desc.value; } else { var getter = desc.get; if (getter === undefined) { return undefined; } return getter.call(receiver); } };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _types = require("./types");
require("./apt");

var XY = _interopRequireWildcard(_types);

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

exports.XY = XY;

// this tells us the display density, if it is retina etc. This is important, otherwise
// things end up loking blurry - we need to scale when rendering to make things look
// nice and sharp. This PIXEL_RATIO will tell us the amount to scale by

var PIXEL_RATIO = function () {
	var ctx = document.createElement("canvas").getContext("2d");
	var dpr = window.devicePixelRatio || 1;
	var bsr = ctx.webkitBackingStorePixelRatio || ctx.mozBackingStorePixelRatio || ctx.msBackingStorePixelRatio || ctx.oBackingStorePixelRatio || ctx.backingStorePixelRatio || 1;

	//$FlowFixMe
	return dpr / bsr;
}();

var Renderable = exports.Renderable = function () {
	function Renderable() {
		_classCallCheck(this, Renderable);

		this.renderingFinished = false;
		this.positionType = "world";
		this.zIndex = 100;
	}

	_createClass(Renderable, [{
		key: "render",
		value: function render(viewport, sinceLastFrame) {}
	}]);

	return Renderable;
}();

var ViewportObject = exports.ViewportObject = function (_Renderable) {
	_inherits(ViewportObject, _Renderable);

	function ViewportObject(options) {
		_classCallCheck(this, ViewportObject);

		var _this = _possibleConstructorReturn(this, (ViewportObject.__proto__ || Object.getPrototypeOf(ViewportObject)).call(this));

		_this.x = options.x;
		_this.y = options.y;
		return _this;
	}

	_createClass(ViewportObject, [{
		key: "render",
		value: function render(viewport, sinceLastFrame) {
			this.update(sinceLastFrame);
		}
	}, {
		key: "update",
		value: function update(sinceLastFrame) {}
	}]);

	return ViewportObject;
}(Renderable);

var Viewport = exports.Viewport = function () {
	function Viewport(element, options) {
		var _this2 = this;

		_classCallCheck(this, Viewport);

		this.element = element;
		this.sizingElement = options.sizingElement || null;

		this.options = options || {};
		this.options.autoRedraw = false;
		this.options.onRedraw = this.options.onRedraw || function () {};

		this.tick = 0;
		this.waitingForFrame = false;
		this.lastFrameTime = null;

		this.renderQueueChanged = false;
		this.renderQueue = [];

		if (this.element instanceof HTMLCanvasElement) {
			this.canvas = this.element;
		} else {
			this.sizingElement = this.sizingElement || this.element;
			this.canvas = document.createElement('canvas');
			this.canvas.width = 300;
			this.canvas.height = 200;
			this.element.appendChild(this.canvas);
		}

		this.context = this.canvas.getContext('2d');

		this.setScale(PIXEL_RATIO);

		if (this.sizingElement) {
			window.addEventListener('resize', function () {
				return _this2.autosize();
			});
			this.autosize();
		}
	}

	// if this is set to an element, the canvas will try to fill it
	// as much as possible when the window is resized


	_createClass(Viewport, [{
		key: "setScale",
		value: function setScale(n) {
			if (n != null) {
				this._scale = n;
				this.updateDimensions();
			}
		}
	}, {
		key: "updateDimensions",
		value: function updateDimensions() {
			// the canvas height and width properties actually call a function. We assign them
			// here to variables for speed reasons, as they might get accessed many times per
			// frame
			this._width = this.canvas.width / (this._scale || 1.0);
			this._height = this.canvas.height / (this._scale || 1.0);
			this._rect = null;
		}
	}, {
		key: "autosize",
		value: function autosize() {
			var _this3 = this;

			if (this.canvas && this.sizingElement) {
				var parentSize = {
					x: this.sizingElement.clientWidth || 0,
					y: this.sizingElement.clientHeight || 0
				};

				this.setCanvasSize(parentSize.x, parentSize.y);

				this.renderQueue.forEach(function (o) {
					if (typeof o.onResize == 'function') {
						o.onResize(_this3._width, _this3._height, _this3);
					}
				});

				this.updateDimensions();
				this.refresh();
			}
		}
	}, {
		key: "setCanvasSize",
		value: function setCanvasSize(width, height) {
			if (this._scale > 1.0) {
				this.canvas.width = Math.floor(width * this._scale);
				this.canvas.height = Math.floor(height * this._scale);
				this.canvas.style.width = width + 'px';
				this.canvas.style.height = height + 'px';
			} else {
				this.canvas.width = width;
				this.canvas.height = height;
			}
		}
	}, {
		key: "start",
		value: function start() {
			return this.refresh(true);
		}

		// requests an animation frame from the canvas to redraw all objects
		//
		// This doesn't actually redraw the canvas directly, so it can safely be called multiple
		// times without doing uneeded work.
		//

	}, {
		key: "refresh",
		value: function refresh() {
			var autoRedraw = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : false;

			if (this.waitingForFrame === false && this.options.autoRedraw === false) {
				// the waiting for frame flag makes sure that the frame will only be redrawn once
				// if mulitple requests are made on the same canvas before it gets a chance to draw
				this.waitingForFrame = true;
				requestAnimationFrame(this.redraw.bind(this));

				if (autoRedraw === true) {
					this.options.autoRedraw = autoRedraw;
				}
			}

			return this;
		}
	}, {
		key: "stop",
		value: function stop() {
			this.options.autoRedraw = false;
			return this;
		}
	}, {
		key: "redraw",
		value: function redraw() {
			this.tick++;
			this.waitingForFrame = false;

			this.clear();

			// call the redraw event, so that the position of objects etc can be updated
			this.options.onRedraw(this);

			// after the redraw event there might be some objects we dont want to render
			// anymore. So we get a list of them, and remove them from the render queue
			var beforeLen = this.renderQueue.length;
			this.renderQueue = this.renderQueue.filter(function (o) {
				return !o.renderingFinished;
			});

			if (beforeLen != this.renderQueue.length) {
				this.renderQueueChanged = true;
			}

			// we want to calulate the time since the last frame so that things can be animated consistantly
			var currentTime = new Date();
			var sinceLastFrame = currentTime - (this.lastFrameTime || currentTime);
			this.lastFrameTime = currentTime;

			this.renderObjects(this.renderQueue, sinceLastFrame);

			if (this.options.autoRedraw === true) {
				requestAnimationFrame(this.redraw.bind(this));
			}

			this.renderQueueChanged = false;
		}
	}, {
		key: "renderObjects",
		value: function renderObjects(renderQueue, sinceLastFrame) {
			this.context.save();
			this.context.scale(this._scale, this._scale);

			renderQueue.forEach(function (o) {
				this.renderObject(o, sinceLastFrame);
			}.bind(this));

			this.context.restore();
		}
	}, {
		key: "renderObject",
		value: function renderObject(o, sinceLastFrame) {
			if (o) {
				o.render(this, sinceLastFrame);
			}
		}
	}, {
		key: "add",
		value: function add(o) {
			return this.startRendering(o);
		}
	}, {
		key: "startRendering",
		value: function startRendering(o) {
			if (!o) {
				return;
			}

			// the object has to have a render function for it to be added to the queue
			if (!o.render || typeof o.render != 'function') {
				return;
			}

			// re-adding the object resets the render finished flag
			if (o.renderingFinished === true) {
				o.renderingFinished = false;
			}

			// if the object has a viewport variable that is not set yet, then we will set it
			// to the current one. Don't want to overwrite this though, because it is possible
			// for an object to belong to more than one viewport
			if (!o.viewport) {
				o.viewport = this;
			}

			// if it has a resize method, then we fire that as well when it is added, so that
			// it can position itself etc
			if (typeof o.onResize == 'function') {
				o.onResize(this._width, this._height, this);
			}

			this.renderQueue.push(o);
			this.renderQueueChanged = true;

			// now we need to sort the render queue by zindex to make sure it is rendered in the same order
			this.renderQueue.sort(function (a, b) {
				return (a.zIndex || 1) - (b.zIndex || 1);
			});

			return this;
		}
	}, {
		key: "clear",
		value: function clear() {
			this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
		}
	}, {
		key: "getObjectCount",
		value: function getObjectCount() {
			return this.renderQueue.length;
		}

		// gets the center of the canvas in static co-ords

	}, {
		key: "canvasToViewport",


		// convert coordinates inside the canvas element to viewport coordinates
		value: function canvasToViewport(sx, sy) {
			return {
				x: this.origin.x + sx,
				y: this.origin.y + sy
			};
		}

		// convert coordinates inside the window containing the convas to 
		// viewport coordinates

	}, {
		key: "windowToViewport",
		value: function windowToViewport(x, y) {
			return this.canvasToViewport(x - this.canvas.offsetLeft, y - this.canvas.offsetTop);
		}
	}, {
		key: "fitText",
		value: function fitText(text, maxWidth) {
			var lines = [];
			var words = text.split(' ').reverse();

			while (words.length > 0) {
				var line = '';
				var word = words.pop();

				while (word && this.context.measureText(line + ' ' + word).width < maxWidth) {
					line += ' ' + word;
					word = words.pop();
				}

				if (word) {
					words.push(word);
				}

				lines.push(line.trim());
			}

			return lines.join("\n");
		}
	}, {
		key: "fillText",
		value: function fillText(text, x, y) {
			var _this4 = this;

			var lineHeight = this.context.measureText("M").width * 1.2;

			text.split("\n").forEach(function (line, i) {
				_this4.context.fillText(line.trim(), x, y + i * lineHeight);
			});
		}
	}, {
		key: "center",
		get: function get() {
			return this.rect.center;
		}
	}, {
		key: "rect",
		get: function get() {
			return this._rect = this._rect || new XY.Rect(0, 0, this._width, this._height);
		}
	}]);

	return Viewport;
}();

var WorldViewport = exports.WorldViewport = function (_Viewport) {
	_inherits(WorldViewport, _Viewport);

	function WorldViewport(element) {
		var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};

		_classCallCheck(this, WorldViewport);

		var _this5 = _possibleConstructorReturn(this, (WorldViewport.__proto__ || Object.getPrototypeOf(WorldViewport)).call(this, element, options));

		_this5.origin = _this5.options.origin || { x: 0, y: 0 };
		_this5.staticQueue = [];
		_this5.worldQueue = [];
		return _this5;
	}

	_createClass(WorldViewport, [{
		key: "updateQueues",
		value: function updateQueues(renderQueue) {
			this.staticQueue = renderQueue.filter(function (o) {
				return o.positionType != 'world';
			});
			this.worldQueue = renderQueue.filter(function (o) {
				return o.positionType == 'world';
			});
		}
	}, {
		key: "renderObjects",
		value: function renderObjects(renderQueue, sinceLastFrame) {
			if (this.renderQueueChanged === true) {
				this.updateQueues(renderQueue);
			}

			this.updateDimensions();

			this.context.save();
			this.context.scale(this._scale, this._scale);
			this.context.translate(-this.origin.x, -this.origin.y);

			for (var i = 0; i < this.worldQueue.length; i++) {
				this.renderObject(this.worldQueue[i], sinceLastFrame);
			}

			this.context.restore();

			// this means that static objects will always render on top of the world ones
			// it would be difficult to fix this, but since this is mostly what we want anyway
			// lets just ignore this problem
			_get(WorldViewport.prototype.__proto__ || Object.getPrototypeOf(WorldViewport.prototype), "renderObjects", this).call(this, this.staticQueue, sinceLastFrame);
		}

		// calls the render method the object in the right way. If the renderable
		// has the position type set to world, then we check if the object is visible
		// before rendering, as well as calling any other aux functions.
		//
		// Statically positioned objects are rendered the same as before

	}, {
		key: "renderObject",
		value: function renderObject(o, sinceLastFrame) {
			if (o.positionType == 'world' && o instanceof ViewportObject) {
				if (this.objectVisible(o) && o.render) {
					o.render(this, sinceLastFrame);
				}
			} else {
				_get(WorldViewport.prototype.__proto__ || Object.getPrototypeOf(WorldViewport.prototype), "renderObject", this).call(this, o, sinceLastFrame);
			}
		}

		// this sets the canvas (0,0) (in screen coords) to the x,y arguments
		// in world coordinates. Put another way, the x,y provided as arguments
		// will be the world coordinates of the top left corner of the canvas.

	}, {
		key: "setOrigin",
		value: function setOrigin(x, y) {
			if (this.isValidNumber(x) && this.isValidNumber(y)) {
				this.origin = { x: x, y: y };
			}
		}
	}, {
		key: "getOrigin",
		value: function getOrigin() {
			return this.origin;
		}

		// this is the same as setOrigin, but it uses the center of the canvas as the reference
		// instead of the top-left. x and y will be the world coordinates of the center of the 
		// canvas

	}, {
		key: "setCenter",
		value: function setCenter(x, y) {
			this._center = null;
			this._rect = null;
			this.setOrigin(x - Math.round(this._width / 2), y - Math.round(this._height / 2));
		}

		// returns the bounds of the viewport in world coordinates
		// this is mainly used to decide if a given object is visible on the
		// canvas and should be rendered

	}, {
		key: "objectVisible",


		//
		// assumes the object being passed has at least a 'getBounds' method, and if not
		// at least an x or y property so it can be evalulated as a point
		//
		// this will default to returning TRUE
		//
		// this gets called for every objet on every frame, so we should work on making it more
		// efficient...
		//
		value: function objectVisible(o) {
			if (o.x == null || o.y == null) return true;

			if (this.pointVisible(o.x, o.y)) return true;

			if (o.x - this.origin.x > this._width * 2 || o.x - this.origin.x < -this._width) return false;

			if (o.y - this.origin.y > this._height * 2 || o.y - this.origin.y < -this._height) return false;

			var bounds = void 0;

			if (!o.getBounds) {
				if (o.x !== undefined && o.y !== undefined) {
					return this.pointVisible(o.x, o.y);
				} else {
					return true;
				}
			} else {
				bounds = o.getBounds();
			}

			if (!bounds.width || !bounds.height) {
				// either object has no width and height, or they are
				// undefined. Either way just evaluate the visibility as if it was a point
				return this.pointVisible(bounds.x, bounds.y);
			} else {
				// we need to check the visibility of each corner of the bounds, if any is visible
				// then we say that the object is
				return this.pointVisible(bounds.x, bounds.y) || this.pointVisible(bounds.x + bounds.width, bounds.y) || this.pointVisible(bounds.x, bounds.y + bounds.height) || this.pointVisible(bounds.x + bounds.width, bounds.y + bounds.height);
			}
		}
	}, {
		key: "pointVisible",
		value: function pointVisible(x, y) {
			return x >= this.origin.x && x < this.origin.x + this._width && y >= this.origin.y && y < this.origin.y + this._height;
		}
	}, {
		key: "isValidNumber",
		value: function isValidNumber(n) {
			return typeof n == 'number' && !isNaN(n) && isFinite(n);
		}
	}, {
		key: "rect",
		get: function get() {
			return this._rect = this._rect || new XY.Rect(this.origin.x, this.origin.y, this._width, this._height);
		}
	}]);

	return WorldViewport;
}(Viewport);
//# sourceMappingURL=sailcloth.js.map