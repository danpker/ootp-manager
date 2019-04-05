"""List view for players."""
from flask import render_template

from base import app
from db.models import Player


@app.route("/")
@app.route("/index")
def index():
    """Return a list of players."""
    players = Player.query.all()
    return render_template(
        "index.html", players=players, title="List of players")
