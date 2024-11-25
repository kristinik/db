from .general_controller import GeneralController
from ..service import stock_service


class StockController(GeneralController):
    _service = stock_service
