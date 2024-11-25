from .general_service import GeneralService
from ..dao import stock_dao

class StockService(GeneralService):
    _dao = stock_dao
