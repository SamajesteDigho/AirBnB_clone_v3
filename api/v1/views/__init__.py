#!/usr/bin/python3
"""
    Here is the view initialization instance
"""
from flask import Blueprint
app_views = Blueprint(name="v1", import_name=__name__, url_prefix="/api/v1")
from api.v1.views.index import *
from api.v1.views import states
from api.v1.views import cities
