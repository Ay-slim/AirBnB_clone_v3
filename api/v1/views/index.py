#!/usr/bin/python3
"""Module that handles status route declaration"""

from api.v1.views import app_views
from flask import jsonify
import models
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def status():
    """Function to execute status route logic"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats_count():
    """'/stats' route that retrieves and display json Responses"""
    classes = {
            "amenities": Amenity,
            "cities": City,
            "places": Place,
            "reviews": Review,
            "states": State,
            "users": User
            }
    todos = {}
    for key, val in classes.items():
        todos[key] = storage.count(val)
    return jsonify(todos)
