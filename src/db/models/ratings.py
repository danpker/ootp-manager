"""Model for Player ratings."""
from db import db


class Ratings(db.Model):
    """Class for Player ratings."""

    snapshot_id = db.Column(
        db.Integer, db.ForeignKey("snapshot.id"), nullable=False,
        primary_key=True)
    snapshot = db.relationship("Snapshot")

    player_id = db.Column(
        db.Integer, db.ForeignKey("player.id"), nullable=False,
        primary_key=True)
    player = db.relationship("Player")

    position = db.Column(db.String(5), nullable=False)
    level = db.Column(db.String(5), nullable=False)

    # attribute ratings
    contact = db.Column(db.Integer, nullable=False)
    gap_power = db.Column(db.Integer, nullable=False)
    power = db.Column(db.Integer, nullable=False)
    eye = db.Column(db.Integer, nullable=False)
    k = db.Column(db.Integer, nullable=False)
