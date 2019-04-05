from base import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(36), nullable=False, unique=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)

    @property
    def latest_snapshot(self):
        pass

