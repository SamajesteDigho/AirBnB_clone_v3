#!/usr/bin/python3
"""
    Here we talk of the indexes
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

@app_views.route('/status')
def status():
    """ Return the page status """
    return {"status": "OK"}


@app_views.route("/stats")
def statistics():
    """ Return a json of the statistics """
    data = {}
    for key, cls in classes.items():
        name = key.lower()
        data[name] = storage.count(cls=cls)
    return jsonify(data)
