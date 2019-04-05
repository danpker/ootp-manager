#!/usr/bin/env python3
# vim: set syntax=python
from base import db
from db.models import *

db.drop_all()
db.create_all()
