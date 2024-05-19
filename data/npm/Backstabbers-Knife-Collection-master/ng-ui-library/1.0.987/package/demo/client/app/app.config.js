export default ($locationProvider, $stateProvider, $urlRouterProvider) => {
  'ngInject';
  // @see: https://github.com/angular-ui/ui-router/wiki/Frequently-Asked-Questions
  // #how-to-configure-your-server-to-work-with-html5mode
  // $locationProvider.html5Mode(true).hashPrefix('!');
  $stateProvider
    .state('demo', {
      url: '/',
      component: 'demo'
    });
  $urlRouterProvider.otherwise('/');
};
