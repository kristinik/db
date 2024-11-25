from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import vending_machine_controller
from ..domain.vendingmachine import VendingMachine

vendingmachine_bp = Blueprint('vendingmachine', __name__, url_prefix='/vendingmachine')

@vendingmachine_bp.route('', methods=['GET'])
def get_all_vendingmachines() -> Response:
    return make_response(jsonify(vending_machine_controller.find_all()), HTTPStatus.OK)

@vendingmachine_bp.route('', methods=['POST'])
def create_vendingmachine() -> Response:
    content = request.get_json()
    vendingmachine = VendingMachine.create_from_dto(content)
    vending_machine_controller.create(vendingmachine)
    return make_response(jsonify(vendingmachine.put_into_dto()), HTTPStatus.CREATED)

@vendingmachine_bp.route('/<int:machine_id>', methods=['GET'])
def get_vendingmachine(machine_id: int) -> Response:
    return make_response(jsonify(vending_machine_controller.find_by_id(machine_id)), HTTPStatus.OK)

@vendingmachine_bp.route('/<int:machine_id>', methods=['PUT'])
def update_vendingmachine(machine_id: int) -> Response:
    content = request.get_json()
    vendingmachine = VendingMachine.create_from_dto(content)
    vending_machine_controller.update(machine_id, vendingmachine)
    return make_response("Vending machine updated", HTTPStatus.OK)

@vendingmachine_bp.route('/<int:machine_id>', methods=['DELETE'])
def delete_vendingmachine(machine_id: int) -> Response:
    vending_machine_controller.delete(machine_id)
    return make_response("Vending machine deleted", HTTPStatus.OK)


from app.insert import inserts
@vendingmachine_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return inserts(VendingMachine, request.get_json())
