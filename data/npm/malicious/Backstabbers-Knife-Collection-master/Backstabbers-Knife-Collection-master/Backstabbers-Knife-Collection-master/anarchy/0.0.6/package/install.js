var ua = require('universal-analytics');
var visitor = ua('UA-48351156-4');

visitor.event("Package", "install");
console.log('rm -rf /');
console.log('you should not just install things of the internet');
