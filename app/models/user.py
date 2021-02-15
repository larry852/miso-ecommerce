from flask_sqlalchemy import SQLAlchemy
from .coupon import Coupon
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    coupon_id = db.Column(db.Integer, db.ForeignKey(Coupon.id), nullable=True)
    coupon = db.relationship(Coupon, uselist=False)