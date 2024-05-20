radicjs
=============
**version:** 0.0.1

A modular Javascript library builder using RequireJS optimizer. 
Provides my projects with commonly used functionality while maintaining the ability to keep the library as small as possible.
It uses some of lodash functions. 
  
  
## Requirements
- jQuery


## Getting Started
Add a build to your liking using the _config.yml
```yaml
tmp: ./tmp

app: src
dest: dist


modules_external_deps:
  github/oauthio: oauthio
  spinner: spinner
  template: handlebars
  widgets: widgetfactory

default: small
builds:
  small:
    filename: radic.small
    modules: [ base, core ]
    lodash: [ omit, pick, values, keys, where, cloneDeep, isUndefined ]
  all:
    filename: radic.all
    modules: [ base, core,
              async/waterfall, async/each, cookie, crypt, github, github/oauthio, github/sync, json, # sdf
              spinner, sprintf, storage, template, template/general, template/comparisons, widgets, wordwrap,
              exports/amd, exports/global ]
    lodash: [ omit, pick, values, keys, where, cloneDeep, isUndefined ]
  githubio:
    filename: radic.githubio
    ignoredeps: [ github/oauthio ]
    modules: [ base, core,
              async/waterfall, async/each, cookie, github, github/oauthio, github/sync, json,
              spinner, storage, template, template/general, template/comparisons, widgets, wordwrap,
              exports/amd, exports/global ]
    lodash: [ omit, pick, values, keys, where, cloneDeep, isUndefined ]

```

#### Run it
```bash
# show help
grunt radicjs:help

# create build from commandline
grunt radicjs:custom --filename customized --modules base,core,async/waterfall --lodash omit,pick,values,keys,where

# preconfigured builds from _config.yml
grunt radicjs:small

grunt radicjs:small --filename mysmall

grunt radicjs:all

grunt radicjs:all --filename mysmall

grunt radicjs:githubio

# overides the _config.yml ignoredeps value. excluding it from the dist/packed/${filename}.packed.js
grunt radicjs:githubio --ignoredeps githubio/oauth,widgets
```

## License
Copyright 2014 Robin Radic 

[MIT Licensed](http://radic.mit-license.org)

