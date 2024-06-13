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
    amenities = storage.all(cls=Amenity)
    result = []
    for _, x in amenities.items():
        result.append(x.to_dict())
    response = make_response(jsonify(result), 200)
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
        response = make_response({"error": "Not a JSON"}, 400)
        return response
    if 'name' not in list(body.keys()):
        response = make_response({"error": "Missing name"}, 400)
        return response
    amenity = Amenity(name=body.get('name', None))
    amenity.save()
    response = make_response(amenity.to_dict(), 201)
    return response


@app_views.route("/amenities/<amenity_id>", methods=['PUT'])
def put_amenities(amenity_id):
    """ Update the amenity with put """
    amenity = storage.get(cls=Amenity, id=amenity_id)
    if amenity is None:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        response = make_response({"error": "Not a JSON"}, 400)
        return response
    amenity.name = body.get('name', amenity.name)
    amenity.save()
    response = make_response(amenity.to_dict(), 200)
    return response
