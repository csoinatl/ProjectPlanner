export default function() {

  this.namespace = '/api';

  this.get('/projects', function () {
    return {
      data: [{
        projectID: 1,
        projectName: 'Test Project 1',
        projectDesc: 'This is a test project',
        projectOwnder: 'Charlie So',
        projectTeam: 'Awesome',
        endDate: '12/31/2018'
      }, {
        projectID: 2,
        projectName: 'Test Project 2',
        projectDesc: 'This is a test project',
        projectOwnder: 'Charlie So',
        projectTeam: 'Awesome',
        endDate: '12/31/2018'
      }
      ]
    }
  });

  this.get('/project/:projectID', function () {
    return {
      data: [{
        projectID: 2,
        projectName: 'Test Project 2',
        projectDesc: 'This is a test project',
        projectOwnder: 'Charlie So',
        projectTeam: 'Awesome',
        endDate: '12/31/2018'
      }]
    }
  });

  this.get('/projecthours/:projectID', function () {
    return {
      data: [{
        projectID: 2,
        reqID: 1,
        teamMemberID: 1,
        analysisHours: 12,
        designHours: 13,
        developmentHours: 14,
        testingHours: 11,
        managementHours: 10
      }]
    }
  });

  this.get('/projectrisk/:projectID', function () {
      return {
        data: [{
          projectID: 2,
          riskID: 1,
          riskDesc: 'This is a serious risk',
          riskPriority: 7,
          riskStatus: 'A'
        }]
      }
    }
  );

  this.get('/requirements', function () {
    return {
      data: [{
        projectID: 2,
        reqID: 2,
        requirements: 'Project Planning Tool is here!',
        reqType: 'R'
      }]
    }
  });
}
