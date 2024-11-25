from .general_dao import GeneralDAO
from ..domain import Stock

class StockDAO(GeneralDAO):
    _domain_type = Stock
