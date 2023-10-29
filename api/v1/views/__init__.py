#!/usr/bin/python3
"""Module for app.views implementation"""

from api.v1.views.index import *
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')