from .general_service import GeneralService
from ..dao import menu_dao

class MenuService(GeneralService):
    _dao = menu_dao
