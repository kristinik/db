from .general_dao import GeneralDAO
from ..domain import Technician

class TechnicianDAO(GeneralDAO):
    _domain_type = Technician
