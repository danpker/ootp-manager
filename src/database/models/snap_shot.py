"""Model for Ratings snapshots."""
from database import db


class Snapshot(db.Model):
    """Class for Snapshot model."""

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True, nullable=False)

    @staticmethod
    def latest_snapshot():
        """Return the latest snapshot."""
        return db.session.query(
           Snapshot).order_by(Snapshot.date.desc()).first()
