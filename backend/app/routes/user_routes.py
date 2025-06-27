# app/routes/user_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.user_controller import register_user, login_user
from app.controllers.diagnostico_controller import guardar_diagnostico

bp = Blueprint("users", __name__, url_prefix="/users")

@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    return register_user(data)

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    return login_user(data)

@bp.route("/diagnostico", methods=["POST", "OPTIONS"])
def Diagnostico():
    if request.method == "OPTIONS":
        return '', 200
    
    print("Diagnóstico recibido en backend")
    data= request.get_json()
    print(data)
    return guardar_diagnostico(data)