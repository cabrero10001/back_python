from flask import Blueprint, request, jsonify
from app.controllers.user_controller import get_all_user, create_user
bp = Blueprint("users", __name__, url_prefix="/users")
@bp.route("/", methods=["GET"])
def list_users():
    return jsonify(get_all_user())
@bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()
    return create_user(data)
