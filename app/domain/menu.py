from __future__ import annotations
from typing import Dict, Any
from app import db


class Menu(db.Model):
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    availability = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    vendingmachine_id = db.Column(db.Integer, db.ForeignKey('vendingmachine.id'), nullable=False)

    product = db.relationship("Product", backref=db.backref('menu_entries', cascade="all, delete-orphan"))
    vending_machine = db.relationship("VendingMachine", backref=db.backref('menu_entries', cascade="all, delete-orphan"))

    def __repr__(self) -> str:
        return f"Menu(id={self.id}, availability={self.availability})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'availability': self.availability,
            'product_id': self.product_id,
            'vendingmachine_id': self.vendingmachine_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Menu:
        return Menu(
            availability=dto_dict.get('availability'),
            product_id=dto_dict.get('product_id'),
            vendingmachine_id=dto_dict.get('vendingmachine_id'),
        )


def insert_product_to_vending_machine(product_name: str, vendingmachine_address: str, availability: int) -> dict:
    from app.domain import Product, VendingMachine


    product = Product.query.filter_by(name=product_name).first()

    vendingmachine = VendingMachine.query.filter_by(address=vendingmachine_address).first()

    if not product:
        raise ValueError(f"Product with name '{product_name}' not found.")
    if not vendingmachine:
        raise ValueError(f"Vending machine with address '{vendingmachine_address}' not found.")

    menu_entry = Menu(
        availability=availability,
        product_id=product.id,
        vendingmachine_id=vendingmachine.id
    )

    db.session.add(menu_entry)
    db.session.commit()

    return {
        "product_id": product.id,
        "vendingmachine_id": vendingmachine.id
    }

