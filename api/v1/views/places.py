#!/usr/bin/python3
"""
    Here we manage all the Place urls
"""
from flask import jsonify, abort, request, make_response
from models.city import City
from models.user import User
from models.place import Place
from models import storage
from api.v1.views import app_views


@app_views.route("/cities/<city_id>/places", methods=['GET'])
def places(city_id):
    """ List all the places belonging to a city """
    city = storage.get(cls=City, id=city_id)
    if city is None:
        abort(404)
    places = []
    for place in city.places:
        places.append(place.to_dict())
    response = make_response(places, 200)
    return response


@app_views.route("/places/<place_id>", methods=['GET'])
def show_place(place_id):
    """ Get a city based on its ID """
    place = storage.get(cls=Place, id=place_id)
    if place is None:
        abort(404)
    response = make_response(place.to_dict(), 200)
    return response


@app_views.route("/places/<place_id>", methods=['DELETE'])
def delete_place(place_id):
    """ Delete city by ID """
    place = storage.get(cls=Place, id=place_id)
    if place is None:
        abort(404)
    place.delete()
    storage.save()
    response = make_response({}, 200)
    return response


@app_views.route("/cities/<city_id>/places", methods=['POST'])
def create_place(city_id):
    """ Create new city given the state """
    city = storage.get(cls=City, id=city_id)
    if city is None:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        abort(jsonify(message="Not a JSON"), 400)
    if 'user_id' not in list(body.keys()):
        abort(jsonify(message="Missing user_id"), 400)
    user = storage.get(cls=User, id=body.get('user_id', None))
    if user is None:
        abort(404)
    if 'name' not in list(body.keys()):
        abort(jsonify(message="Missing name"), 400)
    place = Place(user_id=user.id, city_id=city.id, name=body.get('name', None))
    place.description = body.get('description', None)
    place.number_rooms = body.get('number_rooms', 0)
    place.number_bathrooms = body.get('number_bathrooms', 0)
    place.max_guest = body.get('max_guest', 0)
    place.price_by_night = body.get('price_by_night', 0)
    place.latitude = body.get('latitude', 0.0)
    place.longitude = body.get('longitude', 0.0)
    place.save()
    response = make_response(place.to_dict(), 201)
    return response


@app_views.route("/places/<place_id>", methods=['PUT'])
def update_place(place_id):
    """ Update a given instance of city """
    place = storage.get(cls=Place, id=place_id)
    if place is None:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        abort({"message": "Not a JSON"}, 400)
    place.name = body.get('name', place.name)
    place.description = body.get('description', place.description)
    place.number_rooms = body.get('number_rooms', place.number_rooms)
    place.number_bathrooms = body.get('number_bathrooms',
                                      place.number_bathrooms)
    place.max_guest = body.get('max_guest', place.max_guest)
    place.price_by_night = body.get('price_by_night', place.price_by_night)
    place.latitude = body.get('latitude', place.latitude)
    place.longitude = body.get('longitude', place.longitude)
    place.save()
    response = make_response(place.to_dict(), 200)
    return response
