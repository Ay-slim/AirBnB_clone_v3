#!/usr/bin/python3
"""Module to define API routes using flask"""

from flask import Flask, Blueprint, jsonify
from models import storage
from os import getenv
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)

app.register_blueprint(app_views, url_prefix='/api/v1')
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def app_teardown(exception):
    """Tear down method implementation"""
    storage.close()
git

@app.errorhandler(404)
def not_found(error):
    """Not found error handler"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    env_host = getenv('HBNB_API_HOST', '0.0.0.0')
    env_port = getenv('HBNB_API_PORT', 5000)
    app.run(host=env_host, port=env_port, threaded=True)
