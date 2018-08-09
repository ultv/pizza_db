import db

fixtures_sql = '''
INSERT INTO products (id, name, description, price, image) VALUES (
    1, "Додо", "Ветчина, говядина (фарш), пикантная пепперони, томатный соус, шампиньоны, сладкий перец, лук красный, моцарелла и маслины.",
    385, "/static/image/dodo.jpg"
);
INSERT INTO products (id, name, description, price, image) VALUES (
    2, "Итальянская", "Пикантная пепперони, томатный соус, шампиньоны, моцарелла, маслины и орегано.",
    375, "/static/image/italian.jpg"
);
INSERT INTO products (id, name, description, price, image) VALUES (
    3, "Мексиканская", "Цыпленок, томатный соус, шампиньоны, сладкий перец, лук красный, моцарелла, острый перец халапеньо и томаты.",
    375, "/static/image/mexican.jpg"
);
INSERT INTO products (id, name, description, price, image) VALUES (
    4, "Пеперони", "Пикантная пепперони, томатный соус и моцарелла.",
    375, "/static/image/pepperoni.jpg"
);
INSERT INTO products (id, name, description, price, image) VALUES (
    5, "Супермясная", "Цыпленок, говядина (фарш), пикантная пепперони, томатный соус, острая чоризо, моцарелла и бекон.",
    395, "/static/image/supermeat.jpg"
);
'''

def run():
    conn, cur = db.get_db()
    cur.executescript(fixtures_sql)
    conn.commit()

if __name__ == '__main__':
    run()