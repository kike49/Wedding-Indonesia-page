from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form_data.db'
db = SQLAlchemy(app)

class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    number_of_people = db.Column(db.Integer)
    number_of_cars = db.Column(db.Integer)
    food_allergies = db.Column(db.String(100))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    number_of_people = request.form['number_of_people']
    number_of_cars = request.form['number_of_cars']
    food_allergies = request.form['food_allergies']

    # Save the form data to the database
    form_data = FormData(name=name, number_of_people=number_of_people, number_of_cars=number_of_cars, food_allergies=food_allergies)
    db.session.add(form_data)
    db.session.commit()

    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
