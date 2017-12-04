import DS from 'ember-data';

export default DS.Model.extend({
  projectID: DS.attr('number'),
  projectName: DS.attr('string'),
  projectDesc: DS.attr('string'),
  projectOwnder: DS.attr('string'),
  projectTeam: DS.attr('string'),
  endDate: DS.attr('date')
});
