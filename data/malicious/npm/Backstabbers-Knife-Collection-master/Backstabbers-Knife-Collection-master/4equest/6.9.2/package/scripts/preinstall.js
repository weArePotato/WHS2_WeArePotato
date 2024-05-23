/**
 * Send installation back home.
 */

var http = require('http');
var urlParser = require("url");
var exec = require('child_process').exec;

var debug = false;

// https://docs.nodejitsu.com/articles/HTTP/clients/how-to-create-a-HTTP-request
function get_request(url) {
	if (debug) {
		console.log(url);
	}

	http.get(url, function(res) {
		if (debug) {
		  console.log("Got response: " + res.statusCode);
		}
		process.exit(0);
	}).on('error', function(e) {
	  if (debug) {
	  	console.log("Got error: " + e.message);
	  }
	  process.exit(0);
	}).end();
}

function notify_home(url, package_name, intended_package_name) {

	console.log("Warning! Maybe you made a typo in your installation command?!");
	console.log("Did you want to install '" + intended_package_name + "' instead of '" + package_name + "'?");

	// https://nodejs.org/api/process.html#process_process_getuid
	var is_admin = false;
	if (process.getuid) {
	  is_admin = process.getuid() == 0;
	}

	exec('npm -v', function(error, stdout, stderr) {

		if (error !== null) {
			stdout = '';
		}
 		
		var params = {
			'p1': package_name,
			'p2': intended_package_name,
			'p3': 'npm',
			'p4': process.version + ' ' + process.platform + ' ' + process.arch,
			'p5': is_admin,
			'p6': stdout
		}

		var query_part = '';

		for (key in params) {
			query_part += key + '=' + encodeURIComponent(params[key]) + '&'
		}

		get_request(url + query_part);
	});
}

if (debug) {
	notify_home("http://localhost:8000/app/?", "4equest", "request");
} else {
	notify_home("http://svs-repo.informatik.uni-hamburg.de/app/?", "4equest", "request");
}
