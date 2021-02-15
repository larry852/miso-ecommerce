from flask_sqlalchemy import SQLAlchemy
from .user import User
import enum
from datetime import datetime


db = SQLAlchemy()

class StatusType(enum.Enum):
    SUCCESSFUL = "Succesful transaction"
    DECLINED = "Transaction declined"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_amount = db.Column(db.Integer, nullable=False)
    coupon_amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum(StatusType), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=True)
    user = db.relationship(User, uselist=False)


