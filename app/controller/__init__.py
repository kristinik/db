from .brand_controller import BrandController
from .technician_controller import TechnicianController
from .vendingmachine_controller import VendingMachineController
from .coincollection_controller import CoinCollectionController
from .coinrestock_controller import CoinRestockController
from .product_controller import ProductController
from .menu_controller import MenuController
from .sales_controller import SalesController
from .stock_controller import StockController
from .transactionlog_controller import TransactionLogController
from .feedback_controller import FeedbackController  # Імпортуємо контролер для відгуків

# Ініціалізація контролерів
brand_controller = BrandController()
technician_controller = TechnicianController()
vending_machine_controller = VendingMachineController()
coin_collection_controller = CoinCollectionController()
coin_restock_controller = CoinRestockController()
product_controller = ProductController()
menu_controller = MenuController()
sales_controller = SalesController()
stock_controller = StockController()
transaction_log_controller = TransactionLogController()
feedback_controller = FeedbackController()  # Ініціалізуємо контролер для відгуків
