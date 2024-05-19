import angular from 'angular';
import uiRouter from 'angular-ui-router';
import angularAnimate from 'angular-animate';
import appConfig from './app.config';
import Components from './components/components';
import AppComponent from './app.component';

angular.module('app', [
  uiRouter,
  angularAnimate,
  Components
])
  .config(appConfig)
  .component('app', AppComponent);
