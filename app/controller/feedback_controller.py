# feedback_controller.py
from .general_controller import GeneralController
from ..service import feedback_service

class FeedbackController(GeneralController):
    _service = feedback_service
