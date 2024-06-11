#!/usr/bin/python3
"""
    Here we manage all the Place urls
"""
from flask import jsonify, abort, request, make_response
from models.review import Review
from models.user import User
from models.place import Place
from models import storage
from api.v1.views import app_views


@app_views.route("/places/<place_id>/reviews", methods=['GET'])
def reviews(place_id):
    """ List all the places belonging to a city """
    place = storage.get(cls=Place, id=place_id)
    if place is None:
        abort(404)
    reviews = []
    for review in place.reviews:
        reviews.append(review.to_dict())
    response = make_response(reviews, 200)
    return response


@app_views.route("/reviews/<review_id>", methods=['GET'])
def show_review(review_id):
    """ Get a city based on its ID """
    review = storage.get(cls=Review, id=review_id)
    if review is None:
        abort(404)
    response = make_response(review.to_dict(), 200)
    return response


@app_views.route("/reviews/<review_id>", methods=['DELETE'])
def delete_review(review_id):
    """ Delete city by ID """
    review = storage.get(cls=Review, id=review_id)
    if review is None:
        abort(404)
    review.delete()
    storage.save()
    response = make_response({}, 200)
    return response


@app_views.route("/places/<place_id>/reviews", methods=['POST'])
def create_review(place_id):
    """ Create new city given the state """
    place = storage.get(cls=Place, id=place_id)
    if place is None:
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
    if 'text' not in list(body.keys()):
        abort(jsonify(message="Missing text"), 400)
    review = Review(user_id=user.id, place_id=place.id, text=body.get('text', None))
    review.save()
    response = make_response(review.to_dict(), 201)
    return response


@app_views.route("/reviews/<review_id>", methods=['PUT'])
def update_review(review_id):
    """ Update a given instance of city """
    review = storage.get(cls=Review, id=review_id)
    if review is None:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        abort({"message": "Not a JSON"}, 400)
    review.text = body.get('text', review.text)
    review.save()
    response = make_response(review.to_dict(), 200)
    return response
