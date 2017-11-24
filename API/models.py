from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import json

db = SQLAlchemy()


class Project(db.model):
    """
    Model for project information based on the DB
    """

    __tablename__ = 'projects'
    projectID = db.column(db.BigInteger, primary_key = True)
    projectName = db.column(db.String(100))
    projectOwner = db.column(db.BigInteger)
    projectTeam = db.column(db.Integer)

    def __init__(self, project_id, project_name, project_owner, project_team):
        self.projectID = project_id
        self.projectName = project_name
        self.projectOwner = project_owner
        self.projectTeam = project_team


class FunctionalRequirements(db.model):
    """
    Model for functional requirements from DB
    """

    __tablename__ = 'functionalrequirements'
    projectID = db.column(db.BigInteger)
    fRequirement = db.column(db.String(200))
    fReqAnalysisHours = db.column(db.Integer)
    fReqDesignHours = db.column(db.Integer)
    fReqDevelopmentHours = db.column(db.Integer)
    fReqTestingHours = db.column(db.Integer)
    fReqManagementHours = db.column(db.Integer)

    def __init__(self, project_id, func_req, func_req_anal_hrs, func_rec_des_hrs,
                 func_rec_dev_hrs, func_req_test_hrs, func_req_mngt_hrs):
        self.projectID = project_id
        self.fRequirement = func_req
        self.fReqAnalysisHours = func_req_anal_hrs
        self.fReqDesignHours = func_rec_des_hrs
        self.fReqDevelopmentHours = func_rec_dev_hrs
        self.fReqTestingHours = func_req_test_hrs
        self.fReqManagementHours = func_req_mngt_hrs


class nonFunctionalRequirements(db.model):
    """
    Model for functional requirements from DB
    """

    __tablename__ = 'nonfunctionalrequirements'
    projectID = db.column(db.BigInteger)
    nonFunctionalRequirements = db.column(db.String(200))
    nfReqAnalysisHours = db.column(db.Integer)
    nfReqDesignHours = db.column(db.Integer)
    nfReqDevelopmentHours = db.column(db.Integer)
    nfReqTestingHours = db.column(db.Integer)
    nfReqManagementHours = db.column(db.Integer)


class ProjectTeam(db.model):
    """
    Model for project teams
    """

    __tablename__ = "projectteam"
    projectID = db.column(db.BigInteger)
    designation = db.column(db.String(30))
    analysishours = db.column(db.Integer)
    designhours = db.column(db.Integer)
    developmenthours = db.column(db.Integer)
    testinghours = db.column(db.Integer)
    managementhours = db.column(db.Integer)


class ProjectTool(db.model):
    """
    Model for project tools
    """

    __tablename__ = 'projecttool'
    projectID = db.column(db.BigInteger)
    analysistools = db.column(db.String(50))
    designtools = db.column(db.String(50))
    devemopmenttools = db.column(db.String(50))
    testingtools = db.column(db.String(50))
    managemnettools = db.column(db.String(50))


class Person(db.model):
    """
    Model for person class
    """

    __tablename__ = "person"
    personID = db.column(db.BigInteger, primary_key=True)
    first_name = db.column(db.String(40))
    last_name = db.column(db.String(40))
    title = db.column(db.String(40))
    