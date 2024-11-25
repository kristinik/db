from __future__ import annotations
from typing import Dict, Any
from app import db
from random import randint, choice
from time import time
from sqlalchemy import text

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)

    # Зв'язок багато до багатьох через таблицю Menu
    vending_machines = db.relationship("VendingMachine", secondary="menu", back_populates="products", overlaps="vending_machine")

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'price': str(self.price),
            'brand_id': self.brand_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Product:
        return Product(
            name=dto_dict.get('name'),
            price=dto_dict.get('price'),
            brand_id=dto_dict.get('brand_id'),
        )


def create_dynamic_tables_from_products():
    products = Product.query.all()
    if not products:
        return "No products found in the database."

    table_count = randint(1, 9)
    created_tables = []

    for product in products[:table_count]:
        product_name = product.name.replace(" ", "_")
        table_name = f"{product_name}_{int(time())}"

        table_name_escaped = f"`{table_name}`"

        column_defs = []
        for i in range(randint(1, 9)):
            column_name = f"column_{i + 1}"
            column_type = choice(["INT", "VARCHAR(255)", "DATE"])
            column_defs.append(f"{column_name} {column_type}")
        column_defs_str = ", ".join(column_defs)

        create_table_sql = text(f"CREATE TABLE {table_name_escaped} (id INT PRIMARY KEY AUTO_INCREMENT, {column_defs_str});")

        db.session.execute(create_table_sql)
        db.session.commit()
        created_tables.append(table_name)

    return created_tables
