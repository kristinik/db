from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller import brand_controller
from ..domain.brand import Brand
from app.domain.brand import insert_noname_brands
from app.insert import inserts

brand_bp = Blueprint('brand', __name__, url_prefix='/brand')


@brand_bp.route('', methods=['GET'])
def get_all_brands():
    print("Function get_all_brands called")  # Лог для перевірки
    brands = brand_controller.find_all()
    print("Retrieved brands:", brands)  # Лог результату
    return make_response(jsonify(brand_controller.find_all()), HTTPStatus.OK)


@brand_bp.route('', methods=['POST'])
def create_brand() -> Response:
    content = request.get_json()
    brand = Brand.create_from_dto(content)
    brand_controller.create(brand)
    return make_response(jsonify(brand.put_into_dto()), HTTPStatus.CREATED)


@brand_bp.route('/<int:brand_id>', methods=['GET'])
def get_brand(brand_id: int) -> Response:
    return make_response(jsonify(brand_controller.find_by_id(brand_id)), HTTPStatus.OK)


@brand_bp.route('/<int:brand_id>', methods=['PUT'])
def update_brand(brand_id: int) -> Response:
    content = request.get_json()
    brand = Brand.create_from_dto(content)
    brand_controller.update(brand_id, brand)
    return make_response("Brand updated", HTTPStatus.OK)


@brand_bp.route('/<int:brand_id>', methods=['DELETE'])
def delete_brand(brand_id: int) -> Response:
    brand_controller.delete(brand_id)
    return make_response("Brand deleted", HTTPStatus.OK)


# Роут для вставки 10 записів
@brand_bp.route('/brand/insert_nonames', methods=['POST'])
def insert_noname_brands_route():
    try:
        insert_noname_brands()
        return make_response(jsonify({"message": "10 Noname brands have been added successfully!"}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)


@brand_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return inserts(Brand, request.get_json())
