# feedback_dao.py
from .general_dao import GeneralDAO
from ..domain import Feedback  # Імпортуємо модель Feedback

class FeedbackDAO(GeneralDAO):
    _domain_type = Feedback
