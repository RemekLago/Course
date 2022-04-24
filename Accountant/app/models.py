from email.policy import default
from app import db
from datetime import datetime

class StockTable(db.Model):
    """The table with the stock status"""
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(64))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<StockTable {}>'.format(self.name)
    
class SaldoTable(db.Model):
    """The table with the whole history balance account, just amounts"""
    id = db.Column(db.Integer, primary_key=True)
    payment = db.Column(db.Integer)
    saldo = db.Column(db.Integer)
    status = db.Column(db.String(16))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<SaldoTable {}>'.format(self.saldo)
    
class HistoryTable(db.Model):
    """The table with the whole history of the account by day"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    saldo = db.Column(db.Integer)
    product = db.Column(db.String(64))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    comment = db.Column(db.String(120), default=None)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<HistoryTable {}>'.format(self.name)
    
class CustomHistoryTable(db.Model):
    """The table with dates that the user put to show the custom history of the account"""
    id = db.Column(db.Integer, primary_key=True)
    period_from = db.Column(db.DateTime)
    period_to = db.Column(db.DateTime)

    def __repr__(self):
        return '<CustomHistoryTable {}>'.format(self.id)