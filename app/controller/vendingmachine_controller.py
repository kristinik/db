from .general_controller import GeneralController
from ..service import vending_machine_service


class VendingMachineController(GeneralController):
    _service = vending_machine_service
