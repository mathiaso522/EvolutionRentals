# MODULE
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create a flask object
app = Flask(__name__)

# configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rentals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize the database
db = SQLAlchemy(app)

# create a model for rentals
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle = db.Column(db.String(80), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# route for index 
@app.route("/")
def index():
    return render_template('index.html')

# route for about 
@app.route("/about")
def about():
    return render_template('about.html')

# route for services
@app.route("/services")
def services():
    return render_template('services.html')

# route for contact
@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route('/rent', methods=['POST'])
def rent():
    data = request.get_json()
    vehicle = data.get('vehicle')
    
    if vehicle:
        new_rental = Rental(vehicle=vehicle)
        db.session.add(new_rental)
        db.session.commit()
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False}), 400

@app.route("/rentals")
def view_rentals():
    rentals = Rental.query.all()
    return render_template('rentals.html', rentals=rentals)

@app.route('/reset-db', methods=['POST'])
def reset_db():
    db.drop_all()
    db.create_all()
    return jsonify({'success': True})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # create tables if they don't exist
    app.run(debug=True)