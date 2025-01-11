
from flask import Flask
from flask_pymongo import PyMongo
import logging
from mongoengine import connect

from app.routes import bp_main
from app.routes import bp_auth

# Configure le niveau de log pour pymongo
logging.getLogger('pymongo').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'bab596d6d77abcd51fc5cdd1a3856e81749f225d'
    app.config["MONGO_URI"] = "mongodb://mongo:OZaPicRClcWHfwKTMIIOqAOGhMumMQvY@junction.proxy.rlwy.net:29950" # "mongodb+srv://l0rd_9h057:4NSZCNQDRyGi2IEw@birthcontrolcluster.bzeks.mongodb.net/birthControl?retryWrites=true&w=majority" # "mongodb+srv://l0rd_9h057:4NSZCNQDRyGi2IEw@birthcontrolcluster.bzeks.mongodb.net/?retryWrites=true&w=majority&appName=birthControlCluster"

    mongodb_client = PyMongo(app)
    db = mongodb_client.db

    # Connect to MongoDB
    connect(
        db='birthControl',  # replace with your database name
        host=app.config["MONGO_URI"],         # replace with your MongoDB host
        port=27017,               # replace with your MongoDB port if different
        username='mongo', # 'l0rd_9h057', # add this if authentication is required
        password='OZaPicRClcWHfwKTMIIOqAOGhMumMQvY', # '4NSZCNQDRyGi2IEw', # add this if authentication is required
        alias='default'           # alias for the connection
    )

    logging.debug("liaison des routes.....")
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_auth)

    return app
