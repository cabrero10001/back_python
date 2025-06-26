from app.models.user_model import User
from app.models import db
from werkzeug.security import generate_password_hash

# Obtener todos los usuarios
def get_all_user():
    users = User.query.all()
    return [u.to_dict() for u in users]

# Crear un nuevo usuario
def create_user(data):
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return {"error": "Faltan campos"}, 400

    if User.query.filter_by(username=username).first():
        return {"error": "El usuario ya existe"}, 409

    # Encriptar la contraseña antes de guardarla
    hashed_password = generate_password_hash(password)

    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return {"message": "Usuario creado correctamente"}, 201
