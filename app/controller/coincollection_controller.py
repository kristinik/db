from .general_controller import GeneralController
from ..service import coin_collection_service


class CoinCollectionController(GeneralController):
    _service = coin_collection_service
