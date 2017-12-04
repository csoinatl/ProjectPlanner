from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Project(db.Model):
    """
    Model for project information based on the DB
    """

    __tablename__ = 'projects'
    projectID = db.Column(db.BigInteger(10), primary_key=True)
    projectName = db.Column(db.String(100))
    projectDesc = db.Column(db.String(1000))
    projectOwner = db.Column(db.BigInteger)
    projectTeam = db.Column(db.String(1000))
    startDate = db.Column(db.String(11))
    endDate = db.Column(db.String(11))

    def __init__(self, project_id, project_name, project_desc, project_owner, project_team, start_date, end_date):
        self.projectID = project_id
        self.projectName = project_name
        self.projectDesc = project_desc
        self.projectOwner = project_owner
        self.projectTeam = project_team
        self.startDate = start_date
        self.endDate = end_date

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class Requirements(db.Model):
    #     """
    #     Model for requirements from DB
    #     """

    __tablename__ = 'requirements'
    projectID = db.Column(db.BigInteger(10))
    reqID = db.Ccolumn(db.BigInteger(10))
    requirements = db.Column(db.String(200))
    reqType = db.Column(db.Integer(1))

    def __init__(self, project_id, req_id, func_req, req_type):
        self.projectID = project_id
        self.reqID = req_id
        self.requirements = func_req
        self.reqType = req_type

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class ProjectTeam(db.Model):
    #     """
    #     Model for project teams
    #     """

    __tablename__ = "projectteam"
    projectID = db.Column(db.BigInteger(10))
    teamMemberID = db.Column(db.BigInteger(10))
    teamMemberName = db.Column(db.String(100))
    designation = db.Column(db.String(30))

    def __init__(self, project_id, team_member_id, team_member_name, designation):
        self.projectID = project_id
        self.teamMemberID = team_member_id
        self.teamMemberName = team_member_name
        self.designation = designation

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class projectRisks(db.Model):
    __tablename__ = "projectrisks"
    projectID = db.Column(db.BigInteger(10))
    riskID = db.Column(db.BigInteger(10))
    riskDesc = db.Column(db.String(200))
    riskPriority = db.Column(db.Integer(10))
    riskStatus = db.Column(db.String(30))

    def __init__(self, project_id, risk_id, risk_desc, risk_priority, risk_status):
        self.projectID = project_id
        self.riskID = risk_id
        self.riskDesc = risk_desc
        self.riskPriority = risk_priority
        self.riskStatus = risk_status

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class projectHours(db.Model):
    __tablename__ = "projecthours"
    projectID = db.Column(db.BigInteger(10))
    reqID = db.Column(db.BigInteger(10))
    teamMemberID = db.Column(db.BigInteger(10))
    analysisHours = db.Column(db.Integer(5))
    designHours = db.Column(db.Integer(5))
    developmentHours = db.Column(db.Integer(5))
    testingHours = db.Column(db.Integer(5))
    managementHours = db.Column(db.Integer(5))

    def __init__(self, project_id, req_id, team_member_id, analysis_hours, design_hours, development_hours,
                 testing_hours, management_hours):
        self.projectID = project_id
        self.reqID = req_id
        self.teamMemberID = team_member_id
        self.analysisHours = analysis_hours
        self.designHours = design_hours
        self.developmentHours = development_hours
        self.testingHours = testing_hours
        self.managementHours = management_hours

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
