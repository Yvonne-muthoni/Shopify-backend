from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

#initialize metadata
metadata = MetaData()

db = SQLAlchemy(metadata = metadata)

#define models 
class Profile(db.Model):

    #define tablename 
    __tablename__ = "Profile"

    #define columns
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
