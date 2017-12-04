from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Project(db.Model):
    """
    Model for project information based on the DB
    """

    __tablename__ = 'projects'
    projectID = db.Column(db.BigInteger, primary_key=True)
    projectName = db.Column(db.String(100))
    projectOwner = db.Column(db.BigInteger)
    projectTeam = db.Column(db.Integer)

    def __init__(self, project_id, project_name, project_owner, project_team):
        self.projectID = project_id
        self.projectName = project_name
        self.projectOwner = project_owner
        self.projectTeam = project_team


# class Requirements(db.Model):
#     """
#     Model for functional requirements from DB
#     """
#
#     __tablename__ = 'requirements'
#     projectID = db.Column(db.BigInteger)
#     fRequirement = db.Column(db.String(200))
#     fReqAnalysisHours = db.Column(db.Integer)
#     fReqDesignHours = db.Column(db.Integer)
#     fReqDevelopmentHours = db.Column(db.Integer)
#     fReqTestingHours = db.Column(db.Integer)
#     fReqManagementHours = db.Column(db.Integer)
#
#     def __init__(self, project_id, func_req, func_req_anal_hrs, func_rec_des_hrs,
#                  func_rec_dev_hrs, func_req_test_hrs, func_req_mngt_hrs):
#         self.projectID = project_id
#         self.fRequirement = func_req
#         self.fReqAnalysisHours = func_req_anal_hrs
#         self.fReqDesignHours = func_rec_des_hrs
#         self.fReqDevelopmentHours = func_rec_dev_hrs
#         self.fReqTestingHours = func_req_test_hrs
#         self.fReqManagementHours = func_req_mngt_hrs


# class ProjectTeam(db.Model):
#     """
#     Model for project teams
#     """
#
#     __tablename__ = "projectteam"
#     projectID = db.Column(db.BigInteger)
#     designation = db.Column(db.String(30))
#     analysishours = db.Column(db.Integer)
#     designhours = db.Column(db.Integer)
#     developmenthours = db.Column(db.Integer)
#     testinghours = db.Column(db.Integer)
#     managementhours = db.Column(db.Integer)
