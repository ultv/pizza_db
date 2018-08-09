# Сервис для заказа пиццы.

## Технологии

* [Flask](http://flask.pocoo.org/)
* [Bootstrap](https://getbootstrap.com)

## Инструкция

* Установка зависимостей
```
pip install -r requirements.txt
```

* Инициализация базы данных (создание схемы БД)
```
python init_db.py
```

* Загрузка фейковых данных для тестирования
```
python load_fixtures.py
```

* Запуск веб-сервиса
```
flask run
```
