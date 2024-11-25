from .general_dao import GeneralDAO
from ..domain import CoinCollection

class CoinCollectionDAO(GeneralDAO):
    _domain_type = CoinCollection
