from flask import Flask, redirect, render_template, request, jsonify
from passwords import *
from app import *


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

    data = request.get_json()  # This parses the incoming JSON

    # Access individual fields
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    zipcode = data.get('zipcode')
    description = data.get('description')

    # Print the fields to console
    print("GOT DATA")
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Zipcode:", zipcode)
    print("Description:", description)

    # Optionally return a success response
    return jsonify({"status": "success", "message": "Data received"})


# run the app
if __name__ == '__main__':
    app.run(debug=True)