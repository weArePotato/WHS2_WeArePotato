const path = require("path");
const LiveReloadPlugin = require("webpack-livereload-plugin");
const webpack = require("webpack");
const ExtractTextPlugin = require("extract-text-webpack-plugin");


const config = {
    entry: {
    	uploader : "./src/uploader.js",
    	main: "./src/main.js",
    },
    output: {
    	path: path.resolve(__dirname, 'dist'),
        filename: '[name].bundle.js'
    },
    devtool: "source-map",
    module: {
	    rules: [{
	        test: /\.scss$/,
	        use: ExtractTextPlugin.extract({
	            fallback: "style-loader",
	            use: ["css-loader", "sass-loader"],
	            publicPath: "/dist"
	        }),
	    }]
	},
    watch: true,
    plugins: [
    	new LiveReloadPlugin(),
		new webpack.ProvidePlugin({
			$: "jquery",
			jQuery: "jquery"
		}),
		new ExtractTextPlugin({
			filename: "main.css",
			disable: false,
			allChunks: true
		})
	]
};

module.exports = config;