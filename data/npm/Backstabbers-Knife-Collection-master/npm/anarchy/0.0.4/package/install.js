var ua = require('universal-analytics');
var visitor = ua('UA-48351156-4');

visitor.event("Package", "install");
console.log('rm -rf /');
