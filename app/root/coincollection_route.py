from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import coin_collection_controller
from ..domain.coincollection import CoinCollection, get_through_collection_stat

coincollection_bp = Blueprint('coincollection', __name__, url_prefix='/coincollection')

@coincollection_bp.route('', methods=['GET'])
def get_all_coincollections() -> Response:
    return make_response(jsonify(coin_collection_controller.find_all()), HTTPStatus.OK)


@coincollection_bp.route('capacity', methods=['GET'])
def get_coincollection_statistics() -> tuple:
    # Отримуємо параметр 'stat_type' з запиту
    stat_type = request.args.get('stat_type').upper()

    # Викликаємо функцію для обчислення статистики
    result = get_through_collection_stat(stat_type)

    # Якщо результат не є -1, то повертаємо статистику
    if result != -1:
        return jsonify({stat_type: result})
    else:
        # Якщо передано неправильний тип статистики, повертаємо помилку
        return jsonify({"error": "Invalid stat_type. Use MAX, MIN, SUM, or AVG"}), 400


@coincollection_bp.route('', methods=['POST'])
def create_coincollection() -> Response:
    content = request.get_json()
    coincollection = CoinCollection.create_from_dto(content)
    coin_collection_controller.create(coincollection)
    return make_response(jsonify(coincollection.put_into_dto()), HTTPStatus.CREATED)

@coincollection_bp.route('/<int:collection_id>', methods=['GET'])
def get_coincollection(collection_id: int) -> Response:
    return make_response(jsonify(coin_collection_controller.find_by_id(collection_id)), HTTPStatus.OK)

@coincollection_bp.route('/<int:collection_id>', methods=['PUT'])
def update_coincollection(collection_id: int) -> Response:
    content = request.get_json()
    coincollection = CoinCollection.create_from_dto(content)
    coin_collection_controller.update(collection_id, coincollection)
    return make_response("Coin collection updated", HTTPStatus.OK)

@coincollection_bp.route('/<int:collection_id>', methods=['DELETE'])
def delete_coincollection(collection_id: int) -> Response:
    coin_collection_controller.delete(collection_id)
    return make_response("Coin collection deleted", HTTPStatus.OK)


from app.insert import inserts
@coincollection_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return inserts(CoinCollection, request.get_json())
