const path = require('path');

module.exports = {
    entry: './moment-origin.js',
    output: {
        path: path.resolve(__dirname, './'),
        filename: 'moment.js',
        libraryTarget: 'umd',
        globalObject: 'this',
        library: 'momnet',
    },
};
