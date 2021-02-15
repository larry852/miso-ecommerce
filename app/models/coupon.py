from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Coupon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Integer, nullable=False)