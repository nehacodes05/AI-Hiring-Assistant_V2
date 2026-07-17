from flask import Blueprint, jsonify, g, request, send_file
from utils.auth_decorator import token_required, role_required
from services.application_service import (
    apply_to_job,
    get_job_applications,
    upload_resume,
    download_resume,
)

applications_bp = Blueprint("applications", __name__)


# apply to jobs route
@applications_bp.route("/jobs/<int:job_id>/apply", methods=["POST"])
@token_required
@role_required("candidate")
def apply_job_route(job_id):

    # GEt the authenticated user's information from jwt
    user = g.user

    result = apply_to_job(job_id, user)

    if result["success"]:
        return jsonify(result), 201
    return jsonify(result), 500


# route to get applications b y recruiter
@applications_bp.route("/jobs/<int:job_id>/applications", methods=["GET"])
@token_required
@role_required("recruiter")
def get_applications_route(job_id):

    # get the logged in user from the jwt payload
    user = g.user

    result = get_job_applications(job_id, user)

    if result["success"]:
        return jsonify(result), 200
    return jsonify(result), 500


# route to upload resume
@applications_bp.route("/applications/<int:application_id>/resume", methods=["POST"])
@token_required
@role_required("candidate")
def upload_resume_route(application_id):

    user = g.user

    # Get the uploaded PDF from the request
    resume = request.files.get("resume")

    result = upload_resume(application_id, resume, user)

    if result["success"]:
        return jsonify(result), 200
    return jsonify(result), 500


# download uploaded resume route
@applications_bp.route("/applications/<int:application_id>/resume", methods=["GET"])
@token_required
@role_required("recruiter")
def download_resume_route(application_id):
    user = g.user

    result = download_resume(application_id, user)

    if not result["success"]:
        return jsonify(result), 404

    return send_file(
        result["resume_path"],
        as_attachment=True,
        download_name=f"application_{application_id}.pdf",
    )
