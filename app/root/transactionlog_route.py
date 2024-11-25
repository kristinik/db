from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import transaction_log_controller
from ..domain.transactionlog import TransactionLog

transactionlog_bp = Blueprint('transactionlog', __name__, url_prefix='/transactionlog')

@transactionlog_bp.route('', methods=['GET'])
def get_all_transactionlogs() -> Response:
    return make_response(jsonify(transaction_log_controller.find_all()), HTTPStatus.OK)

@transactionlog_bp.route('', methods=['POST'])
def create_transactionlog() -> Response:
    content = request.get_json()
    transactionlog = TransactionLog.create_from_dto(content)
    transaction_log_controller.create(transactionlog)
    return make_response(jsonify(transactionlog.put_into_dto()), HTTPStatus.CREATED)

@transactionlog_bp.route('/<int:log_id>', methods=['GET'])
def get_transactionlog(log_id: int) -> Response:
    return make_response(jsonify(transaction_log_controller.find_by_id(log_id)), HTTPStatus.OK)

@transactionlog_bp.route('/<int:log_id>', methods=['PUT'])
def update_transactionlog(log_id: int) -> Response:
    content = request.get_json()
    transactionlog = TransactionLog.create_from_dto(content)
    transaction_log_controller.update(log_id, transactionlog)
    return make_response("Transaction log updated", HTTPStatus.OK)

@transactionlog_bp.route('/<int:log_id>', methods=['DELETE'])
def delete_transactionlog(log_id: int) -> Response:
    transaction_log_controller.delete(log_id)
    return make_response("Transaction log deleted", HTTPStatus.OK)

from app.insert import inserts
@transactionlog_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return inserts(TransactionLog, request.get_json())

