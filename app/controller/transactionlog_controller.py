from .general_controller import GeneralController
from ..service import transaction_log_service


class TransactionLogController(GeneralController):
    _service = transaction_log_service
