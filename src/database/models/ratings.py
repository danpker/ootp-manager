"""Model for Player ratings."""
import statistics

from database import db


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

    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(5), nullable=False)
    level = db.Column(db.Integer, nullable=False)

    # attribute ratings
    contact = db.Column(db.Integer, nullable=False)
    gap_power = db.Column(db.Integer, nullable=False)
    power = db.Column(db.Integer, nullable=False)
    eye = db.Column(db.Integer, nullable=False)
    k = db.Column(db.Integer, nullable=False)

    stuff = db.Column(db.Integer, nullable=False)
    movement = db.Column(db.Integer, nullable=False)
    control = db.Column(db.Integer, nullable=False)

    # potential ratings
    contact_potential = db.Column(db.Integer, nullable=False)
    gap_power_potential = db.Column(db.Integer, nullable=False)
    power_potential = db.Column(db.Integer, nullable=False)
    eye_potential = db.Column(db.Integer, nullable=False)
    k_potential = db.Column(db.Integer, nullable=False)

    stuff_potential = db.Column(db.Integer, nullable=False)
    movement_potential = db.Column(db.Integer, nullable=False)
    control_potential = db.Column(db.Integer, nullable=False)

    @property
    def batting_median(self):
        return statistics.median([
            self.contact,
            self.gap_power,
            self.power,
            self.eye,
            self.k,
        ])

    @property
    def batting_potential_diff(self):
        return self.batting_potential_median - self.batting_median

    @property
    def pitching_potential_diff(self):
        return self.pitching_potential_median - self.pitching_median

    @property
    def pitching_median(self):
        return statistics.median([
            self.stuff,
            self.movement,
            self.control,
        ])

    @property
    def batting_potential_median(self):
        return statistics.median([
            self.contact_potential,
            self.gap_power_potential,
            self.power_potential,
            self.eye_potential,
            self.k_potential,
        ])

    @property
    def pitching_potential_median(self):
        return statistics.median([
            self.stuff_potential,
            self.movement_potential,
            self.control_potential,
        ])
