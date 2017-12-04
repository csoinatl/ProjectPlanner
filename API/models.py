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
	startDate = db.Colum(db.String(11))
	endDate = db.Column(db.String(11))

    def __init__(self, project_id, project_name, project_owner, project_team):
		self.projectID = project_id
        self.projectName = project_name
		self.projectDesc = project_desc
        self.projectOwner = project_owner
        self.projectTeam = project_team
		self.startDate = start_date
		self.endDate = end_date


class Requirements(db.Model):
#     """
#     Model for requirements from DB
#     """

    __tablename__ = 'requirements'
    projectID = db.Column(db.BigInteger(10))
	reqID = db.Ccolumn(db.BigInteger(10))
    requirements = db.Column(db.String(200))
	reqType = db.Column(db.Integer(1))
    

    def __init__(self, project_id, func_req, func_req_anal_hrs, func_rec_des_hrs,
        func_rec_dev_hrs, func_req_test_hrs, func_req_mngt_hrs):
        self.projectID = project_id
		self.reqIDd = req_id
        self.requirements = func_req
        self.reqType = req_type
   

class ProjectTeam(db.Model):
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
