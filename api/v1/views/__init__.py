#!/usr/bin/python3
"""
    Here is the view initialization instance
"""
from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint(url_prefix="/api/v1")
