from .general_service import GeneralService
from ..dao import transaction_log_dao

class TransactionLogService(GeneralService):
    _dao = transaction_log_dao
