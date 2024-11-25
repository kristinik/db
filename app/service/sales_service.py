from .general_service import GeneralService
from ..dao import sales_dao

class SalesService(GeneralService):
    _dao = sales_dao
