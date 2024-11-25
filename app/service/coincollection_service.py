from .general_service import GeneralService
from ..dao import coin_collection_dao

class CoinCollectionService(GeneralService):
    _dao = coin_collection_dao
