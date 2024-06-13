#!/usr/bin/python3
"""
    Here we manage all the User urls
"""
from flask import abort, request, make_response, jsonify
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route("/users", methods=['GET'])
def all_users():
    """ Get all the Users """
    users = storage.all(cls=User)
    result = []
    for _, x in users.items():
        result.append(x.to_dict())
    response = make_response(jsonify(result), 200)
    return response


@app_views.route("/users/<user_id>", methods=['GET'])
def user_by_id(user_id):
    """ Get a user be id """
    user = storage.get(cls=User, id=user_id)
    if user is None:
        abort(404)
    response = make_response(user.to_dict(), 200)
    return response


@app_views.route("/users/<user_id>", methods=['DELETE'])
def delete_user_by_id(user_id):
    """ Delete a particular User """
    user = storage.get(cls=User, id=user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    response = make_response({}, 200)
    return response


@app_views.route("/users", methods=['POST'])
def new_user_object():
    """ Creating new object """
    try:
        body = request.get_json()
    except Exception:
        response = make_response({"error": "Not a JSON"}, 400)
        return response
    if 'email' not in list(body.keys()):
        response = make_response({"error": "Missing email"}, 400)
        return response
    if 'password' not in list(body.keys()):
        return make_response({"error": "Missing password"}, 400)
    user = User(email=body['email'], password=body['password'])
    user.first_name = body.get('first_name', None)
    user.last_name = body.get('last_name', None)
    user.save()
    response = make_response(user.to_dict(), 201)
    return response


@app_views.route("/users/<user_id>", methods=['PUT'])
def update_user_by_id(user_id):
    """ Lets update that user """
    user = storage.get(cls=User, id=user_id)
    if user is None:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        return make_response({"error": "Not a JSON"}, 400)
    user.first_name = body.get('first_name', user.first_name)
    user.last_name = body.get('last_name', user.last_name)
    user.password = body.get('password', user.password)
    user.save()
    response = make_response(user.to_dict(), 200)
    return response
