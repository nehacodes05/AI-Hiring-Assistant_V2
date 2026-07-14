import jwt
from flask import request, jsonify, g
from utils.jwt_helper import verify_token
from functools import wraps


def token_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("authorization")

        if not auth_header:
            return jsonify(
                {"success": False, "message": "authorised token is missing"}
            ), 401

        parts = auth_header.split()
        if len(parts) != 2 or parts[0] != "Bearer":
            return jsonify(
                {"succes": False, "message": "Inavlid authorisation header"}
            ), 401

        token = parts[1]

        try:
            payload = verify_token(token)
            g.user = payload

        except jwt.ExpiredSignatureError:
            return jsonify(
                {"succcess": False, "message": "your token has expired"}
            ), 401

        except jwt.InvalidTokenError:
            return jsonify({"succcess": False, "message": "Unauthorised token"}), 401

        return route_function(*args, **kwargs)

    return wrapper


# authentication decorator
def role_required(required_role):

    def decorator(route_function):

        @wraps(route_function)
        def wrapper(*args, **kwargs):

            user = g.user
            if user["role"] != required_role:
                return jsonify({"success": False, "message": "Access denied"}), 403

            return route_function(*args, **kwargs)

        return wrapper

    return decorator
