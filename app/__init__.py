from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
#----------Settings Flask--------------#
app.env ='development'
app.debug='true'
port = 7000

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

from app import views

from app import admin_views
