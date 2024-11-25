from .general_service import GeneralService
from ..dao import vending_machine_dao

class VendingMachineService(GeneralService):
    _dao = vending_machine_dao
