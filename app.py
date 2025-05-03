import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from passwords import secret_key

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = secret_key
# Build an absolute path to the database file in the instance folder 
# NOTE FOR SASHA & SAMIN -> BUILDING THE DATABASE IN THE INSTANCE FOLDER IS IMPORTANT FOR DEPLOYMENT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Ensure the instance folder exists
os.makedirs(app.instance_path, exist_ok=True)

db = SQLAlchemy(app)

# Import models after db is set up and instance folder exists
import models  

#  create the database
with app.app_context():
    db.create_all()
