from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.user import User
from app.models.transaction import Transaction
from app.models.stock import Stock
import os, requests

class User:
    def __init__(self, user_id, username, password, is_logged_in):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.is_logged_in = is_logged_in


users = [
    User(1, "user1", "user1pw", False),
    User(2, "user2", "user2pw", True),
    User(3, "user3", "user3pw", True),
    User(4, "user4", "user4pw", False),
]

# create blueprint here
user_bp = Blueprint("User", __name__, url_prefix="/users")

#VALIDATE MODEL
def validate_model(class_obj,id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"{id} is an invalid id"}, 400))
    query_result = class_obj.query.get(id)
    if not query_result:
        abort(make_response({"message":f"{id} not found"}, 404))

    return query_result


# routes go here
@user_bp.route("", methods=["GET"])
def get_all_users():
    users_response = []
    for user in users:
        users_response.append({
            "user_id": user.user_id,
            "username": user.username,
            "password": user.password,
            "is_logged_in": user.is_logged_in
        })

    return jsonify(users_response)