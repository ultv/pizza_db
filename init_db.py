import db

shema_sql = '''
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS pizza;
DROP TABLE IF EXISTS products;

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    date TIMESTAMP NOT NULL        
);

CREATE TABLE client (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    adress TEXT NOT NULL,
    phone TEXT NOT NULL
);

CREATE TABLE pizza (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    value INTEGER NOT NULL    
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL,
    image TEXT NOT NULL
);
'''

def run():
    conn, cur = db.get_db()
    cur.executescript(shema_sql)

if __name__ == ("__main__"):
    run()



