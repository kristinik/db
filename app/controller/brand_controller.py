from .general_controller import GeneralController
from ..service.brand_service import BrandService

brand_service = BrandService()
class BrandController(GeneralController):
    _service = brand_service
