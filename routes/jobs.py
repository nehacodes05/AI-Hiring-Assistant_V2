from flask import Blueprint, request, jsonify, g
from services.job_service import create_job
from utils.auth_decorator import token_required

jobs_bp = Blueprint("jobs", __name__)


@jobs_bp.route("/jobs", methods=["POST"])
@token_required
def create_job_route():

    data = request.get_json()
    user = g.user

    result = create_job(data, user)

    if result["success"]:
        return jsonify(result), 201
    return jsonify(result), 500
