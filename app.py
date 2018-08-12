from datetime import datetime
from flask import (Flask, render_template, request, redirect, url_for, flash)
import db

app = Flask(__name__)
app.secret_key = '4gdff25EYE33";"№%'

products = db.get_products()
orders = {}
num = 0
order_ok = False

@app.route('/')
def index():
    return render_template('products.html', products = products)

@app.route('/make_order/', methods = ['POST', 'GET'])
def order():
    if request.method == 'POST':

        order = {

            'client' : {
                'name': request.form['name'],
                'surname': request.form['surname'],
                'adress': request.form['adress'],
                'phone': request.form['phone']
            },
            'pizza' : {},
            'status' : {'Поступил' : datetime.now()}
        }

        global order_ok
        assorts = ['Додо', 'Итальянская', 'Мексиканская', 'Пеперони', 'Супермясная']

        for assort in assorts:
            value = request.form[assort]
            if int(value) > 0:
                order['pizza'].update({assort : value})
                order_ok = True

        if order_ok:
            global num
            num = num + 1

            last_client_id = db.add_client(request.form['name'], request.form['surname'], request.form['adress'], request.form['phone'])
            last_order_id = db.add_order(last_client_id, "Поступил")

            for pizza_name, pizza_value in order['pizza'].items():
                db.add_pizza(last_order_id, pizza_name, pizza_value)

            flash('{}, Ваш заказ принят. Менеджер перезвонит на номер {}.'.format(order['client']['name'], order['client']['phone']))
            order_ok = False
            return redirect(url_for('index'))
        else:
            flash('Необходимо указать количество выбранной пиццы для заказа.')
            return render_template('make_order.html', products=products)
    else:
        return render_template('make_order.html', products = products)

@app.route('/orders/', methods = ['POST', 'GET'])
def orders_list():
    if request.method == 'POST':
        splitted_status = request.form.get('select_status').split("-")

        if splitted_status[1] == 'Удалить':
            db.del_order(splitted_status[0])
            flash('Заказ№{} удален.'.format(splitted_status[0]))
            return render_template('orders.html', orders=db.get_orders())
        else:
            db.update_status(splitted_status[0], splitted_status[1])
            return render_template('orders.html', orders = db.get_orders())
    else:
        return render_template('orders.html', orders = db.get_orders())

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')