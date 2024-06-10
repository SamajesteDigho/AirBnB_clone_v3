#!/usr/bin/python3
"""
    Here we manage all the State urls
"""
from flask import jsonify, abort, request, make_response
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route("/states", methods=['GET'])
def all_states():
    """ Get all the states """
    states = storage.all(cls=State)
    result = []
    for _, x in states.items():
        result.append(x.to_dict())
    response = make_response(result, 200)
    return response


@app_views.route("/states/<state_id>", methods=['GET'])
def state_by_id(state_id):
    """ Get a state be id """
    state = storage.get(cls=State, id=state_id)
    if state is None:
        abort(404)
    response = make_response(state.to_dict(), 200)
    return response


@app_views.route("/states/<state_id>", methods=['DELETE'])
def delete_state_by_id(state_id):
    """ Delete a particular state """
    state = storage.get(cls=State, id=state_id)
    print(state)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    response = make_response({}, 200)
    return response


@app_views.route("/states", methods=['POST'])
def new_state_object():
    """ Creating new object """
    try:
        body = request.get_json()
    except Exception:
        abort(jsonify(error="Not a JSON"), 400)
    if 'name' not in list(body.keys()):
        abort(jsonify(error="Missing name"), 400)
    state = State(name=body.get('name', None))
    state.save()
    response = make_response(state.to_dict(), 201)
    return response


@app_views.route("/states/<state_id>", methods=['PUT'])
def update_state_by_id(state_id):
    """ Lets update that state """
    state = storage.get(cls=State, id=state_id)
    if state is None:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        abort(jsonify(error="Not a JSON"), 400)
    state.name = body.get('name', state.name)
    state.save()
    response = make_response(state.to_dict(), 200)
    return response
