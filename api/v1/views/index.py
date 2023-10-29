#!/usr/bin/python3
"""Module that handles status route declaration"""

import models
from models import storage
from models.base_model import BaseModel
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """Function to execute status route logic"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats_count():
    """'/stats' route that retrieves and display json Responses"""
    todos = {'states': State, 'users': User,
             'amenities': Amenity, 'cities': City,
             'places': Place, 'reviews': Review}
    for key in todos:
        todos[key] = storage.count(todos[key])
    return jsonify(todos)
