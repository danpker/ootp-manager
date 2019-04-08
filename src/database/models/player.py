"""Player model for players."""
from database import db
from database.models.snap_shot import Snapshot
from database.models.ratings import Ratings


class Player(db.Model):
    """Class for the Player model."""

    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(36), nullable=False, unique=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)

    @property
    def ratings(self):
        latest_snapshot = Snapshot.latest_snapshot()
        return (
            db.session.query(Ratings)
            .filter(Ratings.snapshot_id == latest_snapshot.id)
            .filter(Ratings.player_id == self.id)
            .one_or_none()
        )
