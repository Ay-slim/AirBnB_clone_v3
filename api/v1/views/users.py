#!/usr/bin/python3
"""Module defining users API endpoints"""

from flask import Flask, abort, request, jsonify
from api.v1.views import app_views
from models.user import User
from models import storage


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    """'/users route to display all users"""
    objects = storage.all(User)
    users = []
    for user in objects.values():
        users.append(user.to_dict())
    return jsonify(users)


@app_views.route('/users/<string:user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user_by_id(user_id):
    """'/users/<user_id>' route to get user by object id"""
    userObject = storage.get(User, user_id)
    if userObject is None:
        abort(404)
    return jsonify(userObject.to_dict())


@app_views.route('/users', methods=['POST'],
                 strict_slashes=False)
def post_users():
    """A route that creates a user"""
    req_body = None
    try:
        req_body = request.get_json()
        if not req_body:
            raise TypeError("Invalid")
    except Exception:
        abort(400, {'Not a JSON'})
    if "email" not in req_body:
        abort(400, {'Missing email'})
    if "password" not in req_body:
        abort(400, {'Missing password'})
    new_user_obj = User(
            email=req_body['email'],
            password=req_body['password'])
    storage.new(new_user_obj)
    storage.save()
    return jsonify(new_user_obj.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def put_user(user_id):
    """This route updates user and returns a JSON response"""
    req_body = None
    try:
        req_body = request.get_json()
        if not req_body:
            raise TypeError("Invalid")
    except Exception:
        abort(400, {'Not a JSON'})
    userObject = storage.get(User, user_id)
    if userObject is None:
        abort(404)
    ignoreKeys = ['id', 'created_at', 'email', 'updated_at']
    ret_obj = {}
    for key, val in req_body.items():
        if key not in ignoreKeys:
            setattr(userObject, key, val)
    storage.save()
    return jsonify(userObject.to_dict()), 200


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """Route to delete a user"""
    userObject = storage.get(User, user_id)
    if userObject is None:
        abort(404)
    storage.delete(userObject)
    storage.save()
    return jsonify({}), 200
