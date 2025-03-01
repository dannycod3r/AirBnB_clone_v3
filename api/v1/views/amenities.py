#!/usr/bin/python3
"""
Amenity API
"""

from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET', 'POST'], strict_slashes=False)
def handle_amenities():
    """
    Handle GET and POST requests for amenities.
    GET: Retrieves the list of all Amenity objects.
    POST: Creates a new Amenity object.
    """
    if request.method == 'GET':
        amenities = storage.all(Amenity).values()
        amenities_list = [amenity.to_dict() for amenity in amenities]
        return jsonify(amenities_list), 200

    if request.method == 'POST':
        if not request.is_json:
            abort(400, "Not a JSON")

        data = request.get_json()
        if 'name' not in data:
            abort(400, "Missing name")

        amenity = Amenity(**data)
        storage.new(amenity)
        storage.save()

        return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def amenity_by_id(amenity_id):
    """
    Handle GET, DELETE, and PUT requests for a specific amenity.
    GET: Retrieves an Amenity object by ID.
    DELETE: Deletes an Amenity object by ID.
    PUT: Updates an Amenity object by ID.
    """
    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    if request.method == 'GET':
        return jsonify(amenity.to_dict()), 200

    elif request.method == 'DELETE':
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200

    elif request.method == 'PUT':
        if not request.is_json:
            abort(400, "Not a JSON")

        data = request.get_json()
        ignore_keys = ["id", "created_at", "updated_at"]

        for key, value in data.items():
            if key not in ignore_keys:
                setattr(amenity, key, value)

        storage.save()
        return jsonify(amenity.to_dict()), 200
