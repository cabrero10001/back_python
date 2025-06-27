from app.models import db
from app.models.user_model import DiagnosticoODS
from flask import jsonify
from datetime import datetime, timezone

def guardar_diagnostico(data):
    user_id = data.get("user_id")
    resultado = data.get("resultado")

    if not user_id or not resultado:
        return {"error": "faltan datos"}, 400

    try:
        nuevo_Diagnostico = DiagnosticoODS (
            resultado = resultado,
            fecha=datetime.now(timezone.utc),
            user_id=user_id
        )

        db.session.add(nuevo_Diagnostico)
        db.session.commit()

        return {"message": "Diagnostico almacenado en db"}, 201
    
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500