from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import product_controller
from ..domain.product import Product, create_dynamic_tables_from_products

product_bp = Blueprint('product', __name__, url_prefix='/product')

@product_bp.route('', methods=['GET'])
def get_all_products() -> Response:
    return make_response(jsonify(product_controller.find_all()), HTTPStatus.OK)

@product_bp.route('', methods=['POST'])
def create_product() -> Response:
    content = request.get_json()
    product = Product.create_from_dto(content)
    product_controller.create(product)
    return make_response(jsonify(product.put_into_dto()), HTTPStatus.CREATED)

@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id: int) -> Response:
    return make_response(jsonify(product_controller.find_by_id(product_id)), HTTPStatus.OK)

@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id: int) -> Response:
    content = request.get_json()
    product = Product.create_from_dto(content)
    product_controller.update(product_id, product)
    return make_response("Product updated", HTTPStatus.OK)

@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int) -> Response:
    product_controller.delete(product_id)
    return make_response("Product deleted", HTTPStatus.OK)

@product_bp.route('/create_dynamic_tables', methods=['POST'])
def create_tables_endpoint():
    table_names = create_dynamic_tables_from_products()
    if isinstance(table_names, str):
        return jsonify({"error": table_names}), 404
    return jsonify({"message": f"Tables {', '.join(table_names)} created successfully!"}), 201

from app.insert import inserts
@product_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return inserts(Product, request.get_json())
