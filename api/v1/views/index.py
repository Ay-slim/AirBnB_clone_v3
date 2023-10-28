#!/usr/bin/python3
"""Module that handles status route declaration"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """Functio to execute status route logic"""
    return jsonify({"status": "OK"})
