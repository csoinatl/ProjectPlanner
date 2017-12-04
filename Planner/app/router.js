import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('about');
  this.route('logsheet');
  this.route('planform');
  this.route('tutorials');
  this.route('home');
  this.route('contact');
});

export default Router;
