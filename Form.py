from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields import EmailField, DateField


class CreateItemForm(Form):
    item_name = SelectField('Items', [validators.DataRequired()],
                            choices=[('', 'Select'), ('goat', 'Goat Plush'), ('cmug', 'Chicken mug')], default='')
    item_quantity = StringField('Quantity', [validators.DataRequired()])