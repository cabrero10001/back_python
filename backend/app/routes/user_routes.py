# app/routes/user_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.user_controller import register_user, login_user

bp = Blueprint("users", __name__, url_prefix="/users")

@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    return register_user(data)

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    return login_user(data)
