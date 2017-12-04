import DS from 'ember-data';

export default DS.Model.extend({
  projectID: DS.attr('number'),
  riskID: DS.attr('number'),
  riskDesc: DS.attr('string'),
  riskPriority: DS.attr('number'),
  riskStatus: DS.attr('string')
});
