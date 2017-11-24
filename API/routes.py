from flask import Flask, render_template, request, session, redirect, url_for
from models import Project, Member
from DBUtil import db

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
