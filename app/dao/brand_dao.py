from .general_dao import GeneralDAO
from ..domain.brand import Brand

class BrandDAO(GeneralDAO):
    _domain_type = Brand
