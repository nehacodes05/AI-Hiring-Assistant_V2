from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user
from utils.auth_decorator import token_required


auth_bp = Blueprint("auth", __name__)


# signup up
@auth_bp.route("/signup", methods=["POST"])
def signup():

    data = request.get_json()

    full_name = data["full_name"]
    email = data["email"]
    password = data["password"]
    role = data["role"]

    success, message, data = register_user(full_name, email, password, role)

    if success:
        return jsonify({"success: True,message": message}), 201

    return jsonify({"success": False, "message": message}), 400


# login route
@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data["email"]
    password = data["password"]

    success, message, token = login_user(email, password)

    # returning Json response
    if success:
        return jsonify({"success": True, "message": message, "token": token}), 200

    return jsonify({"success": False, "message": message}), 401


# Profile route(testing authentication using this simple routeS)
@auth_bp.route("/profile", methods=["GET"])
@token_required
def profile():
    return jsonify({"success": True, "message": "Athenticated successfully"}), 200
