#pip install flask-sqlalchemy Завантажити пакет
from flask import Flask, render_template
from flask_migrate import Migrate
from models import db, pets, get_all_pets


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shelter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the app
db.init_app(app)

migrate = Migrate(app, db)




#TEST ZONE



#END_OF TEST


@app.route('/')
def main_page():

    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/catalog')
def catalog():
    items = get_all_pets()
    return render_template('catalog.html', items=items)


if __name__ == '__main__':

    app.run(debug=True)

