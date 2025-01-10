
# from app.models import db

# class Administrateur(db.Model):
#     __tablename__ = 'administrateurs'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     password = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)

from mongoengine import Document, StringField, EmailField, IntField

class Administrateur(Document):
    meta = {'collection': 'administrateurs'}  # Nom de la collection MongoDB

    # id = IntField(primary_key=True)  # Vous pouvez gérer manuellement l'incrémentation si nécessaire
    password = StringField(required=True, max_length=200)
    email = EmailField(required=True, unique=True)  # Utilisation d'un champ EmailField pour valider les emails
