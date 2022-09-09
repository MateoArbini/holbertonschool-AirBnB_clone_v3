#!/usr/bin/python3
"""file users"""
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify, request, abort
import json


classes = {"amenities": Amenity, "cities": City,
           "places": Place, "reviews": Review, "states": State, "users": User}


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def users(user_id=None):
    """Users funtions"""
    if request.method == 'GET':
        if user_id is None:
            list_of_users = []
            users = storage.all(User)
            for key, value in users.items():
                obj = value.to_dict()
                list_of_users.append(obj)
            return jsonify(list_of_users)
        else:
            users = storage.all(User)
            for key, value in users.items():
                if users[key].id == user_id:
                    return jsonify(value.to_dict())
            abort(404)
    elif request.method == 'DELETE':
        users = storage.all()
        for key, value in users.items():
            if users[key].id == user_id:
                storage.delete(users[key])
                storage.save()
                return jsonify({}), 200
        abort(404)
    elif request.method == 'POST':
        try:
            body = request.get_json()
            if 'email' in body:
                value = {}
                value['email'] = body['email']
                new_user = User(**value)
                new_user.save()
                return jsonify(new_user.to_dict()), 201
            else:
                return jsonify({
                    "error": "Missing email"
                }), 400
            if 'password' in body:
                value = {}
                value['password'] = body['password']
                new_user = User(**value)
                new_user.save()
                return jsonify(new_user.to_dict()), 201
            else:
                return jsonify({
                    "error": "Missing password"
                }), 400
        except Exception as error:
            return jsonify({
                    "error": "Not a JSON"
                }), 400
    else:
        try:
            notAttr['id', 'created_at', 'updated_at', 'email']
            body = request.get_json()
            users = storage.all(User)
            for key, value in users.items():
                if users[key].id == user_id:
                    for k, v in body.items():
                        if k not in notAttr:
                            setattr(value, k, v)
                        value.save()
                        return jsonify(value.to_dict()), 200
            return jsonify({"error": "Not found"}), 400
        except Exception as error:
            return jsonify({
                "error": "Not a JSON"
            }), 400
