from flask import Flask, redirect, render_template, request, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from passwords import *
from app import *
from models import User

# Initialize Flask-Login
login_manager = LoginManager() 
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to login page if not logged in


with app.app_context():
    db.drop_all()  # Drop all tables
    db.create_all()  # Create all tables
    # print(db.query.all())  # Print all records in the database
    new_user = User(username='hewwo', password='ssss')
    db.session.add(new_user)
    db.session.commit() 
    #logout_user()  # Log out the user after creating the database

# hello world route
@app.route('/')
@login_required
def home():
    return render_template('index.html', api_key=api_key, moderator_pin=moderator_pin)  # pass the keys to the template


# route to grab data & add to dattabase (for now just return the latitue, longitude, and notes)
@app.route('/submitData', methods=['POST'])
@login_required
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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Assuming you have a User model defined

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password: 
        return jsonify({"status": "error", "message": "Username and password required"})

    user = User.query.filter_by(username=username).first() 

    if user and user.password == password:
        login_user(user)
        return redirect('/')

    else: 
        return jsonify({"status": "error", "message": "Matching credentials not found"}), 401
    

@app.route('/signup', methods=['POST', 'GET'])
def signup(): 
    if request.method == 'POST': 
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirm = request.form.get('password-confirm')

        user = User.query.filter_by(username=username).first()
        if user: 
            return jsonify({"status": "error", "message": "Username already in use"})
        elif len(password) < 6: 
            return jsonify({"status": "error", "message": "Password must be at least 6 characters"})
        elif password != password_confirm:
            return jsonify({"status": "error", "message": "Passwords do not match"})
        else: 
            # flash("You're logged in!", category='success')
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect('/')

    return render_template('signup.html')

@app.route('/logout')
@login_required 
def logout():
    logout_user()
    return redirect('/login')

    
# @app.route('/addLocation', methods=['POST'])
# def add_location():
    

# run the app
if __name__ == '__main__':
    #app.run(host="127.0.0.1", port=5500, debug=True)
    app.run(debug=True)