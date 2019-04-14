from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from v2_flask.app import routes

db = SQLAlchemy()

app = Flask(__name__)


