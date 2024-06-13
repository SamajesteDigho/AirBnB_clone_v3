#!/usr/bin/python3
"""
    Here we manage all the State urls
"""
from flask import abort, request, make_response, jsonify
from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route("/states/<state_id>/cities", methods=['GET'])
def cities(state_id):
    """ List all the cities belonging to a state """
    state = storage.get(cls=State, id=state_id)
    if state is None:
        abort(404)
    cities = []
    for city in state.cities:
        cities.append(city.to_dict())
    response = make_response(jsonify(cities), 200)
    return response


@app_views.route("/cities/<city_id>", methods=['GET'])
def city_by_id(city_id):
    """ Get a city based on its ID """
    city = storage.get(cls=City, id=city_id)
    if city is None:
        abort(404)
    response = make_response(city.to_dict(), 200)
    return response


@app_views.route("/cities/<city_id>", methods=['DELETE'])
def city_delete(city_id):
    """ Delete city by ID """
    city = storage.get(cls=City, id=city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    response = make_response({}, 200)
    return response


@app_views.route("/states/<state_id>/cities", methods=['POST'])
def new_city(state_id):
    """ Create new city given the state """
    state = storage.get(cls=State, id=state_id)
    if state is None:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        response = make_response({"error": "Not a JSON"}, 400)
        return response
    if 'name' not in list(body.keys()):
        response = make_response({"error": "Missing name"}, 400)
        return response
    city = City(state_id=state_id, name=body.get('name', None))
    city.save()
    response = make_response(city.to_dict(), 201)
    return response


@app_views.route("/cities/<city_id>", methods=['PUT'])
def update_city(city_id):
    """ Update a given instance of city """
    city = storage.get(cls=City, id=city_id)
    if city is None:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        response = make_response({"error": "Not a JSON"}, 400)
        return response
    city.name = body.get('name', city.name)
    city.save()
    response = make_response(city.to_dict(), 200)
    return response
