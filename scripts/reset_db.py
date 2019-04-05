#!/usr/bin/env python3
# vim: set syntax=python
"""Drop and recreate the DB."""
from base import db
from db.models import * # noqa

db.drop_all()
db.create_all()
