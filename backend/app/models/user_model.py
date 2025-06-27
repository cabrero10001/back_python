from . import db
from sqlalchemy.dialects.mysql import JSON
from datetime import datetime

class User(db.Model):
    __tablename__="user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    diagnosticos = db.relationship("DiagnosticoODS", back_populates="user", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password
        }

    def __repr__(self):
        return f'<User {self.username}>'

class DiagnosticoODS(db.Model):
    __tablename__ = "diagnostico_ods"

    id = db.Column(db.Integer, primary_key=True)
    resultado = db.Column(JSON, nullable=False)  
    fecha = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="diagnosticos")

    def to_dict(self):
        return {
            "id": self.id,
            "resultado": self.resultado,
            "fecha": self.fecha.isoformat(),
            "user_id": self.user_id
        }

    def __repr__(self):
        return f"<DiagnosticoODS de User {self.user_id} en {self.fecha}>"