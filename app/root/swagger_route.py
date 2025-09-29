from flask import Blueprint, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os

swagger_bp = Blueprint("swagger_bp", __name__)

SWAGGER_URL = "/swagger"
API_URL = "/swagger.json"

swagger_ui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Coin Collection API"
    }
)

@swagger_bp.route("/swagger.json")
def swagger_json():
    root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return send_from_directory(root_dir, "swagger.json")
