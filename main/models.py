from . import db
from sqlalchemy import Column, Float, Integer, String, ForeignKey

class Bill(db.Model):
    __tablename__ = 'bills'

    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Float(precision=10), nullable=False)
    sub_bills = db.relationship('SubBill', backref='bill_sub_bills_backref', primaryjoin="Bill.id == SubBill.bill_id")

class SubBill(db.Model):
    __tablename__ = 'sub_bills'

    id = db.Column(Integer, primary_key=True)
    amount = db.Column(Float(precision=10), nullable=False)
    reference = db.Column(String)
    bill_id = db.Column(db.Integer, db.ForeignKey("bills.id"), nullable=False)
    bill = db.relationship('Bill', backref='sub_bills_backref')
