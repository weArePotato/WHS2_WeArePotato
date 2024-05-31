#!/usr/bin/node --harmony
var path    = require('path'),
    fs      = require('fs'),
    globule = require('globule');

var args = process.argv.splice(2);
var command = args.shift();

var config = {
    fileName: 'radic-util'
}

var log = function () {
    console.log.apply(console, arguments);
}

var log2 = console.log();
function linkTSConfig(name, to) {
    to = to || 'tsconfig.json';
    fs.existsSync(to) && fs.unlinkSync(to)
    fs.symlinkSync('.tsconfig.' + name + '.json', to)
}

var tasks = {
    build: function () {

        tasks.compile();
        //tasks.test();
        tasks.concat();
        tasks.declarations();
        tasks.clean();
    },

    declarations: function () {

        var dir = path.join(__dirname, 'lib');
        var files = fs.readdirSync(dir);

        files.filter(function (name) {
            return /^.*?\.d\.ts$/m.test(name) !== false;
        }).forEach((function (fileName) {
            fs.appendFileSync(config.fileName + '.d.ts',
                fs.readFileSync(path.join(dir, fileName), 'utf-8')
            )
        }))



        console.log(files)
    },

    test: function () {

        var Jasmine = require('jasmine');
        var jrunner = new Jasmine();
        var SpecReporter = require('jasmine-spec-reporter');
        var noop = function () {
        };

        jrunner.configureDefaultReporter({print: noop});
        jasmine.getEnv().addReporter(new SpecReporter());
        jrunner.loadConfigFile('spec/support/jasmine.json');
        jrunner.onComplete(function (passed) {
            if ( passed ) {
                console.log('All specs have passed');
            }
            else {
                console.log('At least one spec has failed');
            }
        });
        jrunner.execute();
    },

    concat: function () {

        var order = ['general', 'object', 'functions', 'JSON', 'material', 'config', 'storage'];

        var destFilePath = path.join(__dirname, config.fileName + '.js');
        if ( fs.existsSync(destFilePath) ) {
            fs.unlinkSync(destFilePath);
        }
        fs.writeFileSync(destFilePath, '');
        //order.forEach(function (name) { var filePath = path.join(__dirname, 'lib', name + '.js');
        globule.find('lib/*.js').forEach(function (filePath) {
            // var filePath = path.join(__dirname, 'lib', name + '.js');
            fs.appendFileSync(destFilePath, fs.readFileSync(filePath, 'utf-8') + '\n\n;\n')
        })
    },

    compile: function () {
        linkTSConfig('build')
        log(require('child_process').execSync('tsc').toString());
        linkTSConfig('dev')
    },

    clean: function () {
        globule.find('lib/*.{d.ts,js,js.map}').forEach(function (filePath) {
            fs.unlinkSync(filePath)
            log('deleted', filePath);
        })
    },

    linkts: function (name) {
        if ( ['dev', 'build'].indexOf(name) === - 1 ) throw new Error('Require target (dev or build)')
        linkTSConfig(name);
        ;
    }
}


if ( ! tasks[command] ) {
    throw new Error('Not a workinng command')
}
tasks[command].apply(tasks, args);


process.exit()
