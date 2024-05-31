// @flow

export type Bounds = { top:number, left:number, bottom:number, right:number }
export type Point = { x:number,y:number }
export type Size = { width:number, height:number }

export class Rect {
	_x:number;
	_y:number;
	_width:number;
	_height:number;

	_bounds:Bounds;
	_center:Point;
	_origin:Point;
    _size:Size;
    
	constructor(top:number, left:number, width:number, height:number) {
		this._x = top;
		this._y = left;
		this._width = width;
		this._height = height;
	}

	get bounds():Bounds {
		return this._bounds = this._bounds || { 
			top:this._y,
			left:this._x,
			bottom:this._y + this._height,
			right:this._x + this._width
		}
	}

	get center():Point {
		return this._center = this._center || {
			x: this._x + this._width / 2,
			y: this._y + this._height / 2
		}
	}

	get origin():Point {
		return this._origin = this._origin || {
			x: this._x,
			y: this._y
		}
	}

	get size():Size {
		return this._size = this._size || {
			width:this._width,
			height: this._height
		}
	}
}

