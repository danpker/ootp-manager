"""Base file for the flask application."""
import os

from flask import (
    Flask,
)
from yaml import safe_load

from db import db
from views.list import players_list

config_file = os.environ.get("CONFIG")

if config_file is None:
    raise ValueError("Environment variable: CONFIG is not set.")

with open(config_file) as f:
    config = safe_load(f)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config["db_url"]
app.register_blueprint(players_list)
db.init_app(app)
