from __future__ import annotations
from typing import Dict, Any
from app import db

class Brand(db.Model):
    __tablename__ = 'brand'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"Brand(id={self.id}, name='{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Brand:
        return Brand(
            name=dto_dict.get('name')
        )


def insert_noname_brands() -> None:
    # Створюємо список нових брендів
    for i in range(1, 11):  # Вставляємо 10 записів
        brand_name = f"Noname{i}"
        new_brand = Brand(name=brand_name)
        db.session.add(new_brand)

    # Підтверджуємо зміни в базі даних
    db.session.commit()
    print("10 Noname brands have been added successfully.")