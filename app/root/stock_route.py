from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import stock_controller
from ..domain.stock import Stock


stock_bp = Blueprint('stock', __name__, url_prefix='/stock')

@stock_bp.route('', methods=['GET'])
def get_all_stocks() -> Response:
    return make_response(jsonify(stock_controller.find_all()), HTTPStatus.OK)

@stock_bp.route('', methods=['POST'])
def create_stock() -> Response:
    content = request.get_json()
    stock = Stock.create_from_dto(content)
    stock_controller.create(stock)
    return make_response(jsonify(stock.put_into_dto()), HTTPStatus.CREATED)

@stock_bp.route('/<int:stock_id>', methods=['GET'])
def get_stock(stock_id: int) -> Response:
    return make_response(jsonify(stock_controller.find_by_id(stock_id)), HTTPStatus.OK)

@stock_bp.route('/<int:stock_id>', methods=['PUT'])
def update_stock(stock_id: int) -> Response:
    content = request.get_json()
    stock = Stock.create_from_dto(content)
    stock_controller.update(stock_id, stock)
    return make_response("Stock updated", HTTPStatus.OK)

@stock_bp.route('/<int:stock_id>', methods=['DELETE'])
def delete_stock(stock_id: int) -> Response:
    stock_controller.delete(stock_id)
    return make_response("Stock deleted", HTTPStatus.OK)


from app.insert import inserts
@stock_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return inserts(Stock, request.get_json())
