from xmlrpc.client import DateTime
from wtforms import StringField, IntegerField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError

class SaldoForm(FlaskForm):
    comment = StringField('comment', validators=[DataRequired()])
    saldo = IntegerField('saldo', validators=[DataRequired()])
    submit = SubmitField('Submit')

class BuyForm(FlaskForm):
    product = StringField('product', validators=[DataRequired()])
    price = IntegerField('price', validators=[DataRequired()])
    quantity = IntegerField('price', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class SaleForm(FlaskForm):
    product = StringField('product', validators=[DataRequired()])
    price = IntegerField('price', validators=[DataRequired()])
    quantity = IntegerField('price', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class HistoryForm(FlaskForm):
    period_from = DateTime('date_from')
    period_to = DateTime('date_to')
    submit = SubmitField('Submit')