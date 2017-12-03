from flask import Flask, render_template, request, session, redirect, url_for
from models import Project
from DBUtil import db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exists

import json

app = Flask(__name__)


@app.route('/')
def index():
    """
    Basic index page, nothing happens here from API side
    :return:
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """
    Only if needed
    :return:
    """
    return render_template('about.html')


@app.route('/projects')
def projecs():
    """
    Returns list of projects in JSON format, need to determine what information that
    will be returned
    :return: JSON format of list of projects
    """
    return render_template('projects.html')


@app.route('/project', method=['GET', 'POST'])
def projectlist():
    """
    Returns information for a specific project, sent via REST call
    :return: Detailed information for a single project
    """
    return render_template('projectdetail.html')


if __name__ == '__main__':
    connection = db.engine.connect()
    Session = sessionmaker(bind=db.engine)
    session = Session()

    # run some stuff here:
    # Insert a project

    proj = Project
    proj.projectID = '1'
    proj.projectName = 'Test project'
    proj.projectTeam = 'Charlie So'

    session.add(proj)
    session.commit()

    if session.query(exists().where(Project.projectName == 'Test project')).scalar():
        res = session.query(Project).filter_by(projectName='Test project').first()
        print res

    connection.close()