// @flow

import { Renderable, WorldViewport, Viewport } from '../lib/sailcloth.js'
import * as Box from './box'

// just ignore jquery errors
declare function $(any):any;

export class App {
    viewport:WorldViewport;
    constructor() {
        let element = document.getElementById('canvas')
        let move:{x:number,y:number} = {x:0,y:0}

        
        this.viewport = new WorldViewport(element, {
            onRedraw: () => { 
                let p = this.viewport.center;
                this.viewport.setCenter(p.x + move.x, p.y + move.y);
             },
            sizingElement: document.getElementById('container')
        });

        this.viewport.setCenter(0, 0);
        this.viewport.start();

        // add a bunch of rotating boxes, plus a line at 0,0
        this.viewport.add(new Box.RotatingBox({ x: 0, y: 0, size: 64 }));
        this.viewport.add(new Box.RotatingBox({ x: 0, y: 120, size: 48 }));
        this.viewport.add(new Box.RotatingBox({ x: 0, y: -120, size: 48 }));
        this.viewport.add(new Box.RotatingBox({ x: 150, y: 0, size: 48 }));
        this.viewport.add(new Box.RotatingBox({ x: -150, y: 0, size: 48 }));
        this.viewport.add(new GridLines());

        // stop after 10 seconds so we don't load the browser
        // too much
        setTimeout(() => this.viewport.stop(), 10000);

        $(window).keydown((e) => {
            if(e.key == 'w') {
                move.y = -1;
            } else if(e.key == 's') {
                 move.y = 1;
            } else if(e.key == 'a') {
                move.x = -1;
            } else if(e.key == 'd') {
                move.x = 1;
            }
        });

        $(window).keyup((e) => {
            if(e.key == 'w' || e.key == 's') {
                move.y = 0;
            } else if(e.key == 'a' || e.key == 'd') {
                move.x = 0;
            }
        });
    }
}

class GridLines extends Renderable {
    zIndex:number;
    constructor() {
        super();
        this.zIndex = 10;
    }

    render(viewport:Viewport, sinceLastFrame:number) {
        if(viewport instanceof WorldViewport) {
            let bounds = viewport.rect.bounds;
            viewport.context.strokeStyle = "#ddd"
            viewport.context.lineWidth - 1.0;

            viewport.context.beginPath();
            viewport.context.moveTo(bounds.left, 0.5);
            viewport.context.lineTo(bounds.right, 0.5);
            viewport.context.stroke();

            viewport.context.beginPath();
            viewport.context.moveTo(0.5, bounds.top);
            viewport.context.lineTo(0.5, bounds.bottom);
            viewport.context.stroke();
        }
    }
}

