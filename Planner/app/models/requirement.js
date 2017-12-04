import DS from 'ember-data';

export default DS.Model.extend({
  projectID: DS.attr('number'),
  reqID: DS.attr('number'),
  requirements: DS.attr('string'),
  reqType: DS.attr('number')
});
