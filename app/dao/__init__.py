from .brand_dao import BrandDAO
from .technician_dao import TechnicianDAO
from .vendingmachine_dao import VendingMachineDAO
from .coincollection_dao import CoinCollectionDAO
from .coinrestock_dao import CoinRestockDAO
from .product_dao import ProductDAO
from .menu_dao import MenuDAO
from .sales_dao import SalesDAO
from .stock_dao import StockDAO
from .transactionlog_dao import TransactionLogDAO
from .feedback_dao import FeedbackDAO  # Імпортуємо FeedbackDAO

# Ініціалізація DAO
brand_dao = BrandDAO()
technician_dao = TechnicianDAO()
vending_machine_dao = VendingMachineDAO()
coin_collection_dao = CoinCollectionDAO()
coin_restock_dao = CoinRestockDAO()
product_dao = ProductDAO()
menu_dao = MenuDAO()
sales_dao = SalesDAO()
stock_dao = StockDAO()
transaction_log_dao = TransactionLogDAO()
feedback_dao = FeedbackDAO()  # Ініціалізація DAO для feedback
