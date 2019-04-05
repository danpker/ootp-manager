"""Model for Ratings snapshots."""
from base import db


class Snapshot(db.Model):
    """Class for Snapshot model."""

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True, nullable=False)
