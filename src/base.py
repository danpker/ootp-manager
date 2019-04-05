from flask import (
    Flask,
)
from flask_sqlalchemy import SQLAlchemy
from flask import render_template



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route("/")
@app.route("/index")
def index():
    from db.models import Player
    players = Player.query.all()
    return render_template("index.html", players=players)
