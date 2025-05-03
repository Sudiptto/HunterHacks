"""
This is where the database models are defined for the Flask application.
Note for sasha & samin can create databases here
"""

# simple user model for authentication purposes
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import *

# Configure the SQLAlchemy part of the app instance


# create the class
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    



