from __future__ import annotations
from typing import Dict, Any
from app import db

class Stock(db.Model):
    __tablename__ = 'stock'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('vendingmachine.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    vendingmachine = db.relationship("VendingMachine", backref="stocks")

    def __repr__(self) -> str:
        return f"Stock(id={self.id}, machine_id={self.machine_id}, quantity={self.quantity})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'machine_id': self.machine_id,
            'quantity': self.quantity,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Stock:
        return Stock(
            machine_id=dto_dict.get('machine_id'),
            quantity=dto_dict.get('quantity'),
        )

