from __future__ import annotations
from typing import Dict, Any
from app import db

class TransactionLog(db.Model):
    __tablename__ = 'transactionlog'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transaction_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    vendingmachine_id = db.Column(db.Integer, db.ForeignKey('vendingmachine.id'), nullable=False)
    technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'), nullable=False)  # Зовнішній ключ до Technician

    vendingmachine = db.relationship("VendingMachine", backref="transactions")

    # Встановлюємо зв'язок з Technician (Один до багатьох)
    technician = db.relationship("Technician", back_populates="transaction_logs")

    def __repr__(self) -> str:
        return f"Transaction(id={self.id}, transaction_date='{self.transaction_date}', amount={self.amount})"

    def put_into_dto(self) -> Dict[str, Any]:
        # Додати техніка до DTO тільки через ідентифікатор
        return {
            'id': self.id,
            'transaction_date': self.transaction_date,
            'amount': self.amount,
            'vendingmachine_id': self.vendingmachine_id,
            'technician_id': self.technician.id  # Додаємо тільки id техніка
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TransactionLog:
        return TransactionLog(
            transaction_date=dto_dict.get('transaction_date'),
            amount=dto_dict.get('amount'),
            vendingmachine_id=dto_dict.get('vendingmachine_id'),
            technician_id=dto_dict.get('technician_id'),
        )

