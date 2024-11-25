from .general_controller import GeneralController
from ..service import sales_service


class SalesController(GeneralController):
    _service = sales_service
