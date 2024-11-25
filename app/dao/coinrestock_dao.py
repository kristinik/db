from .general_dao import GeneralDAO
from ..domain import CoinRestock

class CoinRestockDAO(GeneralDAO):
    _domain_type = CoinRestock
