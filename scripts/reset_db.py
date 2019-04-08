#!/usr/bin/env python3
# vim: set syntax=python
"""Drop and recreate the DB."""
from base import app
from database import db
from database.models import * # noqa

with app.app_context():
    db.drop_all()
    db.create_all()
