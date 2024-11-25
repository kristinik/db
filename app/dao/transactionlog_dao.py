from .general_dao import GeneralDAO
from ..domain import TransactionLog

class TransactionLogDAO(GeneralDAO):
    _domain_type = TransactionLog
