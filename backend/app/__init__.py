from flask import Flask
from .models import db
from .config import Config
from .routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    init_routes(app)

    return app
