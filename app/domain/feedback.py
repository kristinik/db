from __future__ import annotations
from typing import Dict, Any
from app import db
from sqlalchemy import event, select
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy.orm import class_mapper

class Feedback(db.Model):
    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vendingmachine_id = db.Column(db.Integer, nullable=False)  # Без ForeignKey
    feedback_date = db.Column(db.Date, nullable=False)
    rating = db.Column(db.SmallInteger, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def __repr__(self) -> str:
        return f"Feedback(id={self.id}, machine_id={self.vendingmachine_id}, rating={self.rating})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Перетворює об'єкт на DTO (Data Transfer Object) для передачі в контролери чи API.
        """
        return {
            'id': self.id,
            'vendingmachine_id': self.vendingmachine_id,
            'feedback_date': self.feedback_date,
            'rating': self.rating,
            'comment': self.comment,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Feedback:
        """
        Створює об'єкт Feedback з DTO (Data Transfer Object).
        """
        return Feedback(
            vendingmachine_id=dto_dict.get('vendingmachine_id'),
            feedback_date=dto_dict.get('feedback_date'),
            rating=dto_dict.get('rating'),
            comment=dto_dict.get('comment'),
        )

@event.listens_for(Feedback, "before_insert")
def check_machine_exists(mapper, connection, target):
    """
    Перевіряє, чи існує vendingmachine_id у таблиці vending_machine перед вставкою нового Feedback.
    """
    vendingmachine_table = db.Table('vendingmachine', db.metadata, autoload_with=db.engine)

    # Перевірка на наявність автомату з target.vendingmachine_id
    machine_exists = connection.execute(
        select(vendingmachine_table.c.id).where(vendingmachine_table.c.id == target.vendingmachine_id)
    ).first()

    if not machine_exists:
        raise ValueError(f"Vending machine with id {target.vendingmachine_id} does not exist in vendingmachine table.")




def insert_into_feedback(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Параметризована вставка в таблицю feedback через SQLAlchemy модель Feedback.

    :param data: Словник із даними для вставки (ключі — імена колонок, значення — значення).
    :return: Словник із вставленими даними, включаючи згенерований primary key.
    """
    # Отримуємо таблицю з моделі Feedback
    table = class_mapper(Feedback).mapped_table

    # Перевірка наявності всіх потрібних колонок у таблиці
    missing_columns = [key for key in data.keys() if key not in table.columns]
    if missing_columns:
        raise ValueError(f"Invalid columns for table '{Feedback.__tablename__}': {missing_columns}")

    # Формуємо вставку
    insert_stmt = table.insert().values(**data)

    try:
        # Виконуємо вставку та комітимо транзакцію
        result = db.session.execute(insert_stmt)
        db.session.commit()

        # Отримуємо ID з результату вставки
        inserted_id = result.inserted_primary_key[0]  # отримуємо ID з згенерованого primary key

        # Повертаємо результат, але без вказування імені таблиці
        return {**data, "id": inserted_id}
    except SQLAlchemyError as e:
        db.session.rollback()
        raise ValueError(f"Error inserting into table '{Feedback.__tablename__}': {e}")
