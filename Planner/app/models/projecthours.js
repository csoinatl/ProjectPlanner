import DS from 'ember-data';

export default DS.Model.extend({
  projectID: DS.attr('number'),
  reqID: DS.attr('number'),
  teamMemberID: DS.attr('number'),
  analysisHours: DS.attr('number'),
  designHours: DS.attr('number'),
  developmentHours: DS.attr('number'),
  testingHours: DS.attr('number'),
  managementHours: DS.attr('number')
});
