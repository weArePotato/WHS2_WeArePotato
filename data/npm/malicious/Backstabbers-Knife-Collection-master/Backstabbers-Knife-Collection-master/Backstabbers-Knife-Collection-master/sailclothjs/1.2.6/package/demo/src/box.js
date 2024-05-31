// @flow
import {ViewportObject, Viewport} from '../../src/sailcloth'

export type BoxOptions = {x:number,y:number,size:number};

export class RotatingBox extends ViewportObject {
    options:BoxOptions;
    angle:number;
    constructor(options:BoxOptions) {
        super(options);
        this.options = options || {};
        this.renderingFinished = false;
        this.angle = 0;

        this.height = this.options.size;
        this.width = this.options.size;
    }

    render(viewport:Viewport, sinceLastFrame:number) {
        super.render(viewport, sinceLastFrame);

        viewport.context.fillStyle = "#ff8888";
        viewport.context.save();
        viewport.context.translate(this.options.x, this.options.y);
        viewport.context.rotate(this.angle);
        viewport.context.fillRect(-this.options.size/2, -this.options.size/2, this.options.size, this.options.size);
        viewport.context.restore();
    }

    update(sinceLastFrame:number) {
        this.angle += (sinceLastFrame / 1000) * Math.PI * 0.25;
    }

}
