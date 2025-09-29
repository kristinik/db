from flask import Blueprint, jsonify, request, current_app
from flask_swagger_ui import get_swaggerui_blueprint

swagger_bp = Blueprint("swagger_bp", __name__)

SWAGGER_URL = "/swagger"
API_URL = "/swagger.json"

swagger_ui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Coin Collection API"}
)

EXCLUDE_ENDPOINTS = {
    "static",
    "swagger_bp.swagger_json",
}

EXCLUDE_RULE_PREFIXES = {
    "/swagger",   
    "/docs",      
}

METHODS_ALLOWED = {"GET", "POST", "PUT", "PATCH", "DELETE"}

def _should_exclude(rule):
    if rule.endpoint in EXCLUDE_ENDPOINTS:
        return True
    for pref in EXCLUDE_RULE_PREFIXES:
        if str(rule.rule).startswith(pref):
            return True
    methods = METHODS_ALLOWED.intersection(rule.methods or set())
    return len(methods) == 0

def _path_item_for_methods(methods):
    """Мінімальна заглушка для кожного HTTP-методу."""
    obj = {}
    for m in sorted(methods):
        obj[m.lower()] = {
            "summary": f"{m} {''}",
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
    return obj

@swagger_bp.route("/swagger.json")
def swagger_json():

    host = request.host
    scheme = request.scheme if request.scheme in ("http", "https") else "http"

    paths = {}
    for rule in current_app.url_map.iter_rules():
        if _should_exclude(rule):
            continue
        path = str(rule.rule)
        methods = METHODS_ALLOWED.intersection(rule.methods or set())
        if not methods:
            continue

        swagger_path = path.replace("<", "{").replace(">", "}")
        paths.setdefault(swagger_path, {}).update(_path_item_for_methods(methods))

    spec = {
        "swagger": "2.0",
        "info": {
            "title": "Coin Collection API (auto-generated)",
            "version": "1.0.0",
            "description": " Flask url_map. "
                           "
        },
        "host": host,
        "basePath": "/",
        "schemes": [scheme],
        "paths": paths,
    }
    return jsonify(spec)
