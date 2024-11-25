from .general_controller import GeneralController
from ..service import coin_restock_service


class CoinRestockController(GeneralController):
    _service = coin_restock_service
