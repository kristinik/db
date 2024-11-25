from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import coin_restock_controller
from ..domain.coinrestock import CoinRestock

coinrestock_bp = Blueprint('coinrestock', __name__, url_prefix='/coinrestock')

@coinrestock_bp.route('', methods=['GET'])
def get_all_coinrestocks() -> Response:
    return make_response(jsonify(coin_restock_controller.find_all()), HTTPStatus.OK)

@coinrestock_bp.route('', methods=['POST'])
def create_coinrestock() -> Response:
    content = request.get_json()
    coinrestock = CoinRestock.create_from_dto(content)
    coin_restock_controller.create(coinrestock)
    return make_response(jsonify(coinrestock.put_into_dto()), HTTPStatus.CREATED)

@coinrestock_bp.route('/<int:restock_id>', methods=['GET'])
def get_coinrestock(restock_id: int) -> Response:
    return make_response(jsonify(coin_restock_controller.find_by_id(restock_id)), HTTPStatus.OK)

@coinrestock_bp.route('/<int:restock_id>', methods=['PUT'])
def update_coinrestock(restock_id: int) -> Response:
    content = request.get_json()
    coinrestock = CoinRestock.create_from_dto(content)
    coin_restock_controller.update(restock_id, coinrestock)
    return make_response("Coin restock updated", HTTPStatus.OK)

@coinrestock_bp.route('/<int:restock_id>', methods=['DELETE'])
def delete_coinrestock(restock_id: int) -> Response:
    coin_restock_controller.delete(restock_id)
    return make_response("Coin restock deleted", HTTPStatus.OK)

from app.insert import inserts
@coinrestock_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return inserts(CoinRestock, request.get_json())
