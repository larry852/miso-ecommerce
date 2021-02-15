from flask_sqlalchemy import SQLAlchemy
from .order import Order
from .item import Item

db = SQLAlchemy()

class Detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)    

    order_id = db.Column(db.Integer, db.ForeignKey(Order.id), nullable=True)
    order = db.relationship(Order, uselist=False)

    item_id = db.Column(db.Integer, db.ForeignKey(Item.id), nullable=True)
    item = db.relationship(Item, uselist=False)


