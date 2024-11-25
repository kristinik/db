from .general_service import GeneralService
from ..dao import technician_dao

class TechnicianService(GeneralService):
    _dao = technician_dao
