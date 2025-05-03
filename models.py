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


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(65), unique=True, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable= False)

    def __repr__(self):
        return f'<Location {self.name}>'
    
    


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    review_text = db.Column(db.Text, nullable=False)

    #lets us access user and location objects from review object
    # we call review.user to get the user object, and then we can access username, pass, etc. 
    user = db.relationship('User', backref='reviews')
    location = db.relationship('Location', backref='reviews')

    def __repr__(self): 
        return f'<Review '
