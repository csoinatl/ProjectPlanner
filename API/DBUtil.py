from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import sqlalchemy

dbhost = 'localhost'
dbuser = 'pythonuser'
dbpass = 'Password1'
dbname = 'swe6633'

engine = sqlalchemy.create_engine('mysql://'+dbuser+'@'+dbhost, pool_recycle=280)
DB_URI = 'mysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' + dbname

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)
