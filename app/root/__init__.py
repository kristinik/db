from flask import Flask

from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    # Реєстрація обробника помилок
    app.register_blueprint(err_handler_bp)
    # Імпортуємо ваші Blueprints

    from .brand_route import brand_bp
    from .coincollection_route import coincollection_bp
    from .coinrestock_route import coinrestock_bp
    from .menu_route import menu_bp
    from .product_route import product_bp
    from .sales_route import sales_bp
    from .stock_route import stock_bp
    from .technician_route import technician_bp
    from .transactionlog_route import transactionlog_bp
    from .vendingmachine_route import vendingmachine_bp
    from .feedback_route import feedback_bp  # Імпортуємо feedback_bp

    from .docs_route import docs_bp
    app.register_blueprint(docs_bp)
    
    # Реєстрація всіх ваших Blueprints
    app.register_blueprint(brand_bp)
    app.register_blueprint(coincollection_bp)
    app.register_blueprint(coinrestock_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(sales_bp)
    app.register_blueprint(stock_bp)
    app.register_blueprint(technician_bp)
    app.register_blueprint(transactionlog_bp)
    app.register_blueprint(vendingmachine_bp)
    app.register_blueprint(feedback_bp)  # Реєстрація feedback_bp
