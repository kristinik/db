from .general_controller import GeneralController
from ..service import menu_service


class MenuController(GeneralController):
    _service = menu_service
