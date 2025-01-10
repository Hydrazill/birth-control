
# from app.models import db

# class ActeNaiss(db.Model):
#     __tablename__ = 'acteNaiss'

#     # Clé primaire composite
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
#     # infos enfant
#     firstname = db.Column(db.String(100), nullable=False)
#     lastname = db.Column(db.String(100), nullable=False)
#     birthdate = db.Column(db.String(100), nullable=False)
#     birthplace = db.Column(db.String(15), nullable=False)
#     sexe = db.Column(db.String(200), nullable=False)
    
#     # infos pere
#     namefather = db.Column(db.String(200), nullable=False)
#     birthdatefather = db.Column(db.String(100), nullable=False)
#     birthplacefather = db.Column(db.String(15), nullable=False)
#     addressfather = db.Column(db.String(200), nullable=False)
#     professionfather = db.Column(db.String(200), nullable=False)
    
#     # infos mere
#     namemother = db.Column(db.String(200), nullable=False)
#     birthdatemother = db.Column(db.String(100), nullable=False)
#     birthplacemother = db.Column(db.String(15), nullable=False)
#     addressmother = db.Column(db.String(200), nullable=False)
#     professionmother = db.Column(db.String(200), nullable=False)
    
#     # info declareur
#     firstnamedeclareur = db.Column(db.String(100), db.ForeignKey('declareurs.firstname'), nullable=False)
#     lastnamedeclareur = db.Column(db.String(100), db.ForeignKey('declareurs.lastname'), nullable=False)

from mongoengine import Document, StringField

class ActeNaiss(Document):
    meta = {'collection': 'naissances'}  # Nom de la collection MongoDB

    # Informations sur l'enfant
    firstname = StringField(required=True, max_length=100)
    lastname = StringField(required=True, max_length=100)
    birthdate = StringField(required=True)  # Format de date à valider
    birthplace = StringField(required=True, max_length=15)
    sexe = StringField(required=True, max_length=200)

    # Informations sur le père
    namefather = StringField(required=True, max_length=200)
    birthdatefather = StringField(required=True)
    birthplacefather = StringField(required=True, max_length=15)
    addressfather = StringField(required=True, max_length=200)
    professionfather = StringField(required=True, max_length=200)

    # Informations sur la mère
    namemother = StringField(required=True, max_length=200)
    birthdatemother = StringField(required=True)
    birthplacemother = StringField(required=True, max_length=15)
    addressmother = StringField(required=True, max_length=200)
    professionmother = StringField(required=True, max_length=200)

    # Informations sur le déclarant
    firstnamedeclareur = StringField(required=True, max_length=100)
    lastnamedeclareur = StringField(required=True, max_length=100)
