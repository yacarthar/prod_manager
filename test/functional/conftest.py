"""default fixture for functional test"""

import pytest

from app.api.model import db, Category, User, OrderDetail, Order, Product

@pytest.fixture(scope="package", autouse=True)
def setup_db(client):
    db.session.add_all(
        [
            User(username='Tony', email='tony@gmail.com'),
            User(username='Adam', email='adam@gmail.com'),
            User(username='Maldini', email='maldini@gmail.com'),
            User(username='Sully', email='sully@gmail.com')
        ]
    )
    db.session.add_all(
        [
            Category(name='food'),
            Category(name='vehicle'),
            Category(name='electronic'),
            Category(name='clothes')
        ]
    )
    db.session.add_all(
        [
            Product(name='coconut', price=200, category_id=1),
            Product(name='orange', price=300, category_id=1),
            Product(name='apple', price=400, category_id=1),
            Product(name='lemon', price=250, category_id=1),
            Product(name='mercedes', price=4000, category_id=2),
            Product(name='audi', price=5000, category_id=2),
            Product(name='toyota', price=3500, category_id=2),
            Product(name='samsung phone', price=2000, category_id=3),
            Product(name='huawei phone', price=2000, category_id=3),
            Product(name='macbook', price=5200, category_id=3),
            Product(name='adidas', price=800, category_id=4)
        ]
    )
    db.session.add_all(
        [
            Order(date='2020-05-01', user_id=1),
            Order(date='2020-05-02', user_id=1),
            Order(date='2020-05-03', user_id=2),
            Order(date='2020-05-04', user_id=2),
            Order(date='2020-05-05', user_id=3),
            Order(date='2020-05-06', user_id=3),
            Order(date='2020-05-07', user_id=4),
            Order(date='2020-05-08', user_id=4)
        ]
    )
    db.session.add_all(
        [
            OrderDetail(amount=1, product_id=1, order_id=1),
            OrderDetail(amount=2, product_id=2, order_id=2),
            OrderDetail(amount=3, product_id=3, order_id=3),
            OrderDetail(amount=4, product_id=4, order_id=4),
            OrderDetail(amount=5, product_id=5, order_id=5),
            OrderDetail(amount=6, product_id=6, order_id=6),
            OrderDetail(amount=7, product_id=7, order_id=7),
            OrderDetail(amount=8, product_id=8, order_id=8)
        ]
    )
    db.session.commit()
    yield True

