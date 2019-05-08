"""List view for players."""
from flask import Blueprint
import pandas
import seaborn as sns

from views.base import (
    LATEST_SNAPSHOT,
    snapshot_to_path,
)

players_list = Blueprint("players_list", __name__)


@players_list.route("/")
def index():
    """Return a list of players."""
    df = pandas.read_pickle(snapshot_to_path(LATEST_SNAPSHOT))
    CM = sns.light_palette("green", as_cmap=True)
    return df.style.background_gradient(cmap=CM).render()
