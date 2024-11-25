from .general_service import GeneralService
from ..dao import brand_dao

class BrandService(GeneralService):
    _dao = brand_dao
