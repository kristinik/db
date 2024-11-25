from .general_service import GeneralService
from ..dao import feedback_dao  # Імпортуємо DAO для відгуків

class FeedbackService(GeneralService):
    _dao = feedback_dao  # Встановлюємо DAO для роботи з відгуками
