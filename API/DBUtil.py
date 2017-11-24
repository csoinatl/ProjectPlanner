import SQLAlchemy as SQLAlchemy
from flask import Flask

dbhost = 'localhost'
dbuser = 'root'
dbpass = 'admin'
dbname = 'swe6633'

engine = SQLAlchemy.create_engine('mysql://'+dbuser+'@'+dbhost, pool_recycle=280)
DB_URI = 'mysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' + dbname

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)
