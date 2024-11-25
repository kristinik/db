from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import menu_controller
from ..domain.menu import Menu, insert_product_to_vending_machine


menu_bp = Blueprint('menu', __name__, url_prefix='/menu')

@menu_bp.route('', methods=['GET'])
def get_all_menus() -> Response:
    print("get_all_menus called")  # Додайте цю строку
    return make_response(jsonify(menu_controller.find_all()), HTTPStatus.OK)

@menu_bp.route('', methods=['POST'])
def create_menu() -> Response:
    content = request.get_json()
    menu = Menu.create_from_dto(content)
    menu_controller.create(menu)
    return make_response(jsonify(menu.put_into_dto()), HTTPStatus.CREATED)

@menu_bp.route('/<int:menu_id>', methods=['GET'])
def get_menu(menu_id: int) -> Response:
    return make_response(jsonify(menu_controller.find_by_id(menu_id)), HTTPStatus.OK)

@menu_bp.route('/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id: int) -> Response:
    content = request.get_json()
    menu = Menu.create_from_dto(content)
    menu_controller.update(menu_id, menu)
    return make_response("Menu updated", HTTPStatus.OK)


@menu_bp.route('/<int:menu_id>', methods=['DELETE'])
def delete_menu(menu_id: int) -> Response:
    # Спробуємо знайти меню за вказаним ID
    menu = menu_controller.find_by_id(menu_id)
    if not menu:
        return make_response("Menu not found", HTTPStatus.NOT_FOUND)

    # Якщо меню знайдено, видаляємо його
    menu_controller.delete(menu_id)
    return make_response("Menu deleted", HTTPStatus.OK)


@menu_bp.route('/menu/add_product_to_machine', methods=['POST'])
def add_product_to_machine() -> Response:
    content = request.get_json()

    try:
        ids = insert_product_to_vending_machine(
            product_name=content['product_name'],
            vendingmachine_address=content['vendingmachine_address'],
            availability=content['availability']
        )
        return make_response(jsonify(ids), HTTPStatus.CREATED)
    except ValueError as e:
        return make_response(str(e), HTTPStatus.BAD_REQUEST)


from app.insert import inserts
@menu_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return inserts(Menu, request.get_json())
