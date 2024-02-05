#!/usr/bin/python3
"""
view for User objects that handles all default RestFul API actions
"""
from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.user import User


@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def handle_users():
    """Retrieves the list of all User objects or create a new User object"""
    if request.method == 'GET':
        users = storage.all("User").values()
        users_list = [user.to_dict() for user in users]
        return jsonify(users_list), 200
    elif request.method == 'POST':
        if not request.is_json:
            abort(400, "Not a JSON")
        data = request.get_json()
        if 'email' not in data:
            abort(400, "Missing email")
        if 'password' not in data:
            abort(400, "Missing password")
        user = User(**data)
        storage.new(user)
        storage.save()
        return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['GET', 'DELETE', 'PUT'], strict_slashes=False)
def user_byid(user_id):
    """Retrieves a User object by id, delete or update a User object"""
    user = storage.get("User", user_id)
    if user:
        if request.method == 'GET':
            return jsonify(user.to_dict()), 200
        elif request.method == 'DELETE':
            storage.delete(user)
            storage.save()
            return jsonify({}), 200
        elif request.method == 'PUT':
            if not request.is_json:
                abort(400, "Not a JSON")
            data = request.get_json()
            ignore_keys = ["id", "created_at", "updated_at"]
            for key, value in data.items():
                if key not in ignore_keys:
                    setattr(user, key, value)
            storage.save()
            return jsonify(user.to_dict()), 200
    else:
        abort(404)
