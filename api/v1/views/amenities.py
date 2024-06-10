#!/usr/bin/python3
"""
    Here we manage all the State urls
"""
from flask import jsonify, abort, request, make_response
from models.amenity import Amenity
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route("/amenities", methods=['GET'])
def get_amenities():
    """ Get all amenities """
    data = storage.all(cls=Amenity)
    amenities = []
    for _, x in data.items():
        amenities.append(x.to_dict())
    
    response = make_response(jsonify(amenities), 200)
    return response


@app_views.route("/amenities/<amenity_id>", methods=['GET'])
def get_amenity_by_id(amenity_id):
    """ Get amenity by ID """
    amenity = storage.get(cls=Amenity, id=amenity_id)
    if amenity is None:
        abort(404)
    response = make_response(amenity.to_dict(), 200)
    return response


@app_views.route("/amenities/<amenity_id>", methods=['DELETE'])
def delete_amenity(amenity_id):
    """ Delete amenity by id """
    amenity = storage.get(cls=Amenity, id=amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(obj=amenity)
    storage.save()
    response = make_response({}, 200)
    return response


@app_views.route("/amenities", methods=['POST'])
def post_amenities():
    """ Create new Amenity """
    try:
        body = request.get_json()
    except Exception:
        abort(jsonify(message="Not a JSON"), 400)
    if 'name' not in list(body.keys()):
        abort(jsonify(message="Missing name"), 400)
    amenity = Amenity(name=body['name'])
    amenity.save()
    response = make_response(amenity.to_dict(), 201)
    return response


@app_views.route("/amenities/<amenity_id>", methods=['PUT'])
def put_amennities(amenity_id):
    """ Update the amenity with put """
    amenity = storage.get(cls=Amenity, id=amenity_id)
    if amenity is None:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        abort(jsonify(message="Not a JSON"), 400)
    if 'name' in list(body.keys()):
        amenity.name = body['name']
        amenity.save()
    response = make_response(amenity.to_dict(), 200)
    return response
