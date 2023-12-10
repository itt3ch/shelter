#pip install flask-sqlalchemy Завантажити пакет
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class pets(db.Model):
    __tablename__ = 'pets'

    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    breed = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    city_of_origin = db.Column(db.String(50), nullable=True)
    img = db.Column(db.String(255), nullable=True)

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"<Pet {self.id}: {self.name}, {self.age}, {self.breed}, {self.city}, {self.city_of_origin}>"


# LOGICS
def get_all_pets():
    return pets.query.order_by(pets.id).all()

#get_pet_by_id TODO


