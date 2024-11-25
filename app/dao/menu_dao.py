from .general_dao import GeneralDAO
from ..domain import Menu

class MenuDAO(GeneralDAO):
    _domain_type = Menu
