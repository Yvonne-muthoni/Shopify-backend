from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db


app = Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database_name.db'

#setup migration tool
migrate = Migrate(app, db)

#link our app with the db 
db.init_app(app)

@app.route('/users')
def useres():
    return "input user-name"

@app.route('/Email')
def Email():
    return "input user-email"

@app.route('/Logout')
def logout():
    return "Logged out"