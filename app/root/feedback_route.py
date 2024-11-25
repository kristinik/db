from flask import Blueprint, jsonify, request, make_response
from ..controller import feedback_controller
from ..domain.feedback import Feedback, insert_into_feedback  # Імпортуємо модель Feedback
from http import HTTPStatus
from flask import Response  # Імпортуємо Response

feedback_bp = Blueprint('feedback', __name__, url_prefix='/feedback')


@feedback_bp.route('', methods=['GET'])
def get_all_feedbacks() -> Response:
    # Отримуємо всі відгуки через контролер
    return make_response(jsonify(feedback_controller.find_all()), HTTPStatus.OK)


@feedback_bp.route('', methods=['POST'])
def create_feedback() -> Response:
    content = request.get_json()
    # Створюємо новий відгук з DTO
    feedback = Feedback.create_from_dto(content)
    feedback_controller.create(feedback)
    # Повертаємо створений відгук
    return make_response(jsonify(feedback.put_into_dto()), HTTPStatus.CREATED)


@feedback_bp.route('/<int:feedback_id>', methods=['GET'])
def get_feedback(feedback_id: int) -> Response:
    # Повертаємо відгук за заданим ID
    return make_response(jsonify(feedback_controller.find_by_id(feedback_id)), HTTPStatus.OK)


@feedback_bp.route('/<int:feedback_id>', methods=['PUT'])
def update_feedback(feedback_id: int) -> Response:
    content = request.get_json()
    # Перевіряємо, чи існує відгук для оновлення
    existing_feedback = feedback_controller.find_by_id(feedback_id)
    if not existing_feedback:
        return make_response("Feedback not found", HTTPStatus.NOT_FOUND)

    # Створюємо оновлений об'єкт Feedback
    feedback = Feedback.create_from_dto(content)
    feedback_controller.update(feedback_id, feedback)
    return make_response("Feedback updated", HTTPStatus.OK)


@feedback_bp.route('/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id: int) -> Response:
    # Перевіряємо, чи існує відгук для видалення
    existing_feedback = feedback_controller.find_by_id(feedback_id)
    if not existing_feedback:
        return make_response("Feedback not found", HTTPStatus.NOT_FOUND)

    # Видаляємо відгук
    feedback_controller.delete(feedback_id)
    return make_response("Feedback deleted", HTTPStatus.OK)


from app.insert import inserts
@feedback_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return inserts(Feedback, request.get_json())



@feedback_bp.errorhandler(ValueError)
def handle_value_error(error):
    """
    Глобальна обробка помилок ValueError для Blueprint 'feedback'.
    """
    response = {
        "error": "Bad Request",
        "message": str(error)  # Повертаємо текст помилки
    }
    return jsonify(response), HTTPStatus.BAD_REQUEST
