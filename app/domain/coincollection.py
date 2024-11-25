from __future__ import annotations
from typing import Dict, Any
from app import db

class CoinCollection(db.Model):
    __tablename__ = 'coincollection'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    collection_date = db.Column(db.Date, nullable=False)
    amount_collected = db.Column(db.Numeric(10, 2), nullable=False)
    vendingmachine_id = db.Column(db.Integer, db.ForeignKey('vendingmachine.id'), nullable=False)

    vendingmachine = db.relationship("VendingMachine", backref="coincollections")

    def __repr__(self) -> str:
        return f"CoinCollection(collection_id={self.id}, collection_date='{self.collection_date}', amount_collected={self.amount_collected})"


    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'collection_id': self.id,
            'collection_date': self.collection_date,
            'amount_collected': self.amount_collected,
            'vendingmachine_id': self.vendingmachine_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CoinCollection:
        return CoinCollection(
            collection_date=dto_dict.get('collection_date'),
            amount_collected=dto_dict.get('amount_collected'),
            vendingmachine_id=dto_dict.get('vendingmachine_id'),
        )



def get_through_collection_stat(stat_type: str):
    """
    Функція для отримання статистичних даних (MAX, MIN, SUM, AVG) для стовпця `amount_collected` таблиці `coincollection`.

    :param stat_type: Тип статистики ('MAX', 'MIN', 'SUM', 'AVG')
    :return: Значення статистики або -1, якщо операція не підтримується
    """
    if stat_type == 'MAX':
        result = db.session.query(db.func.max(CoinCollection.amount_collected)).scalar()
        return result
    elif stat_type == 'MIN':
        result = db.session.query(db.func.min(CoinCollection.amount_collected)).scalar()
        return result
    elif stat_type == 'SUM':
        result = db.session.query(db.func.sum(CoinCollection.amount_collected)).scalar()
        return result
    elif stat_type == 'AVG':
        result = db.session.query(db.func.avg(CoinCollection.amount_collected)).scalar()
        return result
    else:
        return -1
