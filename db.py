import datetime
import sqlite3
from os import path

def get_db():
    #conn = sqlite3.connect("pizza.db")

    ROOT = path.dirname(path.realpath(__file__))
    conn = sqlite3.connect(path.join(ROOT, "pizza.db"))

    cur = conn.cursor()
    return conn, cur

def get_products():
    conn, cur = get_db()

    products_rows = cur.execute(
        'SELECT id, name, description, price, image FROM products ORDER BY id').fetchall()

    products = []

    for product_row in products_rows:
        product = {
            "id" : product_row[0],
            "name" : product_row[1],
            "description" : product_row[2],
            "price" : product_row[3],
            "image" : product_row[4]
        }

        products.append(product)
    return products


def add_client(name, surname, adress, phone):
    conn, cur = get_db()

    cur.execute(
        'INSERT INTO client (name, surname, adress, phone) VALUES (?,?,?,?)',
        [name, surname, adress, phone]
    )

    conn.commit()
    return cur.lastrowid

def add_pizza(order_id, name, value):
    conn, cur = get_db()

    cur.execute(
        'INSERT INTO pizza (order_id, name, value) VALUES (?, ?,?)',
        [order_id, name, value]
    )

    conn.commit()
    return cur.lastrowid

def add_order(client_id, status):
    conn, cur = get_db()

    cur.execute(
        'INSERT INTO orders (client_id, status, date) VALUES (?,?,?)',
        [client_id, status, datetime.datetime.now().replace(microsecond=0)]
    )

    conn.commit()
    return cur.lastrowid

def get_order():
    conn, cur = get_db()

    order_rows = cur.execute(
        'SELECT id, client_id, status, date FROM orders ORDER BY id').fetchall()

    orders = {}

    for order_row in order_rows:
        client_id = order_row[1]
        client = get_client(client_id)
        pizza = get_pizza(order_row[0])
        order = {
            'client': {
                'name': client['name'],
                'surname': client['surname'],
                'adress': client['adress'],
                'phone': client['phone']
            },
            'pizza' : pizza,
            'status': { order_row[2]: order_row[3]}
        }
        orders.update({order_row[0]: order})

    return orders

def get_client(client_id):
    conn, cur = get_db()

    client_row = cur.execute('SELECT id, name, surname, adress, phone FROM client WHERE id = ?', [client_id]).fetchone()

    client = {
        "id" : client_row[0],
        "name" : client_row[1],
        "surname" : client_row[2],
        "adress" : client_row[3],
        "phone" : client_row[4]
    }

    return client

def get_pizza(order_id):
    conn, cur = get_db()

    pizza = {}

    pizza_rows = cur.execute('SELECT order_id, name, value FROM pizza WHERE order_id = ?', [order_id]).fetchall()

    for pizza_row in pizza_rows:
        pizza.update({pizza_row[1]: pizza_row[2]})

    return pizza

def update_status(id, status):
    conn, cur = get_db()

    cur.execute('UPDATE orders SET status = ? WHERE id = ?', [status, id])
    conn.commit()

