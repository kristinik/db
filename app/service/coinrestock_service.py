from .general_service import GeneralService
from ..dao import coin_restock_dao

class CoinRestockService(GeneralService):
    _dao = coin_restock_dao
