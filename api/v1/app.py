#!/usr/bin/python3
"""Modeule to define API routes"""

from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views


env_host = getenv("HBNB_API_HOST")
env_port = getenv("HBNB_API_PORT")
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def app_teardown(exception):
    """Tear down method implementation"""
    storage.close()


if __name__ == "__main__":
    host = env_host if env_host else 5000
    port = env_port if env_port else '0.0.0.0'
    app.run(host=host, port=port, threaded=True)
