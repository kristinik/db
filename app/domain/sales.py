from __future__ import annotations
from typing import Dict, Any
from app import db

class Sales(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity_sold = db.Column(db.Integer, nullable=False)
    sale_date = db.Column(db.Date, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    vendingmachine_id = db.Column(db.Integer, db.ForeignKey('vendingmachine.id'), nullable=False)

    product = db.relationship("Product", backref="sales")
    vendingmachine = db.relationship("VendingMachine", backref="sales")

    def __repr__(self) -> str:
        return f"Sales(id={self.id}, quantity_sold={self.quantity_sold}, sale_date='{self.sale_date}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'quantity_sold': self.quantity_sold,
            'sale_date': self.sale_date,
            'product_id': self.product_id,
            'vendingmachine_id': self.vendingmachine_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Sales:
        return Sales(
            quantity_sold=dto_dict.get('quantity_sold'),
            sale_date=dto_dict.get('sale_date'),
            product_id=dto_dict.get('product_id'),
            vendingmachine_id=dto_dict.get('vendingmachine_id'),
        )

