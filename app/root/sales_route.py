from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import sales_controller
from ..domain.sales import Sales

sales_bp = Blueprint('sales', __name__, url_prefix='/sales')

@sales_bp.route('', methods=['GET'])
def get_all_sales() -> Response:
    return make_response(jsonify(sales_controller.find_all()), HTTPStatus.OK)

@sales_bp.route('', methods=['POST'])
def create_sales() -> Response:
    content = request.get_json()
    sales = Sales.create_from_dto(content)
    sales_controller.create(sales)
    return make_response(jsonify(sales.put_into_dto()), HTTPStatus.CREATED)

@sales_bp.route('/<int:sale_id>', methods=['GET'])
def get_sale(sale_id: int) -> Response:
    return make_response(jsonify(sales_controller.find_by_id(sale_id)), HTTPStatus.OK)

@sales_bp.route('/<int:sale_id>', methods=['PUT'])
def update_sale(sale_id: int) -> Response:
    content = request.get_json()
    sales = Sales.create_from_dto(content)
    sales_controller.update(sale_id, sales)
    return make_response("Sale updated", HTTPStatus.OK)


from app.insert import inserts
@sales_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return inserts(Sales, request.get_json())


from sqlalchemy.exc import OperationalError
from app import db

@sales_bp.route('/sales/cr', methods=['POST'])
def create_sale():
    try:
        # Отримання даних із запиту
        data = request.get_json()

        # Створення нового продажу
        new_sale = Sales(
            quantity_sold=data['quantity_sold'],
            sale_date=data['sale_date'],
            product_id=data['product_id'],
            vendingmachine_id=data['vendingmachine_id']
        )

        # Додавання до сесії
        db.session.add(new_sale)
        db.session.commit()

        return make_response(
            jsonify({"message": "Sale created successfully", "sale": new_sale.put_into_dto()}),
            201
        )

    except OperationalError as e:
        # Перевіряємо текст помилки на SQLSTATE '45000'
        if "SQLSTATE '45000'" in str(e.orig):
            return make_response(
                jsonify({"error": str(e.orig)}), 400
            )
        else:
            return make_response(
                jsonify({"error": "Value of quantity_sold cannot end with two zeros"}), 500
            )

    except Exception as e:
        # Загальний обробник для інших помилок
        return make_response(
            jsonify({"error": str(e)}), 500
        )


@sales_bp.route('/<int:sale_id>', methods=['DELETE'])
def delete_sale(sale_id: int) -> Response:
    try:
        # Виклик контролера для видалення
        sales_controller.delete(sale_id)
        return make_response("Sale deleted", HTTPStatus.OK)

    except OperationalError as e:
        error_message = str(e.orig)
        print(f"OperationalError caught: {error_message}")  # Логування помилки для відладки

        # Перевіряємо, чи викликано SIGNAL SQLSTATE '45000'
        if "SQLSTATE '45000'" in error_message:
            return make_response(
                jsonify({"error": "Deletion of rows from the sales table is not allowed."}),
                HTTPStatus.BAD_REQUEST
            )

        # Інші помилки бази даних
        return make_response(
            jsonify({"error": "Database error", "details": error_message}),
            HTTPStatus.INTERNAL_SERVER_ERROR
        )

    except Exception as e:
        # Загальна обробка інших винятків
        error_details = str(e)
        print(f"Unexpected error: {error_details}")  # Логування загальних помилок
        return make_response(
            jsonify({"error": "Unexpected error", "details": error_details}),
            HTTPStatus.INTERNAL_SERVER_ERROR
        )

