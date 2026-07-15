from flask import Blueprint, request, jsonify, g
from services.job_service import create_job, get_jobs, update_job, delete_job
from utils.auth_decorator import token_required


jobs_bp = Blueprint("jobs", __name__)


# route to  create job
@jobs_bp.route("/jobs", methods=["POST"])
@token_required
def create_job_route():

    data = request.get_json()
    user = g.user

    result = create_job(data, user)

    if result["success"]:
        return jsonify(result), 201
    return jsonify(result), 500


# Get jobs
@jobs_bp.route("/jobs", methods=["GET"])
@token_required
def get_jobs_route():

    user = g.user

    result = get_jobs(user)

    if result["success"]:
        return jsonify(result), 200

    return jsonify(result), 404


# add update route


@jobs_bp.route("/jobs/<int:job_id>", methods=["PUT"])
@token_required
def update_job_route(job_id):

    data = request.get_json()

    user = g.user

    result = update_job(job_id, data, user)

    if result["success"]:
        return jsonify(result), 200

    return jsonify(result), 500


# delete jobs route
@jobs_bp.route("/jobs/<int:job_id>", methods=["DELETE"])
@token_required
def delete_job_route(job_id):

    user = g.user

    result = delete_job(job_id, user)

    if result["success"]:
        return jsonify(result), 200

    return jsonify(result), 500
