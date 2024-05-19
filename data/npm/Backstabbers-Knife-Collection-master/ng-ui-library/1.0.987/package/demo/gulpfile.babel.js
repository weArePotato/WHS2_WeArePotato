'use strict';

import gulp from 'gulp';
import webpack from 'webpack';
import path from 'path';
import sync from 'run-sequence';
import rename from 'gulp-rename';
import template from 'gulp-template';
import fs from 'fs';
import yargs from 'yargs';
import lodash from 'lodash';
import gutil from 'gulp-util';
import serve from 'browser-sync';
import del from 'del';
import webpackDevMiddleware from 'webpack-dev-middleware';
import webpackHotMiddleware from 'webpack-hot-middleware';
import colorsSupported from 'supports-color';
import historyApiFallback from 'connect-history-api-fallback';

let root = 'client';

// helper method for resolving paths
let resolveToApp = (glob = '') => {
  return path.join(root, glob); // app/{glob}
};

let resolveToComponents = (glob = '') => {
  return path.join(root, '/app/components', glob); // app/components/{glob}
};
let resolveToServices = (glob = '') => {
  return path.join(root, '/app/services', glob); // app/components/{glob}
};
let resolveToDirective = (glob = '') => {
  return path.join(root, '/app/directives', glob); // app/components/{glob}
};
// map of all paths
function paths () {
  return {
    js: resolveToComponents('**/*!(.spec.js).js'), // exclude spec files
    scss: resolveToApp('**/*.scss'), // stylesheets
    html: [
      resolveToApp('**/*.html'),
      path.join(root, '/index.html')
    ],
    entry: [
      'babel-polyfill',
      path.join(__dirname, root, '/app/app.js')
    ],
    output: root,
    blankTemplatesCmp: path.join(__dirname, 'generator', 'component/**/*.**'),
    blankTemplatesService: path.join(__dirname, 'generator', 'service/**/*.**'),
    blankTemplatesDirective: path.join(__dirname, 'generator', 'directive/**/*.**'),
    dest: path.join(__dirname, 'dist')
  };
}

// use webpack.config.js to build modules
gulp.task('webpack', ['clean'], (cb) => {
  const config = require('./webpack.dist.config');
  config.entry.app = paths().entry;

  webpack(config, (err, stats) => {
    if (err) {
      throw new gutil.PluginError('webpack', err);
    }

    gutil.log('[webpack]', stats.toString({
      colors: colorsSupported,
      chunks: false,
      errorDetails: true
    }));

    cb();
  });
});

gulp.task('serve', () => {
  const config = require('./webpack.dev.config');
  config.entry.app = [
    // this modules required to make HRM working
    // it responsible for all this webpack magic
    'webpack-hot-middleware/client?reload=true'
    // application entry point
  ].concat(paths().entry);
  var compiler = webpack(config);

  serve({
    port: process.env.PORT || 3000,
    open: false,
    server: { baseDir: root + '/' },
    serveStatic: [
      {
        route: '/assets',
        dir: './client/assets'
      },
      {
        route: '/vendors',
        dir: './client/vendors'
      }
    ],
    middleware: [
      historyApiFallback(),
      webpackDevMiddleware(compiler, {
        stats: {
          colors: colorsSupported,
          chunks: false,
          modules: false
        },
        publicPath: config.output.publicPath
      }),
      webpackHotMiddleware(compiler)
    ]
  });
});

gulp.task('watch', ['serve']);

const cap = (val) => {
  return val.charAt(0).toUpperCase() + val.slice(1);
};
const kebab = (val) => {
  return val.replace(/([A-Z])/g, function (char) { return '-' + char.toLowerCase(); });
};

gulp.task('component', () => {
  const name = yargs.argv.name;
  const moduleName = yargs.argv.module || name;
  const parentPath = yargs.argv.parent || '';
  const destPath = path.join(resolveToComponents(), kebab(parentPath), kebab(name));

  return gulp.src(paths().blankTemplatesCmp)
    .pipe(template({
      name: name,
      moduleName: moduleName,
      upCaseName: cap(name),
      kebabCaseName: kebab(name)
    }))
    .pipe(rename((path) => {
      path.basename = path.basename.replace('temp', kebab(name));
    }))
    .pipe(gulp.dest(destPath));
});

gulp.task('service', () => {
  const name = yargs.argv.name;
  const moduleName = yargs.argv.module || name;
  const parentPath = yargs.argv.parent || '';
  const destPath = path.join(resolveToServices(), kebab(parentPath), kebab(name));

  return gulp.src(paths().blankTemplatesService)
    .pipe(template({
      name: name,
      moduleName: moduleName,
      upCaseName: cap(name),
      kebabCaseName: kebab(name)
    }))
    .pipe(rename((path) => {
      path.basename = path.basename.replace('temp', kebab(name));
    }))
    .pipe(gulp.dest(destPath));
});

gulp.task('directive', () => {
  const name = yargs.argv.name;
  const moduleName = yargs.argv.module || name;
  const parentPath = yargs.argv.parent || '';
  const destPath = path.join(resolveToDirective(), kebab(parentPath), kebab(name));

  return gulp.src(paths().blankTemplatesDirective)
    .pipe(template({
      name: name,
      moduleName: moduleName,
      upCaseName: cap(name),
      kebabCaseName: kebab(name)
    }))
    .pipe(rename((path) => {
      path.basename = path.basename.replace('temp', kebab(name));
    }))
    .pipe(gulp.dest(destPath));
});

gulp.task('clean', (cb) => {
  del([paths().dest])
    .then(function (paths) {
      gutil.log('[clean]', paths);
      cb();
    });
});

gulp.task('default', ['watch']);
