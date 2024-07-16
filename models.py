from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin

db = SQLAlchemy()

class Profile(db.Model):
    _tablename_ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    full_name = db.Column(db.String())
    phone_number = db.Column(db.String())
    # Add other fields as needed

    user = relationship("User", back_populates="profile")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'full_name': self.full_name,
            'phone_number': self.phone_number
            # Include other fields here
        }