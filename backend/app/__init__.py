from flask import Flask
from flask_cors import CORS
from .models import db
from .config import Config
from .routes import init_routes
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 👉 Habilitar CORS
    CORS(app)

    db.init_app(app)
    Migrate(app, db)

    init_routes(app)

    return app
