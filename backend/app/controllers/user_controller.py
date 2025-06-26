# app/controllers/user_controller.py
from app.models.user_model import User
from app.models import db
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash


def register_user(data):
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"error": "Faltan campos"}, 400

    if User.query.filter_by(username=username).first():
        return {"error": "El usuario ya existe"}, 409
    
    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return {"message": "Usuario registrado"}, 201

def login_user(data):
    print("Iniciando sesión")
    print(data)
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return {"error": "Credenciales inválidas"}, 401

    print("Credenciales válidas")
    return {"message": "Inicio de sesión exitoso", "user": user.to_dict()}, 200

