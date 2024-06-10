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
    data = storage.all(cls=State)
    result = []
    for id, x in data.items():
        result.append(x.to_dict())
    return jsonify(result)


@app_views.route("/states/<state_id>", methods=['GET'])
def state_by_id(state_id):
    """ Get a state be id """
    data = storage.get(cls=State, id=state_id)
    if data is None:
        abort(404)
    else:
        return jsonify(data.to_dict())


@app_views.route("/states/<state_id>", methods=['DELETE'])
def delete_state_by_id(state_id):
    """ Delete a particular state """
    data = storage.get(cls=State, id=state_id)
    print(data)
    if data is None:
        abort(404)
    else:
        storage.delete(obj=data)
        # storage.save()
        response = make_response(jsonify({}), 200)
        return response


@app_views.route("/states", methods=['POST'])
def new_state_object():
    """ Creating new object """
    try:
        info = request.get_json()
    except Exception:
        abort(jsonify(error="Mising name"), 400)
    state = State(name=info['name'])
    response = make_response(jsonify(state.to_dict()), 201)
    return response


@app_views.route("/states/<state_id>", methods=['PUT'])
def update_state_by_id(state_id):
    """ Lets update that state """
    state = storage.get(cls=State, id=state_id)
    if state is None:
        abort(404)
    try:
        info = request.get_json()
    except Exception:
        abort(jsonify(error="Not a JSON"), 400)
    if 'name' in list(info.keys()):
        state.name = info['name']
        state.save()
    response = make_response(jsonify(state.to_dict()), 200)
    return response
