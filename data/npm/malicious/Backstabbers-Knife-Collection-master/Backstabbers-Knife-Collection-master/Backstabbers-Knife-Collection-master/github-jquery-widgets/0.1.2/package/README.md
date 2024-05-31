# github-jquery-widgets
[![Travis build status](https://img.shields.io/travis/RobinRadic/github-jquery-widgets.svg)](http://travis-ci.org/RobinRadic/github-jquery-widgets)
[![NPM Version](https://img.shields.io/npm/v/github-jquery-widgets.svg)](http://npmjs.org/package/github-jquery-widgets)
[![Goto documentation](http://img.shields.io/badge/goto-documentation-orange.svg)](http://robin.radic.nl/github-jquery-widgets)
[![Goto repository](http://img.shields.io/badge/goto-repository-orange.svg)](https://github.com/robinradic/github-jquery-widgets)
[![License](http://img.shields.io/badge/license-MIT-blue.svg)](http://radic.mit-license.org)


## Getting Started
  
Check out the [demonstration](http://robin.radic.nl/github-jquery-widgets/demo) or [documentation](http://robin.radic.nl/github-jquery-widgets) for more information.
  
### Installing
```bash
# Using bower
bower install --save github-jquery-widgets

# Using node
npm install --save github-jquery-widgets
```

### Usage
  
#### Dependencies and widget files
The package ships with seperate files allowing various ways to handle dependencies and to include/exclude widgets.  **tip:** use grunt-usemin or something likewise to concat and minify your js/css.
```html
<link href="path/to/dist/github-widgets.css" type="text/css" rel="stylesheet">
<link href="path/to/dist/github-profile.css" type="text/css" rel="stylesheet">
<link href="path/to/dist/github-events.css" type="text/css" rel="stylesheet">
<script src="jquery.min.js"></script>
<script src="path/to/dist/dep/packed/radic.githubwidgets.packed.min.js"></script> <!-- includes: spin.js, widget.js, handlebars.runtime.min.js -->
<script src="path/to/dist/github-widget.js"></script>
<script src="path/to/dist/github-profile.js"></script>
<script src="path/to/dist/github-events.js"></script>
```
  
As an alternative, instead of using the packed radic.githubwidgets.js, you can use the non-packed version. You will have to include `spin.js`, `widget.js` and `handlebars.runtime.js` yourself. An example:
```html
<link href="path/to/dist/github-widgets.css" type="text/css" rel="stylesheet">
<link href="path/to/dist/github-profile.css" type="text/css" rel="stylesheet">
<link href="path/to/dist/github-events.css" type="text/css" rel="stylesheet">
<script src="jquery.min.js"></script>
<script src="jquery-ui.min.js"></script> <!-- provides widget.js (jQuery UI Widget Factory) -->
<script src="path/to/dist/dep/spin.js"></script>
<script src="path/to/dist/dep/handlebars.runtime.min.js"></script>
<script src="path/to/dist/dep/radic.githubwidgets.min.js"></script>
<script src="path/to/dist/github-widget.js"></script>
<script src="path/to/dist/github-profile.js"></script>
<script src="path/to/dist/github-events.js"></script>
```

### Initializing a widget
```javascript
$(function(){
    $('selector').githubProfile({
        username: 'robinradic'
    });
});
```
More information can be found in the [API documentation](http://robin.radic.nl/github-jquery-widgets/)

## Customizing your build
By downloading the source, you can create a customized build. You can alter the HTML templates and SCSS.
  
### Getting started
```bash
git clone https://github.com/robinradic/github-jquery-widgets # or fork->clone a version.
cd github-jquery-widgets
./scripts/bootstrap.sh # This will update-init the radicjs submodule and copy the pre-commit hook that updates the submodule before commiting
npm install
bower install
```
  
**More information soon**


## License
Copyright 2014 Robin Radic 

[MIT Licensed](http://radic.mit-license.org)

