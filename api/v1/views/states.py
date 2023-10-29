#!/usr/bin/python3
""" State objects that handles RESTFul API module"""

from flask import Flask
from flask import Flask, abort
from api.v1.views import app_views
from os import name
from models.state import State
from flask import request


@app_views.route('/status', methods=['GET'] strict_slashes=False)
def to_get():
    """'/status' route to display state objects as JSON response"""
    objects = storage.all('State')
    lista = []
    for state in objects.values():
        lista.append(state.to_dict())
    return jsonify(lista)


@app_views.route('/states/<string:stateid>', methods=['GET'],
                 strict_slashes=False)
def to_get_id():
    """'/states/<state_id>' route to updates a State object id"""
    objects = storage.get('State', 'state_id')
    if objects is None:
        abort(404)
    return jsonify(objects.to_dict()), 'OK'


@app_views.route('/states/', methods=['POST'],
                 strict_slashes=False)
def post_states():
    """A route that creates a state"""
    response = request.get_json()
    if response id None:
        abort(400, {'Not a JSON'})
    if "name" not in response:
        abort(400, {'Missing name'})
    stateObject = State(name=response['name'])
    storage.new(stateObject)
    storage.save()
    return jsonify(stateObject.to_dict()), '201'


@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def put_state():
    """This route updates state as JSON response"""
    response = request.get_json()
    if response id None:
        abort(400, {'Not a JSON'})
    stateObject = storage.get(State, state_id)
    if stateObject is None:
        abort(404)
    ignoreKeys = ['id', 'created_at', 'updated_at']
    for key in response.items():
        if key not in ignoreKeys:
            setattr(stateObject, key)
    storage.save()
    return jsonify(stateObject.to_dict()), '200'


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleting():
    """JSON response to delete a state"""
    stateObject = storage.get(State, state_id)
    if stateObject is None:
        abort(404)
    storage.delete(stateObject)
    storage.save()
    return jsonify({}), '200'
