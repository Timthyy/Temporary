import shelve, hashlib
from flask import Flask, render_template, request, redirect, url_for, session
from Form import *
from Rewards import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/rewards')  # redirect page to rewards.html when click on navbar
def rewards():
    return render_template('rewards.html')


@app.route('/createItem', methods=['GET', 'POST'])
def create_item():
    item_form = CreateItemForm(request.form)
    if request.method == 'POST' and item_form.validate():
        items_dict = {}
        db = shelve.open('cart.db', 'c')

        try:
            items_dict = db['Cart']
        except:
            print("Error in retrieving Cart Items from cart.db.")

        items = Item(item_form.item_name.data, item_form.item_quantity.data)

        items_dict[items.get_order_id()] = items
        db['Cart'] = items_dict

        db.close()


    return render_template('rewards.html', form=item_form)


if __name__ == '__main__':
    app.run()
