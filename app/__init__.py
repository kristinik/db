import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    from app.config import Config
    app.config.from_object(Config)

    db.init_app(app)

    from app.root import register_routes
    register_routes(app)

    with app.app_context():
        db.create_all()

    return app
