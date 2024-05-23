// @flow
import * as XY from './types'
export { XY }

// this tells us the display density, if it is retina etc. This is important, otherwise
// things end up loking blurry - we need to scale when rendering to make things look
// nice and sharp. This PIXEL_RATIO will tell us the amount to scale by
var PIXEL_RATIO = (function () {
	var ctx = document.createElement("canvas").getContext("2d");
	var dpr = window.devicePixelRatio || 1;
	var bsr = ctx.webkitBackingStorePixelRatio ||
		ctx.mozBackingStorePixelRatio ||
		ctx.msBackingStorePixelRatio ||
		ctx.oBackingStorePixelRatio ||
		ctx.backingStorePixelRatio || 1;

	//$FlowFixMe
	return dpr / bsr;
})();

export interface IRenderable {
    viewport:Viewport;
	renderingFinished:boolean;
	positionType: "world" | "static";
    render(viewport:Viewport, sinceLastFrame:number):void;
}

export class Renderable {
	viewport:Viewport;
	renderingFinished:boolean;
	positionType: "world" | "static";
	zIndex:number;
	constructor() {
		this.renderingFinished = false;
		this.positionType = "world";
		this.zIndex = 100;
	}

	render(viewport:Viewport, sinceLastFrame:number) {
	}
}

export class ViewportObject extends Renderable {
    x:number;
	y:number;
	width:?number;
	height:?number;
    constructor(options:{x:number,y:number}) {
		super();
		this.x = options.x;
		this.y = options.y;
    }

    render(viewport:Viewport, sinceLastFrame:number) {
        this.update(sinceLastFrame);
    }

    update(sinceLastFrame:number) {
    }
}

export class Viewport {
    element:HTMLElement;
    options:Object;
    tick:number;
    waitingForFrame:boolean;
    lastFrameTime:?Date;
    renderQueueChanged:boolean;
    renderQueue:Object[];
    canvas:HTMLCanvasElement;
	context:CanvasRenderingContext2D;
	origin:XY.Point;
    
    _width:number;
    _height:number;
	_scale:number;
	_rect:?XY.Rect;
	
	// if this is set to an element, the canvas will try to fill it
	// as much as possible when the window is resized
	sizingElement:?HTMLElement;
	constructor(element:HTMLElement, options:Object) {
		this.element = element;
		this.sizingElement = options.sizingElement || null;

		this.options = options || {};
		this.options.autoRedraw = false;
		this.options.onRedraw = this.options.onRedraw || function() {};

		this.tick = 0;
		this.waitingForFrame = false;
		this.lastFrameTime = null;

		this.renderQueueChanged = false;
		this.renderQueue = [];

		if(this.element instanceof HTMLCanvasElement) {
			this.canvas = this.element;
		} else {
			this.sizingElement = this.sizingElement|| this.element;
			this.canvas = document.createElement('canvas');
			this.canvas.width = 300;
			this.canvas.height = 200;
			this.element.appendChild(this.canvas);
		}

		this.context = this.canvas.getContext('2d');
		
		this.setScale(PIXEL_RATIO);

		if(this.sizingElement) {
			window.addEventListener('resize', () => this.autosize());
			this.autosize();
		}
		
	}
	setScale(n:number) {
		if(n != null) {
			this._scale = n;
			this.updateDimensions();
		}
	}

	updateDimensions() {
		// the canvas height and width properties actually call a function. We assign them
		// here to variables for speed reasons, as they might get accessed many times per
		// frame
		this._width = this.canvas.width / (this._scale || 1.0);
		this._height = this.canvas.height / (this._scale || 1.0);
		this._rect = null;
	}

	autosize() {
		if(this.canvas && this.sizingElement) {
			var parentSize = {
				x: this.sizingElement.clientWidth || 0,
				y: this.sizingElement.clientHeight || 0
			}

			this.setCanvasSize(parentSize.x, parentSize.y);

			this.renderQueue.forEach(o => {
				if(typeof o.onResize == 'function') {
					o.onResize(this._width, this._height, this);
				}
			});

			this.updateDimensions();
			this.refresh();
		}
	}

	setCanvasSize(width:number, height:number) {
		if(this._scale > 1.0) {
			this.canvas.width = Math.floor(width * this._scale);
			this.canvas.height = Math.floor(height * this._scale);
			this.canvas.style.width = width + 'px';
			this.canvas.style.height = height + 'px';
		} else {
			this.canvas.width = width;
			this.canvas.height = height;
		}
	}

	start() {
		return this.refresh(true);
	}

	// requests an animation frame from the canvas to redraw all objects
	//
	// This doesn't actually redraw the canvas directly, so it can safely be called multiple
	// times without doing uneeded work.
	//
	refresh(autoRedraw:boolean = false) {
		if(this.waitingForFrame === false && this.options.autoRedraw === false) {
			// the waiting for frame flag makes sure that the frame will only be redrawn once
			// if mulitple requests are made on the same canvas before it gets a chance to draw
			this.waitingForFrame = true;
			requestAnimationFrame(this.redraw.bind(this));
			
			if(autoRedraw === true) {
				this.options.autoRedraw = autoRedraw;
			}
		}

		return this;
 	}

	stop() {
		this.options.autoRedraw = false;
		return this;
	}

	redraw() {
		this.tick++;
		this.waitingForFrame = false;

		this.clear();

		// call the redraw event, so that the position of objects etc can be updated
		this.options.onRedraw(this);

		// after the redraw event there might be some objects we dont want to render
		// anymore. So we get a list of them, and remove them from the render queue
		let beforeLen = this.renderQueue.length;
		this.renderQueue = this.renderQueue.filter(o => !o.renderingFinished);
		
		if(beforeLen != this.renderQueue.length) {
			this.renderQueueChanged = true;
		}

		// we want to calulate the time since the last frame so that things can be animated consistantly
		var currentTime = new Date();
		var sinceLastFrame = currentTime - (this.lastFrameTime || currentTime);
		this.lastFrameTime = currentTime;

		this.renderObjects(this.renderQueue, sinceLastFrame);

		if(this.options.autoRedraw === true) {
			requestAnimationFrame(this.redraw.bind(this));
		}

		this.renderQueueChanged = false;
	}

	renderObjects(renderQueue:IRenderable[], sinceLastFrame:number) {
		this.context.save();
		this.context.scale(this._scale, this._scale);

		renderQueue.forEach(function(o) {
			this.renderObject(o, sinceLastFrame);
		}.bind(this));

		this.context.restore();
	}

	renderObject(o:IRenderable, sinceLastFrame:number) {
		if(o) {
			o.render(this, sinceLastFrame);
		}		
	}

	add(o:IRenderable) {
		return this.startRendering(o);
	}

	startRendering(o:IRenderable) {
    	if(!o) {
    		return;
    	}

		// the object has to have a render function for it to be added to the queue
		if(!o.render || typeof o.render != 'function') {
			return;
		}

		// re-adding the object resets the render finished flag
		if(o.renderingFinished === true) {
			o.renderingFinished = false;
		}

		// if the object has a viewport variable that is not set yet, then we will set it
		// to the current one. Don't want to overwrite this though, because it is possible
		// for an object to belong to more than one viewport
		if(!o.viewport) {
			o.viewport = this;
		}

		// if it has a resize method, then we fire that as well when it is added, so that
		// it can position itself etc
		if(typeof o.onResize == 'function') {
			o.onResize(this._width, this._height, this);
		}

		this.renderQueue.push(o);
		this.renderQueueChanged = true;

		// now we need to sort the render queue by zindex to make sure it is rendered in the same order
		this.renderQueue.sort(function(a, b) { return (a.zIndex || 1) - (b.zIndex || 1);});

		return this;
	}

	clear() {
		this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
	}

	getObjectCount() {
		return this.renderQueue.length;
	}

	// gets the center of the canvas in static co-ords
	get center():XY.Point {
		return this.rect.center;
	}

	get rect():XY.Rect {
		return this._rect = this._rect || new XY.Rect(0, 0, this._width, this._height);
	}
	
	// convert coordinates inside the canvas element to viewport coordinates
	canvasToViewport(sx:number, sy:number) {
		return {
			x: this.origin.x + sx,
			y: this.origin.y + sy
		};
	}

	// convert coordinates inside the window containing the convas to 
	// viewport coordinates
	windowToViewport(x:number, y:number) {
		return this.canvasToViewport(
			x - this.canvas.offsetLeft,
			y - this.canvas.offsetTop
		);
	}

	fitText(text:string, maxWidth:number) {
		const lines = [];
		const words = text.split(' ').reverse();

		while(words.length > 0) {
			let line = '';
			let word = words.pop();

			while(word && this.context.measureText(line + ' ' + word).width < maxWidth) {
				line += (' ' + word);
				word = words.pop();
			}

			if(word) {
				words.push(word);
			}

			lines.push(line.trim());
		}

		return lines.join("\n");
	}

	fillText(text:string, x:number, y:number) {
		const lineHeight = this.context.measureText("M").width * 1.2;

		text.split("\n").forEach((line, i) => {
			this.context.fillText(line.trim(), x, y + i*lineHeight);
		});
	}


}

export class WorldViewport extends Viewport {
	staticQueue:IRenderable[];
	worldQueue:IRenderable[];
	_center:?XY.Point;

	constructor(element:HTMLElement, options:Object = {}) {
		super(element, options);
		this.origin = this.options.origin || {x:0, y:0};
		this.staticQueue = [];
		this.worldQueue = [];
	}

	updateQueues(renderQueue:IRenderable[]) {
		this.staticQueue = renderQueue.filter(o => o.positionType != 'world');
		this.worldQueue  = renderQueue.filter(o => o.positionType == 'world');
	}

	renderObjects(renderQueue:IRenderable[], sinceLastFrame:number) {
		if(this.renderQueueChanged === true) {
			this.updateQueues(renderQueue);
		}

		this.updateDimensions();

		this.context.save();
		this.context.scale(this._scale, this._scale);
		this.context.translate(-this.origin.x, -this.origin.y);
		
		for(var i=0; i < this.worldQueue.length; i++) {
			this.renderObject(this.worldQueue[i], sinceLastFrame);
		}

		this.context.restore();

		// this means that static objects will always render on top of the world ones
		// it would be difficult to fix this, but since this is mostly what we want anyway
		// lets just ignore this problem
		super.renderObjects(this.staticQueue, sinceLastFrame);

	}

	// calls the render method the object in the right way. If the renderable
	// has the position type set to world, then we check if the object is visible
	// before rendering, as well as calling any other aux functions.
	//
	// Statically positioned objects are rendered the same as before
	renderObject(o:IRenderable, sinceLastFrame:number) {
		if(o.positionType == 'world' && o instanceof ViewportObject) {
			if(this.objectVisible(o) && o.render) {
				o.render(this, sinceLastFrame);
			}
		} else {
			super.renderObject(o, sinceLastFrame);
		}
	}

	// this sets the canvas (0,0) (in screen coords) to the x,y arguments
	// in world coordinates. Put another way, the x,y provided as arguments
	// will be the world coordinates of the top left corner of the canvas.
	setOrigin(x:number, y:number) {
		if(this.isValidNumber(x) && this.isValidNumber(y)) {
			this.origin = {x: x, y: y};
		}
	}

	getOrigin():XY.Point {
		return this.origin;
	}

	// this is the same as setOrigin, but it uses the center of the canvas as the reference
	// instead of the top-left. x and y will be the world coordinates of the center of the 
	// canvas
	setCenter(x:number, y:number) {
		this._center = null;
		this._rect = null;
		this.setOrigin(x - Math.round(this._width / 2), y - Math.round(this._height / 2));
	}

	// returns the bounds of the viewport in world coordinates
	// this is mainly used to decide if a given object is visible on the
	// canvas and should be rendered
	get rect():Object {
		return this._rect = this._rect || new XY.Rect(this.origin.x, this.origin.y, this._width, this._height);
	}

	//
	// assumes the object being passed has at least a 'getBounds' method, and if not
	// at least an x or y property so it can be evalulated as a point
	//
	// this will default to returning TRUE
	//
	// this gets called for every objet on every frame, so we should work on making it more
	// efficient...
	//
	objectVisible(o:ViewportObject) {
		if(o.x == null || o.y == null)
			return true;

		if(this.pointVisible(o.x, o.y))
			return true;

		if((o.x - this.origin.x > this._width * 2) || (o.x - this.origin.x < -this._width))
			return false;

		if((o.y - this.origin.y > this._height * 2) || (o.y - this.origin.y < -this._height))
			return false;

		let bounds:?XY.Bounds;

		if(!o.getBounds) {
			if(o.x !== undefined  && o.y !== undefined) {
				return this.pointVisible(o.x, o.y);
			} else {
				return true;
			}
		} else {
			bounds = (o:any).getBounds();
		}

		if(!bounds.width || !bounds.height) {
			// either object has no width and height, or they are
			// undefined. Either way just evaluate the visibility as if it was a point
			return this.pointVisible(bounds.x, bounds.y);
		} else {
			// we need to check the visibility of each corner of the bounds, if any is visible
			// then we say that the object is
			return this.pointVisible(bounds.x, bounds.y) ||
				this.pointVisible(bounds.x + bounds.width, bounds.y) ||
				this.pointVisible(bounds.x, bounds.y + bounds.height) ||
				this.pointVisible(bounds.x + bounds.width, bounds.y + bounds.height);
		}
	}

	pointVisible(x:number, y:number) {
		return (x >= this.origin.x && x < this.origin.x + this._width) && (y >= this.origin.y && y < this.origin.y + this._height);
	}

	isValidNumber(n:number):boolean {
		return typeof n == 'number' && !isNaN(n) && isFinite(n)
	}
}

