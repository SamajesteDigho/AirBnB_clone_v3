#!/usr/bin/python3
"""
    Here is the app file
"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(blueprint=app_views)


@app.teardown_appcontext
def teardown(exception):
    """ Tearing down the context """
    storage.close()


if __name__ == "__main__":
    """ Here we launch """
    host = getenv("HBNB_API_HOST", '0.0.0.0')
    port = getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
