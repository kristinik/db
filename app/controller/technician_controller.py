from .general_controller import GeneralController
from ..service import technician_service


class TechnicianController(GeneralController):
    _service = technician_service
