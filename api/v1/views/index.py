#!/usr/bin/python3
"""
    Here we talk of the indexes
"""
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """ Return the page status """
    return {"status": "OK"}
