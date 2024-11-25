from .general_dao import GeneralDAO
from ..domain import Sales

class SalesDAO(GeneralDAO):
    _domain_type = Sales
