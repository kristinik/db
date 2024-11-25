from __future__ import annotations
from typing import Dict, Any
from app import db

class CoinRestock(db.Model):
    __tablename__ = 'coinrestock'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restock_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    vendingmachine_id = db.Column(db.Integer, db.ForeignKey('vendingmachine.id'), nullable=False)

    vendingmachine = db.relationship("VendingMachine", backref="coinrestocks")

    def __repr__(self) -> str:
        return f"CoinRestock(id={self.id}, restock_date='{self.restock_date}', amount={self.amount})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'restock_date': self.restock_date,
            'amount': self.amount,
            'vendingmachine_id': self.vendingmachine_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CoinRestock:
        return CoinRestock(
            restock_date=dto_dict.get('restock_date'),
            amount=dto_dict.get('amount'),
            vendingmachine_id=dto_dict.get('vendingmachine_id'),
        )
