#!/usr/bin/python3
"""
    Here we manage all the State urls
"""
from flask import jsonify, abort, request, make_response
from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route("/states/<state_id>/cities", methods=['GET'])