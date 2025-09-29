from flask import Blueprint, jsonify, request, current_app, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os

SWAGGER_URL = "/swagger"
API_URL = "/swagger.json"

swagger_bp = Blueprint("swagger_bp", __name__)
swagger_ui_bp = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Coin Collection API"}
)

METHODS_ALLOWED = {"GET", "POST", "PUT", "PATCH", "DELETE"}
EXCLUDE_ENDPOINTS = {"static"}
EXCLUDE_RULE_PREFIXES = {SWAGGER_URL, "/docs"}

def _should_exclude(rule):
    if rule.endpoint in EXCLUDE_ENDPOINTS:
        return True
    path = str(rule.rule)
    for pref in EXCLUDE_RULE_PREFIXES:
        if path.startswith(pref):
            return True
    return not (rule.methods and METHODS_ALLOWED.intersection(rule.methods))

def _autogen_spec():
    host = request.host
    scheme = request.scheme if request.scheme in ("http", "https") else "http"

    paths = {}
    for rule in current_app.url_map.iter_rules():
        if _should_exclude(rule):
            continue
        swagger_path = str(rule.rule).replace("<", "{").replace(">", "}")
        methods = sorted(m.lower() for m in METHODS_ALLOWED.intersection(rule.methods or set()))
        if not methods:
            continue
        paths.setdefault(swagger_path, {})
        for m in methods:
            paths[swagger_path][m] = {
                "summary": f"{m.upper()} {swagger_path}",
                "parameters": [],
                "responses": {
                    "200": {"description": "OK"},
                    "201": {"description": "Created"},
                    "204": {"description": "No Content"},
                    "400": {"description": "Bad Request"},
                    "404": {"description": "Not Found"},
                    "500": {"description": "Server Error"}
                }
            }

    return {
        "swagger": "1.0",
        "info": {"title": "Coin Collection API (auto)", "version": "1.0.0"},
        "host": host,
        "basePath": "/",
        "schemes": [scheme],
        "paths": paths,
    }

@swagger_bp.route("/swagger.json")
def swagger_json():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    static_json = os.path.join(root_dir, "swagger.json")
    if os.path.isfile(static_json):
        return send_from_directory(root_dir, "swagger.json")
    return jsonify(_autogen_spec())
