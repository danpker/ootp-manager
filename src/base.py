"""Base file for the flask application."""
from flask import (
    Flask,
)

from views.list import players_list

app = Flask(__name__)
app.register_blueprint(players_list)
