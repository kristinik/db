from .general_dao import GeneralDAO
from ..domain import VendingMachine

class VendingMachineDAO(GeneralDAO):
    _domain_type = VendingMachine
