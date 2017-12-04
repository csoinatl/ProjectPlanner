import DS from 'ember-data';

export default DS.Model.extend({
  projectID: DS.attr('number'),
  teamMemberID: DS.attr('number'),
  teamMemberName: DS.attr('string'),
  designation: DS.attr('string')
});
