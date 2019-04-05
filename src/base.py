"""Base file for the flask application."""
import os

from flask import (
    Flask,
)
from flask_sqlalchemy import SQLAlchemy
from yaml import safe_load

config_file = os.environ.get("CONFIG")

if config_file is None:
    raise ValueError("Environment variable: CONFIG is not set.")

with open(config_file) as f:
    config = safe_load(f)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config["db_url"]
db = SQLAlchemy(app)
