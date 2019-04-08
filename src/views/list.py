"""List view for players."""
from flask import (
    Blueprint,
    render_template,
)

from database.models import Player


players_list = Blueprint("players_list", __name__)


@players_list.route("/")
def index():
    """Return a list of players."""
    players = Player.query.all()
    return render_template(
        "index.html", players=players, title="List of players")
