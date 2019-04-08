"""Player model for players."""
from db import db


class Player(db.Model):
    """Class for the Player model."""

    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(36), nullable=False, unique=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
