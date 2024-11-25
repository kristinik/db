from __future__ import annotations
from typing import Dict, Any
from app import db

class Technician(db.Model):
    __tablename__ = 'technician'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=True)

    # Зворотний зв'язок з TransactionLog (Один до багатьох)
    transaction_logs = db.relationship("TransactionLog", back_populates="technician")

    def __repr__(self) -> str:
        return f"Technician(id={self.id}, name='{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        # Вивести всі транзакції цього техніка в DTO, тільки ідентифікатори транзакцій
        return {
            'id': self.id,
            'name': self.name,
            'contact_info': self.contact_info,
            'transaction_logs': [log.id for log in self.transaction_logs]  # Тільки id транзакцій
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Technician:
        return Technician(
            name=dto_dict.get('name'),
            contact_info=dto_dict.get('contact_info'),
        )
