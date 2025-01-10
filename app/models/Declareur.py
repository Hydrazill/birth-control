
# from app.models import db

# class Declareur(db.Model):
#     __tablename__ = 'declareurs'

#     # Clé primaire composite (lastname, firstname)
#     firstname = db.Column(db.String(100), primary_key=True, nullable=False)
#     lastname = db.Column(db.String(100), primary_key=True, nullable=False)

#     email = db.Column(db.String(100), unique=True, nullable=False)
#     phonenumber = db.Column(db.String(15), nullable=False)
#     adresse = db.Column(db.String(200), nullable=False)
#     sexe = db.Column(db.String(200), nullable=False)
#     password = db.Column(db.String(200), nullable=False)

from mongoengine import Document, StringField, EmailField

class Declareur(Document):
    meta = {
        'collection': 'declareurs',
        'indexes': [
            {'fields': ['firstname', 'lastname'], 'unique': True}  # Index composite pour garantir unicité
        ]
    }

    firstname = StringField(required=True, max_length=100)
    lastname = StringField(required=True, max_length=100)
    email = EmailField(required=True, unique=True)  # Champ email unique
    phonenumber = StringField(required=True, max_length=15)
    adresse = StringField(required=True, max_length=200)
    sexe = StringField(required=True, max_length=200)
    password = StringField(required=True, max_length=200)
