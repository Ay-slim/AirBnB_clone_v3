#!/usr/bin/python3
"""Module to define API routes using flask"""

from flask import Flask, jsonify
from models import storage
from os import getenv
from api.v1.views import app_views


env_host = getenv("HBNB_API_HOST")
env_port = getenv("HBNB_API_PORT")
app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def app_teardown(exception):
    """Tear down method implementation"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Not found error handler"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = env_host if env_host else '0.0.0.0'
    port = env_port if env_port else 5000
    app.run(host=host, port=port, threaded=True)
