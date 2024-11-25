from app.service.brand_service import BrandService
from .technician_service import TechnicianService
from .vendingmachine_service import VendingMachineService
from .coincollection_service import CoinCollectionService
from .coinrestock_service import CoinRestockService
from .product_service import ProductService
from .menu_service import MenuService
from .sales_service import SalesService
from .stock_service import StockService
from .transactionlog_service import TransactionLogService
from .feedback_service import FeedbackService


# Створення екземплярів сервісів
brand_service = BrandService()
technician_service = TechnicianService()
vending_machine_service = VendingMachineService()
coin_collection_service = CoinCollectionService()
coin_restock_service = CoinRestockService()
product_service = ProductService()
menu_service = MenuService()
sales_service = SalesService()
stock_service = StockService()
transaction_log_service = TransactionLogService()
feedback_service = FeedbackService()
