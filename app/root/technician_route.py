from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import technician_controller
from ..domain.technician import Technician

from sqlalchemy.exc import OperationalError

technician_bp = Blueprint('technician', __name__, url_prefix='/technician')


@technician_bp.route('', methods=['GET'])
def get_all_technicians() -> Response:
    return make_response(jsonify(technician_controller.find_all()), HTTPStatus.OK)





@technician_bp.route('/<int:technician_id>', methods=['GET'])
def get_technician(technician_id: int) -> Response:
    return make_response(jsonify(technician_controller.find_by_id(technician_id)), HTTPStatus.OK)




@technician_bp.route('/<int:technician_id>', methods=['DELETE'])
def delete_technician(technician_id: int) -> Response:
    technician_controller.delete(technician_id)
    return make_response("Technician deleted", HTTPStatus.OK)




from app.insert import inserts
@technician_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return inserts(Technician, request.get_json())



@technician_bp.route('', methods=['POST'])
def create_technician() -> Response:
    try:
        # Отримання даних із запиту
        content = request.get_json()
        technician = Technician.create_from_dto(content)

        # Спроба створити запис
        technician_controller.create(technician)

        # Успішний результат
        return make_response(jsonify(technician.put_into_dto()), HTTPStatus.CREATED)

    except OperationalError as e:
        # Перевіряємо, чи це помилка SQLSTATE '45000'
        error_message = str(e.orig)
        if "SQLSTATE '45000'" in error_message:
            return make_response(
                jsonify({"error": "Name is not allowed. Allowed names: Svitlana, Petro, Olha, Taras."}),
                HTTPStatus.BAD_REQUEST
            )
        # Загальна обробка OperationalError
        return make_response(
            jsonify({"error": "Database error", "details": error_message}),
            HTTPStatus.INTERNAL_SERVER_ERROR
        )

    except Exception as e:
        # Інші помилки
        return make_response(
            jsonify({"error": "Unexpected error", "details": str(e)}),
            HTTPStatus.INTERNAL_SERVER_ERROR
        )


@technician_bp.route('/<int:technician_id>', methods=['PUT'])
def update_technician(technician_id: int) -> Response:
    try:
        # Отримання даних із запиту
        content = request.get_json()
        technician = Technician.create_from_dto(content)

        # Спроба оновити запис
        technician_controller.update(technician_id, technician)

        # Успішний результат
        return make_response("Technician updated", HTTPStatus.OK)

    except OperationalError as e:
        # Перевіряємо, чи це помилка SQLSTATE '45000'
        error_message = str(e.orig)
        if "SQLSTATE '45000'" in error_message:
            return make_response(
                jsonify({"error": "Name is not allowed. Allowed names: Svitlana, Petro, Olha, Taras."}),
                HTTPStatus.BAD_REQUEST
            )
        # Загальна обробка OperationalError
        return make_response(
            jsonify({"error": "Database error", "details": error_message}),
            HTTPStatus.INTERNAL_SERVER_ERROR
        )

    except Exception as e:
        # Інші помилки
        return make_response(
            jsonify({"error": "Unexpected error", "details": str(e)}),
            HTTPStatus.INTERNAL_SERVER_ERROR
        )
