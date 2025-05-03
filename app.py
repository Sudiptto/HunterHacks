from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from passwords import *

# set up the app / database (IE: Filler)
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key # note make sure this secret key is hidden at all times
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # initialize flask sql database
db = SQLAlchemy(app)


# hello world route
@app.route('/')
def home():
    return render_template('index.html', api_key=api_key, moderator_pin=moderator_pin)  # pass the keys to the template


# route to grab data & add to dattabase (for now just return the latitue, longitude, and notes)
@app.route('/submitData', methods=['POST'])
def submit_data():
    # data being collected 
    '''
    latitude
    longitude
    zipcode
    description 
    '''

    # print the data (latitude, longitude , zipcode & description) to the console for now
    print("GOT DATA")

    print("Latitude: ", request.form.get('latitude'))
    print("Longitude: ", request.form.get('longitude'))
    print("Zipcode: ", request.form.get('zipcode'))
    print("Description: ", request.form.get('description'))


    pass


# run the app
if __name__ == '__main__':
    app.run(debug=True)