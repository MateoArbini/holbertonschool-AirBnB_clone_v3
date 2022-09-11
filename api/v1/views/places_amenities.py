#!/usr/bin/python3
"""file places_reviews"""
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
import json

classes = {"amenities": Amenity, "cities": City,
           "places": Place, "reviews": Review, "states": State, "users": User}

storage_t = getenv("HBNB_TYPE_STORAGE")


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def review(place_id):
    if storage_t == "db":
        place = storage.get("Place", place_id)
        if place is None:
            abort(404)
        list_ameniti = []
        for i in place.amenities:
            list_ameniti.append(i.to_dict())
    else:
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        storage.reload()
