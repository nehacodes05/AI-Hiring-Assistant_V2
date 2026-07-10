import jwt
from flask import request, jsonify
from utils.jwt_helper import verify_token
from functools import wraps


def token_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("authorization")

        if not auth_header:
            return jsonify(
                {"success": "False", "message": "authorised token is missing"}
            ), 401

        parts = auth_header.split()
        if len(parts) != 2 or parts[0] != "Bearer":
            return jsonify(
                {"succes": "False", "message": "Inavlid authorisation header"}
            ), 401

        token = parts[1]

        try:
            payload = verify_token(token)

        except jwt.ExpiredSignatureError:
            return jsonify(
                {"succcess": "False", "message": "your taken has expired"}
            ), 401

        except jwt.InvalidTokenError:
            return jsonify({"succcess": "False", "message": "Unauthorised token"}), 401

        return route_function(*args, **kwargs)

    return wrapper
