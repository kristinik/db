from __future__ import annotations
from typing import Dict, Any
from app import db

class VendingMachine(db.Model):
    __tablename__ = 'vendingmachine'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(255), nullable=False)
    gps_coordinates = db.Column(db.String(50), nullable=False, unique=True)
    last_restock_date = db.Column(db.Date, nullable=False)
    technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'), nullable=False)

    # Зв'язок багато до багатьох через таблицю Menu
    products = db.relationship("Product", secondary="menu", back_populates="vending_machines", overlaps="product")

    def __repr__(self) -> str:
        return f"VendingMachine(id={self.id}, address='{self.address}', gps_coordinates='{self.gps_coordinates}')"

    def put_into_dto(self) -> Dict[str, Any]:
        # Вивести дані про автомат і його продукти без дублювання
        return {
            'id': self.id,
            'address': self.address,
            'gps_coordinates': self.gps_coordinates,
            'last_restock_date': self.last_restock_date,
            'technician_id': self.technician_id,
            'products': [
                {
                    'id': product.id,
                    'name': product.name,
                    'price': str(product.price)
                }
                for product in self.products
            ]
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> VendingMachine:
        return VendingMachine(
            address=dto_dict.get('address'),
            gps_coordinates=dto_dict.get('gps_coordinates'),
            last_restock_date=dto_dict.get('last_restock_date'),
            technician_id=dto_dict.get('technician_id'),
        )
