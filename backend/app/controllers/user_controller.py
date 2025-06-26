# app/controllers/user_controller.py
from app.models.user_model import User
from app.models import db
from flask import jsonify

def register_user(data):
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return {"error": "Faltan campos"}, 400

    if User.query.filter_by(username=username).first():
        return {"error": "El usuario ya existe"}, 409

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return {"message": "Usuario registrado"}, 201

def login_user(data):
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username, password=password).first()

    if not user:
        return {"error": "Credenciales inválidas"}, 401

    print("Credenciales validas")
    return {"message": "Inicio de sesión exitoso", "user": user.to_dict()}, 200
